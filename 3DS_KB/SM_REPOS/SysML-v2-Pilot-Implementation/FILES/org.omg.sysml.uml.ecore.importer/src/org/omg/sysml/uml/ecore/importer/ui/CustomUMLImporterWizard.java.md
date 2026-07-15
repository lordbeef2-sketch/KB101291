# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/ui/CustomUMLImporterWizard.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/ui/CustomUMLImporterWizard.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.uml.ecore.importer/src/org/omg/sysml/uml/ecore/importer/ui/CustomUMLImporterWizard.java
- source_bytes: 1428
- source_sha256: `842bada9955b74d3d1798700f39a768c3e88b34e83785c186bde4c01fbb29293`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * Copyright (c) 2006, 2007 IBM Corporation and others.
 * All rights reserved.   This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v20.html
 *
 * Contributors:
 *   IBM - initial API and implementation
 *
 * $Id: UMLImporterWizard.java,v 1.4 2007/05/30 20:11:19 khussey Exp $
 */
package org.omg.sysml.uml.ecore.importer.ui;

import org.eclipse.emf.converter.ModelConverter;
import org.eclipse.emf.importer.ui.contribution.base.ModelImporterPackagePage;
import org.eclipse.uml2.uml.ecore.importer.ui.UMLImporterDetailPage;
import org.eclipse.uml2.uml.ecore.importer.ui.UMLImporterWizard;
import org.omg.sysml.uml.ecore.importer.CustomUMLImporter;

public class CustomUMLImporterWizard extends UMLImporterWizard {

	@Override
	protected ModelConverter createModelConverter() {
		return new CustomUMLImporter();
	}

	@Override
	public void addPages() {
		UMLImporterDetailPage detailPage = new CustomUMLImporterDetailPage(getModelImporter(), "UMLImporterDetailPage"); //$NON-NLS-1$
		addPage(detailPage);

		ModelImporterPackagePage packagePage = new ModelImporterPackagePage(getModelImporter(),
				"UMLImporterPackagePage") { //$NON-NLS-1$
		};

		packagePage.setShowReferencedGenModels(true);
		addPage(packagePage);
	}
}
````
