# NOMAGIC ATTACHMENT: FixEObjectNotFoundErrors-sysml_v2-2026xHF1.groovy

- attachment_id: `312246978`
- space_key: `SYSML2P`
- parent_page_id: `312246975`
- parent_page_title: (2026x) Managing project imports in the local repository
- media_type: `application/octet-stream`
- reported_bytes: 11612
- download_url: https://docs.nomagic.com/download/attachments/312246975/FixEObjectNotFoundErrors-sysml_v2-2026xHF1.groovy?version=1&modificationDate=1781081343363&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `9bb67f020fa5fa499a0f1f8ba4d0705b0039ef4b2b931ad814c7c1632b65bf00`

## EXACT ATTACHMENT SOURCE

````groovy
package com.nomagic.magicdraw

import com.dassault_systemes.modeler.kerml.model.cache.RelationshipCache;
import com.nomagic.ci.persistence.IPrimaryProject;
import com.nomagic.esi.api.*;
import com.nomagic.esi.core.msg.info.Ref;
import com.nomagic.esi.core.msg.info.impl.EObjectData;
import com.nomagic.esi.core.msg.info.impl.KryogenicEObjectData
import com.nomagic.esi.emf.EsiResourceImpl;
import com.nomagic.esi.emf.EsiResourceSetImpl;
import com.nomagic.esi.emf.impl.EsiObjectImpl;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.magicdraw.core.Project;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.eclipse.emf.ecore.EReference;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.resource.Resource;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;


Script.fix();

// tested with CEA 2026xHF1 Build: 2025-12-05 (2026.0.0-99-55fec9c2
/**
 * The script is designed to fix TWC/local repository project data when the project elements with references to elements which are not accessible by traversing
 * containment tree. In other words the project contains elements which are in state CLEAN, they are not added into existing element neither resource and the
 * project contains normal elements which still references such ghost elements.
 *
 * Additionally relationship cache is rebuilt
 */
public class Script
{
	private static final Logger LOG = LogManager.getLogger("fix-project");
	private static boolean clean = true;

	private static String printFD(FeaturedData d)
	{
		return String.format("%s{id=%s}", d.getEClassName(), d.getID());
	}
	private static String print(EsiObject obj)
	{
		return String.format("%s{id=%s}", obj.eClass().getName(), obj.esiID());
	}

