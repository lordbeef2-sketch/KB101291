# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext/src/org/omg/sysml/xtext/scoping/SysMLScopeProvider.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext/src/org/omg/sysml/xtext/scoping/SysMLScopeProvider.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext/src/org/omg/sysml/xtext/scoping/SysMLScopeProvider.xtend
- source_bytes: 3263
- source_sha256: `09aff6bd17292eb1572c5da8c773820634942fcb1545399efa15f7d441b2866d`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2025 Model Driven Solutions, Inc.
 *    
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * Eclipse Public License for more details.
 * 
 * You should have received a copy of the Eclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 * 
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 * 
 * Contributors:
 *  Ed Seidewitz, MDS
 * 
 *****************************************************************************/
package org.omg.sysml.xtext.scoping

import org.omg.kerml.xtext.scoping.KerMLScopeProvider
import org.eclipse.emf.ecore.EObject
import org.eclipse.emf.ecore.EReference
import org.omg.sysml.lang.sysml.Membership
import org.omg.sysml.lang.sysml.TransitionUsage
import org.omg.sysml.lang.sysml.FeatureMembership
import org.omg.sysml.lang.sysml.ReferenceSubsetting
import org.omg.sysml.lang.sysml.SuccessionAsUsage
import org.omg.sysml.lang.sysml.FeatureChaining

/**
 * This class contains custom scoping description.
 * 
 * See https://www.eclipse.org/Xtext/documentation/303_runtime_concepts.html#scoping
 * on how and when to use it.
 */
class SysMLScopeProvider extends KerMLScopeProvider {
	
	def EObject featureRelationship(EObject context) {
		if (context instanceof FeatureChaining) {
			var featureChained = context.featureChained
			val ownedFeatureChainings = featureChained.ownedFeatureChaining
			val i = ownedFeatureChainings.indexOf(context)
			if ( i <= 0) {
				return featureChained.owningRelationship
			}
		}
		return context
	}
	
	override getScope(EObject context, EReference reference) {
		var relationship = context.featureRelationship

		// Scope a TransitionUsage source to the owningNamespace of the TransitionUsage
		if (relationship instanceof Membership) {
			val owningNamespace = relationship.membershipOwningNamespace;
			if (owningNamespace instanceof TransitionUsage && 
				relationship == owningNamespace.ownedMembership.filter[mem | !(mem instanceof FeatureMembership)].head) {
				return owningNamespace.scope_owningNamespace(context, reference)
			}
		
		// Scope a TransitionUsage target to the owningNamespace of the TransitionUsage
		} else if (relationship instanceof ReferenceSubsetting) {
			val owningFeature = relationship.owningFeature
			val owningType = owningFeature.owningType
			if (owningType instanceof SuccessionAsUsage && owningType.ownedEndFeature.indexOf(owningFeature) == 1) {
				val outerNamespace = owningType.owningNamespace
				if (outerNamespace instanceof TransitionUsage && owningType === (outerNamespace as TransitionUsage).succession) {
					return outerNamespace.scope_owningNamespace(context, reference)
				}
			}
		}
		return super.getScope(context, reference)
	}
}

````