	public static void fix()
	{
		Project project = Application.getInstance().getProject();
		if (project != null && project.isEsiProject())
		{
			LOG.info("Analysing project {}", project.getName());
			IPrimaryProject primaryProject = project.getPrimaryProject();


			Set<UUID> allIDs = new HashSet<>();
			for (EsiResource r : primaryProject.getResourceSet().getResources() )
			{
				UUID resourceID = r.getID();
				Session session = r.getResourceSet().getSession();
				long version = r.getCommitInfo().getID();
				LOG.info("Collecting object identifiers...");
				session.getCacheManager().readDataFromCache(resourceID, version, d -> {
					UUID id = d.getID();
					allIDs.add(id);
				});
			}

			EsiResource resource = (EsiResource) primaryProject.getResourceSet().getResources().get(0);
			UUID resourceID = resource.getID();
			long version = resource.getCommitInfo().getID();

			LOG.info("Object identifiers collected");
			LOG.info("Starting analysis...");
			Set<UUID> unresolvable = new HashSet<>();
			Set<UUID> forDeleting = new HashSet<>();
			Set<Entry> illegalRefs = new HashSet<>();
			AtomicBoolean reanalyze = new AtomicBoolean(false);
			do
			{
				reanalyze.set(false);
				Session session = resource.getResourceSet().getSession();
				session.getCacheManager().readDataFromCache(resourceID, version, d -> {
					UUID id = d.getID();
					Ref container = ((KryogenicEObjectData) d).getContainer();
					int containerFeatureID = d.getContainerFeatureID();
					int result = checkValue(container, allIDs, unresolvable, illegalRefs, forDeleting, id, containerFeatureID, -1);

					if (result == 2)
					{
						// container reference unresolvable
						if (forDeleting.add(id))
						{
							LOG.info("{} container reference {} can't be resolved", printFD(d), container);
							reanalyze.set(true);
						}
					}

					int featuresCount = d.getFeatureCount();
					for (int i = 0; i < featuresCount; i++)
					{
						Object value = d.getFeatureValue(i);
						if (value instanceof Collection)
						{
							Collection collection = (Collection)value;
							int index = 0;
							for (Object object : collection)
							{
								checkValue(object, allIDs, unresolvable, illegalRefs, forDeleting, id, i, index);
								index++;
							}
						}
						else
						{
							checkValue(value, allIDs, unresolvable, illegalRefs, forDeleting, id, i, -1);
						}
					}
				});
			}
			while (reanalyze.get());
			LOG.info("Model analysis completed");
			LOG.info("Found objects what should be deleted: {}", forDeleting.size());
			LOG.info("Found references what should be deleted: {}", illegalRefs.size());

			if (clean)
			{
				LOG.info("Starting model fixing");
				EsiResourceSetImpl resourceSet = (EsiResourceSetImpl) resource.getResourceSet();
				List<EObjectStateChangedListener> listeners = List.copyOf(resourceSet.getEObjectStateChangedListeners());
				EventLogger eventLogger = new EventLogger();
				for (EObjectStateChangedListener listener : listeners)
				{
					resourceSet.removeEObjectStateChangedListener(listener);
				}
				resourceSet.addEObjectStateChangedListener(eventLogger);
				try
				{
					LOG.info("Starting references clearing");
					for (Entry entry : illegalRefs)
					{
						EsiObject object = resource.getObject(entry.id);
						EObjectData data = ((EsiObjectImpl) object).esiData();
						EStructuralFeature feature = object.eClass().getEStructuralFeature(entry.featureID);
						if (feature.isMany())
						{
							List originalValue = (List) data.getFeatureValue(entry.featureID);
							List<Ref> modifiedValue = new ArrayList<>(originalValue);
							Ref removedValue = removeValue(entry, modifiedValue);
							data.setFeatureValue(entry.featureID, modifiedValue, false);
							LOG.info("Removed object {} reference {} value {} at index={}",
									 printFD(data),
									 feature.getContainerClass().getName() + "." +  feature.getName(),
									 removedValue,
									 originalValue.indexOf(removedValue));
						}
						else
						{
							Object valueInHolder = data.getFeatureValue(entry.featureID);
							data.setFeatureValue(entry.featureID, null, false);
							LOG.info("Removed object {} reference {} value {}",
									 printFD(data),
									 feature.getContainerClass().getName() + "." +  feature.getName(),
									 valueInHolder);
							if (feature instanceof EReference && feature.isContainer())
							{
								Ref oldContainer = data.getContainer();
								data.unsetContainer(false);
								LOG.info("Removed object {} container reference {} value {}",
										 printFD(data),
										 feature.getContainerClass().getName() + "." +  feature.getName(),
										 oldContainer);

							}
						}
						markAsDirty(object);
					}
					LOG.info("References cleared");
					LOG.info("Starting deleting of illegal objects");
					for (UUID uuid : forDeleting)
					{
						EsiObject object = resource.getObject(uuid);
						((Resource.Internal) resource).detached(object);
						LOG.info("Deleted {}", print(object));
					}
					LOG.info("Deleting of illegal objects completed");
				}
				catch (Exception e)
				{
					LOG.error("Project data fixing failed. Please close the project without committing it.", e);
				}
				finally
				{
					resourceSet.removeEObjectStateChangedListener(eventLogger);
					for (EObjectStateChangedListener listener : listeners)
					{
						resourceSet.addEObjectStateChangedListener(listener);
					}
					for (StateChangeEvent event : eventLogger.events)
					{
						if (event.object != null)
						{
							if (!forDeleting.contains(event.object.esiID()))
							{
								listeners.forEach(e -> e.stateChanged(event.resource, event.object, event.oldState, event.newState));
							}

						}
						if (event.objects != null)
						{
							Collection<EsiObject> filteredObjects = new ArrayList<>(event.objects);
							filteredObjects.removeIf(o -> forDeleting.contains(o.esiID()));
							if (!filteredObjects.isEmpty())
							{
								listeners.forEach(e -> e.stateChanged(event.resource, filteredObjects, event.oldState, event.newState));
							}
						}
					}
				}
			}
			LOG.info("Model analysis and fixing completed");

			LOG.info("Rebuilding cache...");
			RelationshipCache.getInstance(project).rebuildCache();
			LOG.info("Rebuilding cache done");

		}
	}

	private static Ref removeValue(Entry entry, List<Ref> list)
	{
		for (Iterator<Ref> iterator = list.iterator(); iterator.hasNext(); )
		{
			Ref ref = iterator.next();
			if (ref.getObjectID().equals(entry.value))
			{
				iterator.remove();
				return ref;
			}
		}
		return null;
	}

	private static void markAsDirty(EsiObject object)
	{
		(object.eResource() as EsiResource).markObjectAsChanged(object)
	}

	// 0 - not reference
	// 1 - ref resolvable
	// 2 - ref unresolvable
	private static int checkValue(Object value,
								  Set<UUID> allIds,
								  Set<UUID> unresolvable,
								  Set<Entry> referencing,
								  Set<UUID> forDeleting,
								  UUID id,
								  int featureID,
								  int index)
	{
		if (value instanceof Ref)
		{
			Ref ref = (Ref) value;
			UUID objectID = ref.getObjectID();
			if (forDeleting.contains(objectID) || !allIds.contains(objectID))
			{
				unresolvable.add(objectID);
				referencing.add(new Entry(id, featureID, index, objectID));
				return 2;
			}
			return 1;
		}
		return 0;
	}

	private static class Entry
	{
		private final UUID id;
		private final int featureID;
		private final int index;
		private final UUID value;

		public Entry(UUID id, int featureID, int index, UUID value)
		{
			this.id = id;
			this.featureID = featureID;
			this.index = index;
			this.value = value;
		}

		@Override
		public boolean equals(Object o)
		{
			if (o == null || getClass() != o.getClass())
			{
				return false;
			}
			Entry entry = (Entry) o;
			return featureID == entry.featureID && index == entry.index && Objects.equals(id, entry.id) && Objects.equals(value, entry.value);
		}

		@Override
		public int hashCode()
		{
			return Objects.hash(id, featureID, index, value);
		}
	}

	private static class EventLogger implements EObjectStateChangedListener
	{
		private List<StateChangeEvent> events = new ArrayList<>();

		@Override
		public void stateChanged(EsiResource resource, Collection<EsiObject> objects, State oldState, State newState)
		{
			events.add(new StateChangeEvent(resource, objects, oldState, newState));
		}

		@Override
		public void stateChanged(EsiResource resource, EsiObject object, State oldState, State newState)
		{
			events.add(new StateChangeEvent(resource, object, oldState, newState));
		}
	}

	private static class StateChangeEvent
	{
		private final EsiResource resource;
		private final Collection<EsiObject> objects;
		private final State oldState;
		private final State newState;
		private final EsiObject object;

		public StateChangeEvent(EsiResource resource, EsiObject object, State oldState, State newState)
		{
			this.resource = resource;
			this.object = object;
			this.oldState = oldState;
			this.newState = newState;
			this.objects = null;
		}

		public StateChangeEvent(EsiResource resource, Collection<EsiObject> objects, State oldState, State newState)
		{
			this.resource = resource;
			this.objects = objects;
			this.oldState = oldState;
			this.newState = newState;
			this.object = null;
		}
	}
}

````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "312246978",
  "type": "attachment",
  "status": "current",
  "title": "FixEObjectNotFoundErrors-sysml_v2-2026xHF1.groovy",
  "version": {
    "by": {
      "type": "known",
      "username": "kbe12",
      "userKey": "2c9f81f87674fd7d017a0928ba470000",
      "profilePicture": {
        "path": "/images/icons/profilepics/default.svg",
        "width": 48,
        "height": 48,
        "isDefault": true
      },
      "displayName": "Kristina B.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=2c9f81f87674fd7d017a0928ba470000"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2026-06-10T10:49:03.363+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/312246978/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/312246978"
    }
  },
  "position": -1,
  "container": {
    "id": "312246975",
    "type": "page",
    "status": "current",
    "title": "(2026x) Managing project imports in the local repository",
    "position": 1,
    "extensions": {
      "position": 1
    },
    "_links": {
      "webui": "/spaces/SYSML2P/pages/312246975/2026x+Managing+project+imports+in+the+local+repository",
      "edit": "/pages/resumedraft.action?draftId=312246975&draftShareId=052bd48b-2d12-4bfa-8a30-6f6cb8c086b3",
      "tinyui": "/x/v4KcEg",
      "self": "https://docs.nomagic.com/rest/api/content/312246975"
    },
    "_expandable": {
      "container": "/rest/api/space/SYSML2P",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/312246975/child",
      "restrictions": "/rest/api/content/312246975/restriction/byOperation",
      "history": "/rest/api/content/312246975/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/312246975/descendant",
      "space": "/rest/api/space/SYSML2P",
      "relevantViewRestrictions": "/rest/api/content/312246975/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/octet-stream"
  },
  "extensions": {
    "mediaType": "application/octet-stream",
    "fileSize": 11612,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/312246975/FixEObjectNotFoundErrors-sysml_v2-2026xHF1.groovy?version=1&modificationDate=1781081343363&api=v2",
    "webui": "/spaces/SYSML2P/pages/312246975/2026x+Managing+project+imports+in+the+local+repository?preview=%2F312246975%2F312246978%2FFixEObjectNotFoundErrors-sysml_v2-2026xHF1.groovy",
    "self": "https://docs.nomagic.com/rest/api/content/312246978"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/312246978/child",
    "restrictions": "/rest/api/content/312246978/restriction/byOperation",
    "history": "/rest/api/content/312246978/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/312246978/descendant",
    "space": "/rest/api/space/SYSML2P",
    "relevantViewRestrictions": "/rest/api/content/312246978/restriction/relevantViewRestrictions"
  }
}
````
