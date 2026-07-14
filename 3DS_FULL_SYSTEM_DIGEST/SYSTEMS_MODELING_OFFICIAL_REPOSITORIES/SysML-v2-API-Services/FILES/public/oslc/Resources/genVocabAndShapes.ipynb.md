# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/public/oslc/Resources/genVocabAndShapes.ipynb

- repository: `SysML-v2-API-Services`
- source_path: `public/oslc/Resources/genVocabAndShapes.ipynb`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/public/oslc/Resources/genVocabAndShapes.ipynb
- source_bytes: 144388
- source_sha256: `01aed3a321717b528cd21e4a044065028fdf93eba6c22492f90c2cac47814019`
- decoded_as: `utf-8`

## NORMALIZED NOTEBOOK CELLS

### CELL 1: markdown

# Generate the SysML Vocabulary Terms

Generate the SysML v2 vocabulary from /Users/jamsden/Developer/SysML/SysML-v2-Pilot-Implementation/org.omg.sysml/model/SysML.ecore. This will be the merged KerML and SysML into a single vocabulary with a single namespace.

Set genOASIS = True to generate for OASIS, leave false to generate for OMG



### CELL 2: code

# Initial imports and local methods
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD, RDFS, OWL, DCTERMS, BNode
from pyecore.ecore import EClass, EAttribute, EReference, EString, EObject, EEnum
from pyecore.resources import ResourceSet, URI
from bs4 import BeautifulSoup
import os

genOASIS = False  # set to True to generate OASIS SysML instead of OMG: Deprecated, only generate OMG

# use the class name as a prefix to the attribute name to ensure they are unique
# this should no longer be used, but the method to calculate the qualified name is retained.
def qualident(eClass, eAttribute):
    return eClass.name[0].lower() + eClass.name[1:] + '_' + eAttribute.name[0].capitalize() + eAttribute.name[1:]  

# Get the description of the model element as the first paragraph
# with markdown removed if strip is True (rdfs:comment is a string, not an XMLLiteral)
def comment(eModelElement, strip=True):
    desc = f'{eModelElement.name}.'  # rdfs:comment is required in the vocabulary, this is the default
    a = eModelElement.getEAnnotation('http://www.eclipse.org/emf/2002/GenModel')
    if a is None: return desc
    description = a.details['documentation']
    root = BeautifulSoup(str(description))
    description = root.find('p') 
    if strip:
        text =  description.get_text() # the first paragraph with the HTML stripped out
        if not (text is None or text==''): desc = text
    else:
        # strip off the <p> and </p>, they are not needed and cause the period to appear to be missing to shapechecker
        desc = str(description)[3:-4]  # but include the rest of the markup
    if not desc.endswith('.'): desc = desc + '.'
    return desc


# some useful RDF namespaces
vann = Namespace('http://purl.org/vocab/vann/')
oslc = Namespace('http://open-services.net/ns/core#')
oslc_am = Namespace('http://open-services.net/ns/am#')
oslc_sysml = Namespace('https://www.omg.org/spec/sysml/vocabulary#')  # OMG namespace
if genOASIS: oslc_sysml = Namespace('http://open-services.net/ns/sysml#')  # OASIS namespace

# the OASIS copywrite and license information, not used for OMG 
copyright = """
# Copyright 2024 OASIS Open
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""


### CELL 3: code

# Generate the SysML OSLC vocabulary file

vocab_file = 'SysML-vocab.ttl'
if genOASIS: vocab_file = 'sysml-vocab.ttl'

# create the SysML vocabulary graph, initially empty
g = Graph()
g.bind('oslc_sysml', oslc_sysml)
g.bind('oslc_am', oslc_am)

# add the vocabulary ontology
o = URIRef(oslc_sysml)
g.add((o, RDF.type, OWL.Ontology))
g.add((o, RDFS.label, Literal("OSLC SysML v2 Vocabulary")))
g.add((o, DCTERMS.description, Literal("All vocabulary URIs defined in the OSLC SysML v2 namespace.", datatype=RDF.XMLLiteral)))
g.add((o, DCTERMS.title, Literal("OSLC SysML v2 Vocabulary")))
g.add((o, vann.preferredNamespacePrefix, Literal("oslc_sysml")))
if genOASIS:
    g.add((o, DCTERMS.dateCopyrighted, Literal("2012-2024")))
    g.add((o, DCTERMS.hasVersion, Literal("PSD01")))
    g.add((o, DCTERMS.isPartOf, URIRef('https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/os/sysml-spec.html')))
    g.add((o, DCTERMS.issued, Literal("2024-08-01", datatype=XSD.date)))
    g.add((o, DCTERMS.license, URIRef('http://www.apache.org/licenses/LICENSE-2.0')))
    g.add((o, DCTERMS.publisher,  URIRef('https://open-services.net/about/')))
    g.add((o, DCTERMS.source, URIRef('https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/os/sysml-vocab.ttl')))
else:
    g.add((o, DCTERMS.publisher,  URIRef('https://www.omg.org')))
    g.add((o, DCTERMS.issued, Literal("2025-02-01", datatype=XSD.date)))
    g.add((o, DCTERMS.hasVersion, Literal("V2")))
    g.add((o, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/SysML')))
    g.add((o, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/SysML-vocab.ttl')))
    g.add((o, DCTERMS.license, URIRef('')))

# load the SysML.ecore model - this is the merged KerML and SysML metamodel using a single namespace
rset = ResourceSet()
resource = rset.get_resource(URI('/Users/jamsden/Developer/SysML-v2-Pilot-Implementation/org.omg.sysml/model/sysml_clean.ecore'))
mm_root = resource.contents[0]
rset.metamodel_registry[mm_root.nsURI] = mm_root
# At this point, the .ecore is loaded in the 'rset' as a metamodel


for c in mm_root.eClassifiers:
    # Generate the classes
    if isinstance(c, EClass):
        g.add((oslc_sysml.term(c.name), RDF.type, RDFS.Class))
        if c.name=='Element':
            g.add((oslc_sysml.term(c.name), RDFS.subClassOf, oslc_am.Resource))  # only Element
        if c.eSuperTypes is not None and len(c.eSuperTypes) >= 1:
            for super in c.eSuperTypes:
                g.add((oslc_sysml.term(c.name), RDFS.subClassOf, oslc_sysml.term(super.name)))
        g.add((oslc_sysml.term(c.name), RDFS.label, Literal(c.name)))
        g.add((oslc_sysml.term(c.name), RDFS.comment, Literal(comment(c))))
        g.add((oslc_sysml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_sysml)))

        # generate the properties
        for a in c.eStructuralFeatures:
            name = a.name  # done't use the class name as a prefix to the attribute name to ensure they are unique
            s = oslc_sysml.term(name)
            g.add((s, RDF.type, RDF.Property))
            g.add((s, RDFS.label, Literal(name)))
            # does the property already have a comment?
            pcomment = g.value(s, RDFS.comment)
            if pcomment is not None:
                # This is a property with multiple domains
                # Concatenate the comment for each domain class into a single comment
                pcomment = pcomment + '\n' + c.name+': '+comment(a)
                g.remove((s, RDFS.comment, None))
                g.add((s, RDFS.comment, Literal(pcomment)))
            else:
                g.add((s, RDFS.comment, Literal(c.name+': '+comment(a))))
            g.add((s, RDFS.isDefinedBy, URIRef(oslc_sysml)))
    if isinstance(c, EEnum):
        g.add((oslc_sysml.term(c.name), RDF.type, RDFS.Class))
        g.add((oslc_sysml.term(c.name), RDFS.label, Literal(c.name)))
        g.add((oslc_sysml.term(c.name), RDFS.comment, Literal(comment(c))))
        g.add((oslc_sysml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_sysml)))

        # generate the enumeration literals
        for a in c.eLiterals:
            name = a.name  # don't use the class name as a prefix to the attribute name to ensure they are unique
            s = oslc_sysml.term(name)
            g.add((s, RDF.type, oslc_sysml.term(c.name)))
            g.add((s, RDFS.label, Literal(name)))
            g.add((s, RDFS.comment, Literal(comment(a))))
            g.add((s, RDFS.isDefinedBy, URIRef(oslc_sysml)))
        
g.serialize(destination=f'../{vocab_file}')

if genOASIS:  # add the copyright for OASIS
    with open('../sysml-vocab.ttl','r') as f:
        with open('../temp.ttl','w') as f2: 
            f2.write(copyright)
            f2.write(f.read())
    os.remove('../sysml-vocab.ttl')
    os.rename('../temp.ttl','../sysml-vocab.ttl')

### CELL 4: markdown

# Generate the SysML OSLC constraints
Generate the SysML v2 constraints from /Users/jamsden/Developer/SysML/SysML-v2-Pilot-Implementation/org.omg.sysml/model/SysML.ecore. This will be the merged KerML and SysML into a single vocabulary with a single namespace. 

This depends on the vocabulary that was generated above.

The ResourceShape properties also do not need class prefixes because they are added to the classes using blank nodes which makes them unique.



### CELL 5: code

# Get a list of the properties that are defined in more than one class (ignoring inheritance)
# These need to be added as shape properties using blank nodes to ensure they are properly scoped by the class
# Iterate over all the EClasses in the model and collect the EAttribute and EReference property names
# Then find all the ones that are duplicated
import pandas as pd

allProperties = []
for c in mm_root.eClassifiers:
    if isinstance(c, EClass):
         for a in c.eStructuralFeatures:
              allProperties.append(a.name)
allProperties = pd.Series(allProperties)
multiDefProps = set(allProperties[allProperties.duplicated()]);

### CELL 6: code

# Generate the SysML OSLC constraints
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD, RDFS, OWL, DCTERMS
from pyecore.ecore import EClassifier, EClass, EAttribute, EReference, EString, EObject, EEnum
from pyecore.resources import ResourceSet, URI
from bs4 import BeautifulSoup
import os

shapes_file = 'SysML-shapes.ttl'
if genOASIS: shapes_file = 'sysml-shapes.ttl'

def multiplicity(eAttribute):
    lower = eAttribute.lowerBound
    upper = eAttribute.upperBound
    if lower==1 and upper==1: return oslc['Exactly-one']
    if lower==1 and upper !=0: return oslc['One-or-many']
    if lower==0 and upper==1: return oslc['Zero-or-one']
    if lower==0 and upper !=0: return oslc['Zero-or-many']

def valueType(a):
    match a.eType.name:
        case 'Boolean': return XSD.boolean
        case 'String': return XSD.string
        case 'Real': return XSD.float
        case 'Integer': return XSD.integer
        case _: return oslc_sysml.term(a.eType.name)

def propertyAlreadyAdded(propname, eclass, shape, graph):
    # is the property already ready in this shape
    # Note: the property could be a global property definition or in a blank node
    props = list(graph.objects(shape, oslc.property))
    props = list(map(lambda s: graph.value(s, oslc.name).value, props))
    return propname in props


def addClassProperties(eclass, shape, graph, vocab_namespace, shape_namespace):
    # generate the properties specific to this ResourceShape
    for a in eclass.eStructuralFeatures:
        name = a.name
        cls = vocab_namespace.term(eclass.name)
        prop = vocab_namespace.term(name)
        # does the uninherited property appear in more than one class?
        # if it does, then add the Property constraint using a blank node for the class
        # if not, then define the property so it can be reused where it is inherited
        propval = shape_namespace.term(name)
        if propertyAlreadyAdded(name, eclass, shape, graph): return
        if name in multiDefProps:
            propval = BNode()
        graph.add((shape, oslc.property, propval))

        # and create the oslc:Property elements defined by this EClass
        graph.add((propval, RDF.type, oslc.Property))
        graph.add((propval, oslc.name, Literal(name)))
        graph.add((propval, oslc.occurs, multiplicity(a)))
        graph.add((propval, oslc.propertyDefinition, URIRef(prop)))
        graph.add((propval, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
        if isinstance(a, EReference):
            graph.add((propval, oslc.valueType, oslc.Resource))
            graph.add((propval, oslc.range, vocab_namespace.term(a.eType.name)))
            graph.add((propval, oslc.representation, oslc.Either))
        graph.add((propval, DCTERMS.description, Literal(comment(a,strip=False), datatype=RDF.XMLLiteral)))
        # is the property a redefinition? If so, remove the inherited property
        # Commented out because we decide that 1) redefined properties are inherited in SysML v2
        # and this is the behavior of the Services REST API JSON representation
        """
        redefinitions = a.getEAnnotation('redefines')
        if redefinitions is not None:
            reference = redefinitions.references[0].name
            prop = shape_namespace.term(reference)
            graph.remove((shape, oslc.property, prop))
            # the property could have been added with a blank node
        """


def addSuperclassProperties(eclass, shape, graph, vocab_namespace, shape_namespace):
    if eclass.eSuperTypes is not None and len(eclass.eSuperTypes) >= 1:
        for super in eclass.eSuperTypes:
            # recursively add the properties for the superclasses up the hierarchy
            addSuperclassProperties(super, shape, graph, vocab_namespace, shape_namespace)
            # and add the properties for this superclass
            addClassProperties(super, shape, graph, vocab_namespace, shape_namespace)

    # some useful RDF namespaces
vann = Namespace('http://purl.org/vocab/vann/')
oslc = Namespace('http://open-services.net/ns/core#')
oslc_am = Namespace('http://open-services.net/ns/am#')
oslc_sysml_shapes = Namespace('https://www.omg.org/spec/SysML/20250201/shapes/')  # OMG namespace versioned for constraints
if genOASIS: oslc_sysml_shapes = Namespace('http://open-services.net/ns/sysml/shapes/20250201#')  # OASIS namespace

jazz_am = Namespace('http://jazz.net/ns/dm/linktypes#')

# create the SysML constraints graph, initially empty
g = Graph()
g.bind('oslc_sysml', oslc_sysml)
g.bind('oslc_am', oslc_am)
g.bind('oslc', oslc)
g.bind('oslc_sysml_shapes', oslc_sysml_shapes)
g.bind('jazz_am', jazz_am)

s = URIRef(oslc_sysml_shapes)
g.add((s, RDF.type, oslc.ResourceShapeConstraints))
g.add((s, RDFS.label, Literal("OSLC  System Modeling Language (SysML) Constraints")))
g.add((s, DCTERMS.description, Literal("<p>Constraints on vocabulary terms defined in the OSLC System Modeling Language (SysML) namespace.</p>", datatype=RDF.XMLLiteral)))
g.add((s, DCTERMS.title, Literal("OSLC System Modeling Language (SysML) Version 2.0 Constraints")))

if genOASIS:
    g.add((s, DCTERMS.dateCopyrighted, Literal("2012-2024")))
    g.add((s, DCTERMS.issued, Literal("2025-02-01", datatype=XSD.date)))
    g.add((s, DCTERMS.hasVersion, Literal("PSD01")))
    g.add((s, DCTERMS.isPartOf, URIRef("https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/psd01/sysml-spec.html")))
    g.add((s, DCTERMS.license, URIRef("http://www.apache.org/licenses/LICENSE-2.0")))
    g.add((s, DCTERMS.source, URIRef("https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/psd01/sysml-shapes.ttl")))
else:
    g.add((s, DCTERMS.publisher, URIRef("https://www.omg.org")))
    g.add((s, DCTERMS.issued, Literal("2025-02-01", datatype=XSD.date)))
    g.add((s, DCTERMS.hasVersion, Literal("V2")))
    g.add((s, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/SysML')))
    g.add((s, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/SysML-vocab.ttl')))
    g.add((s, DCTERMS.license, URIRef('')))

# load the SysML.ecore model - this is the merged KerML and SysML metamodel using a single namespace
rset = ResourceSet()
resource = rset.get_resource(URI('/Users/jamsden/Developer/SysML-v2-Pilot-Implementation/org.omg.sysml/model/sysml_clean.ecore'))
mm_root = resource.contents[0]
rset.metamodel_registry[mm_root.nsURI] = mm_root
# At this point, the .ecore is loaded in the 'rset' as a metamodel


for c in mm_root.eClassifiers:
    # Generate the ResourceShape
    if isinstance(c, EClass):
        shape = oslc_sysml_shapes.term(c.name+'Shape')
        g.add((shape, RDF.type, oslc.ResourceShape))  # only Element
        g.add((shape, DCTERMS.title, Literal(c.name+'Shape', datatype=RDF.XMLLiteral)))
        g.add((shape, DCTERMS.description, Literal(comment(c,strip=False),datatype=RDF.XMLLiteral)))
        g.add((shape, oslc.describes, URIRef(oslc_sysml.term(c.name))))

        # add all the properties inherited from all superclasses up to Element
        addSuperclassProperties(c, shape, g, oslc_sysml, oslc_sysml_shapes)
        addClassProperties(c, shape, g, oslc_sysml, oslc_sysml_shapes)

        # add the inherited oslc_am:Resource properties
        g.add((shape, oslc.property, oslc_sysml_shapes.type))
        g.add((shape, oslc.property, oslc_sysml_shapes.dctype))
        g.add((shape, oslc.property, oslc_sysml_shapes.identifier))
        g.add((shape, oslc.property, oslc_sysml_shapes.title))
        g.add((shape, oslc.property, oslc_sysml_shapes.shortTitle))
        g.add((shape, oslc.property, oslc_sysml_shapes.description))
        g.add((shape, oslc.property, oslc_sysml_shapes.source))
        g.add((shape, oslc.property, oslc_sysml_shapes.creator))
        g.add((shape, oslc.property, oslc_sysml_shapes.created))
        g.add((shape, oslc.property, oslc_sysml_shapes.contributor))
        g.add((shape, oslc.property, oslc_sysml_shapes.modified))
        g.add((shape, oslc.property, oslc_sysml_shapes.serviceProvider))
        g.add((shape, oslc.property, oslc_sysml_shapes.instanceShape))
        g.add((shape, oslc.property, oslc_sysml_shapes.derives))
        g.add((shape, oslc.property, oslc_sysml_shapes.elaborates))
        g.add((shape, oslc.property, oslc_sysml_shapes.refine))
        g.add((shape, oslc.property, oslc_sysml_shapes.external))
        g.add((shape, oslc.property, oslc_sysml_shapes.satisfy))
        g.add((shape, oslc.property, oslc_sysml_shapes.trace))
        
    # and create the oslc_am:Resource inherited oslc:Property items
    g.add((oslc_sysml_shapes.type, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.type, oslc.name, Literal('type')))
    g.add((oslc_sysml_shapes.type, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.type, oslc.propertyDefinition, RDF.type))
    g.add((oslc_sysml_shapes.type, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.type, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.type, oslc.range, RDFS.Class))
    g.add((oslc_sysml_shapes.type, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.type, DCTERMS.description, Literal("The resource type URIs.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.dctype, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.dctype, oslc.name, Literal('dctype')))
    g.add((oslc_sysml_shapes.dctype, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.dctype, oslc.propertyDefinition, DCTERMS.type))
    g.add((oslc_sysml_shapes.dctype, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.dctype, oslc.valueType, XSD.string))
    g.add((oslc_sysml_shapes.dctype, DCTERMS.description, Literal("A short string representation for the type, for example ‘Car’.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.identifier, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.identifier, oslc.name, Literal('identifier')))
    g.add((oslc_sysml_shapes.identifier, oslc.occurs, oslc['Exactly-one']))
    g.add((oslc_sysml_shapes.identifier, oslc.propertyDefinition, DCTERMS.identifier))
    g.add((oslc_sysml_shapes.identifier, oslc.readOnly, Literal('true',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.identifier, oslc.valueType, XSD.string))
    g.add((oslc_sysml_shapes.identifier, DCTERMS.description, Literal("""A unique identifier for a resource. Typically read-only and assigned by the
service provider when a resource is created. Not typically intended for end-user display.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.title, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.title, oslc.name, Literal('title')))
    g.add((oslc_sysml_shapes.title, oslc.occurs, oslc['Exactly-one']))
    g.add((oslc_sysml_shapes.title, oslc.propertyDefinition, DCTERMS.title))
    g.add((oslc_sysml_shapes.title, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.title, oslc.valueType, RDF.XMLLiteral))
    g.add((oslc_sysml_shapes.title, DCTERMS.description, Literal("Title of the resource represented as rich text in XHTML content.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.shortTitle, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.shortTitle, oslc.name, Literal('shortTitle')))
    g.add((oslc_sysml_shapes.shortTitle, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_sysml_shapes.shortTitle, oslc.propertyDefinition, oslc.shortTitle))
    g.add((oslc_sysml_shapes.shortTitle, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.shortTitle, oslc.valueType, RDF.XMLLiteral))
    g.add((oslc_sysml_shapes.shortTitle, DCTERMS.description, Literal("{{Short name identifying a resource, often used as an abbreviated identifier for presentation to end-users. SHOULD include only content that is valid inside an XHTML &lt;span&gt; element}}.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.description, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.description, oslc.name, Literal('description')))
    g.add((oslc_sysml_shapes.description, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_sysml_shapes.description, oslc.propertyDefinition, DCTERMS.description))
    g.add((oslc_sysml_shapes.description, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.description, oslc.valueType, RDF.XMLLiteral))
    g.add((oslc_sysml_shapes.description, DCTERMS.description, Literal("Descriptive text about resource represented as rich text in XHTML content.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.source, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.source, oslc.name, Literal('source')))
    g.add((oslc_sysml_shapes.source, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_sysml_shapes.source, oslc.propertyDefinition, DCTERMS.source))
    g.add((oslc_sysml_shapes.source, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.source, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.source, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.source, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.source, DCTERMS.description, Literal("The resource URI a client can perform a get on to obtain the original non-OSLC AM formatted resource that was used to create this resource. The source resource is usually a binary or proprietary format that the service provider can consume and convert into an OSLC AM format. The service may use content negotiation with the Accept header to obtain the desired content type.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.creator, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.creator, oslc.name, Literal('creator')))
    g.add((oslc_sysml_shapes.creator, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.creator, oslc.propertyDefinition, DCTERMS.creator))
    g.add((oslc_sysml_shapes.creator, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.creator, oslc.valueType, oslc.AnyResource))
    g.add((oslc_sysml_shapes.creator, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.creator, oslc.representation, oslc.Either))
    g.add((oslc_sysml_shapes.creator, DCTERMS.description, Literal("Creator or creators of the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.created, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.created, oslc.name, Literal('created')))
    g.add((oslc_sysml_shapes.created, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_sysml_shapes.created, oslc.propertyDefinition, DCTERMS.created))
    g.add((oslc_sysml_shapes.created, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.created, oslc.valueType, XSD.dateTime))
    g.add((oslc_sysml_shapes.created, DCTERMS.description, Literal("Timestamp of resource creation.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.contributor, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.contributor, oslc.name, Literal('contributor')))
    g.add((oslc_sysml_shapes.contributor, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.contributor, oslc.propertyDefinition, DCTERMS.contributor))
    g.add((oslc_sysml_shapes.contributor, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.contributor, oslc.valueType, oslc.AnyResource))
    g.add((oslc_sysml_shapes.contributor, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.contributor, oslc.representation, oslc.Either))
    g.add((oslc_sysml_shapes.contributor, DCTERMS.description, Literal("Contributor or contributors to the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.modified, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.modified, oslc.name, Literal('modified')))
    g.add((oslc_sysml_shapes.modified, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_sysml_shapes.modified, oslc.propertyDefinition, DCTERMS.modified))
    g.add((oslc_sysml_shapes.modified, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.modified, oslc.valueType, XSD.dateTime))
    g.add((oslc_sysml_shapes.modified, DCTERMS.description, Literal("Timestamp of latest resource modification.", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.serviceProvider, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.serviceProvider, oslc.name, Literal('serviceProvider')))
    g.add((oslc_sysml_shapes.serviceProvider, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.serviceProvider, oslc.propertyDefinition, oslc.serviceProvider))
    g.add((oslc_sysml_shapes.serviceProvider, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.serviceProvider, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.serviceProvider, oslc.range, oslc.ServiceProvider))
    g.add((oslc_sysml_shapes.serviceProvider, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.serviceProvider, DCTERMS.description, Literal("""A link to the resource's OSLC Service Provider. There may be cases when the
subject resource is available from a service provider that implements multiple domain
specifications, which could result in multiple values for this property.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.instanceShape, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.instanceShape, oslc.name, Literal('instanceShape')))
    g.add((oslc_sysml_shapes.instanceShape, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_sysml_shapes.instanceShape, oslc.propertyDefinition, oslc.instanceShape))
    g.add((oslc_sysml_shapes.instanceShape, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.instanceShape, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.instanceShape, oslc.range, oslc.ResourceShape))
    g.add((oslc_sysml_shapes.instanceShape, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.instanceShape, DCTERMS.description, Literal("""The URI of a Resource Shape that describes the possible properties, occurrence,
value types, allowed values and labels. This shape information is useful in displaying the subject
resource as well as guiding clients in performing modifications. Instance shapes may be specific
to the authenticated user associated with the request that retrieved the resource, the current
state of the resource and other factors and thus should not be cached.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.derives, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.derives, oslc.name, Literal('derives')))
    g.add((oslc_sysml_shapes.derives, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.derives, oslc.propertyDefinition, jazz_am.derives))
    g.add((oslc_sysml_shapes.derives, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.derives, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.derives, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.derives, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.derives, DCTERMS.description, Literal("""The resource that derives from another resource originated from or is
significantly influenced by the referenced resource. For example a model element derives from a
requirement.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.elaborates, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.elaborates, oslc.name, Literal('elaborates')))
    g.add((oslc_sysml_shapes.elaborates, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.elaborates, oslc.propertyDefinition, jazz_am.elaborates))
    g.add((oslc_sysml_shapes.elaborates, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.elaborates, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.elaborates, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.elaborates, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.elaborates, DCTERMS.description, Literal("""This resource elaborates the referenced resource.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.refine, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.refine, oslc.name, Literal('refine')))
    g.add((oslc_sysml_shapes.refine, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.refine, oslc.propertyDefinition, jazz_am.refine))
    g.add((oslc_sysml_shapes.refine, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.refine, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.refine, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.refine, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.refine, DCTERMS.description, Literal("""The target is a refinement of the source. (e.g. a use case scenario
might be a refinement of a textual requirement that describes the interaction).""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.external, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.external, oslc.name, Literal('external')))
    g.add((oslc_sysml_shapes.external, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.external, oslc.propertyDefinition, jazz_am.external))
    g.add((oslc_sysml_shapes.external, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.external, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.external, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.external, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.external, DCTERMS.description, Literal("""A generic link from a resource to an external web page.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.satisfy, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.satisfy, oslc.name, Literal('satisfy')))
    g.add((oslc_sysml_shapes.satisfy, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.satisfy, oslc.propertyDefinition, jazz_am.satisfy))
    g.add((oslc_sysml_shapes.satisfy, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.satisfy, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.satisfy, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.satisfy, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.satisfy, DCTERMS.description, Literal("""The model element satisfies the requirement (e.g. The use case
satisfies a functional requirement).""", datatype=RDF.XMLLiteral)))

    g.add((oslc_sysml_shapes.trace, RDF.type, oslc.Property))
    g.add((oslc_sysml_shapes.trace, oslc.name, Literal('trace')))
    g.add((oslc_sysml_shapes.trace, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_sysml_shapes.trace, oslc.propertyDefinition, jazz_am.trace))
    g.add((oslc_sysml_shapes.trace, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_sysml_shapes.trace, oslc.valueType, oslc.Resource))
    g.add((oslc_sysml_shapes.trace, oslc.range, oslc.Any))
    g.add((oslc_sysml_shapes.trace, oslc.representation, oslc.Reference))
    g.add((oslc_sysml_shapes.trace, DCTERMS.description, Literal("""The model element has a trace to the requirement (e.g. An attribute
or its value are traced to a requirement).""", datatype=RDF.XMLLiteral)))


g.serialize(destination=f'../{shapes_file}')

if genOASIS:  # add the copywrite header
    with open('../sysml-shapes.ttl','r') as f:
        with open('../temp.ttl','w') as f2: 
            f2.write(copyright)
            f2.write(f.read())
    os.remove('../sysml-shapes.ttl')
    os.rename('../temp.ttl','../sysml-shapes.ttl')

### CELL 7: markdown

## Get SysML v2 classes
A notebook to get a list of the SysML v2 classes and generate the vocabToShape div sections needed in sysml-shapes.html.



### CELL 8: code

# Read and parse the sysml-vocab.ttl file
from rdflib import Graph, URIRef, Literal, Namespace, RDF

# some useful RDF namespaces
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
DCTERMS = Namespace('http://purl.org/dc/terms/')
oslc = Namespace('http://open-services.net/ns/core#')
oslc_am = Namespace('http://open-services.net/ns/am#')

g = Graph()
g.parse('../SysML-vocab.ttl')


### CELL 9: code

# get a list of the classes and create the dev elements needed for shapeToSpec
classes = g.subjects(rdf.type, rdfs.Class)

# and now create the shapeToSpec div for each class
for c in classes:
    name = str(c)
    name = name[name.index('#')+1:]
    print(
f"""

<div
        title="Constraints for {name}"
        data-include="./SysML-shapes.ttl#{name}Shape"
        data-oninclude="shapeToSpec"
        data-include-sync="true"
        data-include-replace="true"
        data-include-format="html"
      ></div>
"""        
    )

### CELL 10: markdown

# Generate OSLC KerML vocab

### CELL 11: code

# create the KerML vocabulary graph, initially empty

oslc_kerml = Namespace('https://www.omg.org/spec/kerml/vocabulary#')

g = Graph()
g.bind('oslc_kerml', oslc_kerml)
g.bind('oslc_am', oslc_am)

# add the vocabulary ontology
o = URIRef(oslc_kerml)
g.add((o, RDF.type, OWL.Ontology))
g.add((o, RDFS.label, Literal("OSLC KerML Vocabulary")))
g.add((o, DCTERMS.description, Literal("All vocabulary URIs defined in the OSLC KerML namespace.", datatype=RDF.XMLLiteral)))
g.add((o, DCTERMS.issued, Literal("2025-02-01", datatype=XSD.date)))
g.add((o, DCTERMS.license, URIRef('')))
g.add((o, DCTERMS.publisher,  URIRef('https://www.omg.org')))
g.add((o, DCTERMS.title, Literal("OSLC KerML Vocabulary")))
g.add((o, vann.preferredNamespacePrefix, Literal("oslc_kerml")))
g.add((o, DCTERMS.hasVersion, Literal("V2")))
g.add((o, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/KerML')))
g.add((o, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/KerML-vocab.ttl')))

# load the KerML.ecore model
rset = ResourceSet()
resource = rset.get_resource(URI('/Users/jamsden/Developer/SysML-v2-Pilot-Implementation/org.omg.sysml/model/KerML.ecore'))
mm_root = resource.contents[0]
rset.metamodel_registry[mm_root.nsURI] = mm_root
# At this point, the .ecore is loaded in the 'rset' as a metamodel


for c in mm_root.eClassifiers:
    # Generate the classes
    if isinstance(c, EClass):
        g.add((oslc_kerml.term(c.name), RDF.type, RDFS.Class))
        if c.name=='Element':
            g.add((oslc_kerml.term(c.name), RDFS.subClassOf, oslc_am.Resource))  # only Element
        if c.eSuperTypes is not None and len(c.eSuperTypes) >= 1:
            for super in c.eSuperTypes:
                g.add((oslc_kerml.term(c.name), RDFS.subClassOf, oslc_kerml.term(super.name)))
        g.add((oslc_kerml.term(c.name), RDFS.label, Literal(c.name)))
        g.add((oslc_kerml.term(c.name), RDFS.comment, Literal(comment(c))))
        g.add((oslc_kerml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_kerml)))

        # generate the properties
        for a in c.eStructuralFeatures:
            name = a.name  # use the class name as a prefix to the attribute name to ensure they are unique
            s = oslc_kerml.term(name)
            g.add((s, RDF.type, RDF.Property))
            g.add((s, RDFS.label, Literal(name)))
            pcomment = g.value(s, RDFS.comment)
            if pcomment is not None:
                # This is a property with multiple domains
                # Concatenate the comment for each domain class into a single comment
                pcomment = pcomment + '\n' + c.name+': '+comment(a)
                g.remove((s, RDFS.comment, None))
                g.add((s, RDFS.comment, Literal(pcomment)))
            else:
                g.add((s, RDFS.comment, Literal(c.name+': '+comment(a))))
            g.add((s, RDFS.isDefinedBy, URIRef(oslc_kerml)))
    if isinstance(c, EEnum):
        g.add((oslc_kerml.term(c.name), RDF.type, RDFS.Class))
        g.add((oslc_kerml.term(c.name), RDFS.label, Literal(c.name)))
        g.add((oslc_kerml.term(c.name), RDFS.comment, Literal(comment(c))))
        g.add((oslc_kerml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_kerml)))

        # generate the enumeration literals
        for a in c.eLiterals:
            name = a.name  # don't use the class name as a prefix to the attribute name to ensure they are unique
            s = oslc_kerml.term(name)
            g.add((s, RDF.type, oslc_kerml.term(c.name)))
            g.add((s, RDFS.label, Literal(name)))
            g.add((s, RDFS.comment, Literal(comment(a))))
            g.add((s, RDFS.isDefinedBy, URIRef(oslc_kerml)))
        
g.serialize(destination='../KerML-vocab.ttl')



### CELL 12: code

# Generate KerML Constraints

    

# create the SysML constraints graph, initially empty
oslc_kerml_shapes = Namespace('https://www.omg.org/spec/kerml/20250201/shapes#')
jazz_am = Namespace('http://jazz.net/ns/dm/linktypes#')

g = Graph()
g.bind('oslc_kerml', oslc_kerml)
g.bind('oslc_am', oslc_am)
g.bind('oslc', oslc)
g.bind('', oslc_kerml_shapes)
g.bind('jazz_am', jazz_am)

s = URIRef(oslc_kerml_shapes)
g.add((s, RDF.type, oslc.ResourceShapeConstraints))
g.add((s, RDFS.label, Literal("OSLC  Kernel Modeling Language (KerML) Constraints")))
g.add((s, DCTERMS.dateCopyrighted, Literal("2012-2024")))
g.add((s, DCTERMS.description, Literal("<p>Constraints on vocabulary terms defined in the OSLC Kernel Modeling Language (KerML) namespace.</p>", datatype=RDF.XMLLiteral)))
g.add((s, DCTERMS.publisher,  URIRef('https://www.omg.org')))
g.add((s, DCTERMS.title, Literal("OSLC Kernel Modeling Language (SysML) Version 2.0 Constraints")))
g.add((s, DCTERMS.hasVersion, Literal("V2")))
g.add((s, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/KerML')))
g.add((s, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/KerML-vocab.ttl')))
g.add((s, DCTERMS.license, URIRef('')))

for c in mm_root.eClassifiers:
    # Generate the ResourceShape
    if isinstance(c, EClass):
        shape = oslc_kerml_shapes.term(c.name+'Shape')
        g.add((shape, RDF.type, oslc.ResourceShape))  # only Element
        g.add((shape, DCTERMS.title, Literal(c.name+'Shape', datatype=RDF.XMLLiteral)))
        g.add((shape, DCTERMS.description, Literal(comment(c,strip=False),datatype=RDF.XMLLiteral)))
        g.add((shape, oslc.describes, URIRef(oslc_kerml.term(c.name))))

        # add all the properties inherited from all superclasses up to Element
        addSuperclassProperties(c, shape, g, oslc_kerml, oslc_kerml_shapes)
        addClassProperties(c, shape, g, oslc_kerml, oslc_kerml_shapes)

        # add the inherited oslc_am:Resource properties
        g.add((shape, oslc.property, oslc_kerml_shapes.type))
        g.add((shape, oslc.property, oslc_kerml_shapes.dctype))
        g.add((shape, oslc.property, oslc_kerml_shapes.identifier))
        g.add((shape, oslc.property, oslc_kerml_shapes.title))
        g.add((shape, oslc.property, oslc_kerml_shapes.shortTitle))
        g.add((shape, oslc.property, oslc_kerml_shapes.description))
        g.add((shape, oslc.property, oslc_kerml_shapes.source))
        g.add((shape, oslc.property, oslc_kerml_shapes.creator))
        g.add((shape, oslc.property, oslc_kerml_shapes.created))
        g.add((shape, oslc.property, oslc_kerml_shapes.contributor))
        g.add((shape, oslc.property, oslc_kerml_shapes.modified))
        g.add((shape, oslc.property, oslc_kerml_shapes.serviceProvider))
        g.add((shape, oslc.property, oslc_kerml_shapes.instanceShape))
        g.add((shape, oslc.property, oslc_kerml_shapes.derives))
        g.add((shape, oslc.property, oslc_kerml_shapes.elaborates))
        g.add((shape, oslc.property, oslc_kerml_shapes.refine))
        g.add((shape, oslc.property, oslc_kerml_shapes.external))
        g.add((shape, oslc.property, oslc_kerml_shapes.satisfy))
        g.add((shape, oslc.property, oslc_kerml_shapes.trace))
        
    # and create the oslc_am:Resource inherited oslc:Property items
    g.add((oslc_kerml_shapes.type, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.type, oslc.name, Literal('type')))
    g.add((oslc_kerml_shapes.type, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.type, oslc.propertyDefinition, RDF.type))
    g.add((oslc_kerml_shapes.type, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.type, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.type, oslc.range, RDFS.Class))
    g.add((oslc_kerml_shapes.type, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.type, DCTERMS.description, Literal("The resource type URIs.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.dctype, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.dctype, oslc.name, Literal('dctype')))
    g.add((oslc_kerml_shapes.dctype, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.dctype, oslc.propertyDefinition, DCTERMS.type))
    g.add((oslc_kerml_shapes.dctype, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.dctype, oslc.valueType, XSD.string))
    g.add((oslc_kerml_shapes.dctype, DCTERMS.description, Literal("A short string representation for the type, for example ‘Car’.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.identifier, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.identifier, oslc.name, Literal('identifier')))
    g.add((oslc_kerml_shapes.identifier, oslc.occurs, oslc['Exactly-one']))
    g.add((oslc_kerml_shapes.identifier, oslc.propertyDefinition, DCTERMS.identifier))
    g.add((oslc_kerml_shapes.identifier, oslc.readOnly, Literal('true',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.identifier, oslc.valueType, XSD.string))
    g.add((oslc_kerml_shapes.identifier, DCTERMS.description, Literal("""A unique identifier for a resource. Typically read-only and assigned by the
service provider when a resource is created. Not typically intended for end-user display.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.title, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.title, oslc.name, Literal('title')))
    g.add((oslc_kerml_shapes.title, oslc.occurs, oslc['Exactly-one']))
    g.add((oslc_kerml_shapes.title, oslc.propertyDefinition, DCTERMS.title))
    g.add((oslc_kerml_shapes.title, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.title, oslc.valueType, RDF.XMLLiteral))
    g.add((oslc_kerml_shapes.title, DCTERMS.description, Literal("Title of the resource represented as rich text in XHTML content.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.shortTitle, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.shortTitle, oslc.name, Literal('shortTitle')))
    g.add((oslc_kerml_shapes.shortTitle, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_kerml_shapes.shortTitle, oslc.propertyDefinition, oslc.shortTitle))
    g.add((oslc_kerml_shapes.shortTitle, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.shortTitle, oslc.valueType, RDF.XMLLiteral))
    g.add((oslc_kerml_shapes.shortTitle, DCTERMS.description, Literal("{{Short name identifying a resource, often used as an abbreviated identifier for presentation to end-users. SHOULD include only content that is valid inside an XHTML &lt;span&gt; element}}.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.description, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.description, oslc.name, Literal('description')))
    g.add((oslc_kerml_shapes.description, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_kerml_shapes.description, oslc.propertyDefinition, DCTERMS.description))
    g.add((oslc_kerml_shapes.description, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.description, oslc.valueType, RDF.XMLLiteral))
    g.add((oslc_kerml_shapes.description, DCTERMS.description, Literal("Descriptive text about resource represented as rich text in XHTML content.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.source, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.source, oslc.name, Literal('source')))
    g.add((oslc_kerml_shapes.source, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_kerml_shapes.source, oslc.propertyDefinition, DCTERMS.source))
    g.add((oslc_kerml_shapes.source, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.source, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.source, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.source, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.source, DCTERMS.description, Literal("The resource URI a client can perform a get on to obtain the original non-OSLC AM formatted resource that was used to create this resource. The source resource is usually a binary or proprietary format that the service provider can consume and convert into an OSLC AM format. The service may use content negotiation with the Accept header to obtain the desired content type.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.creator, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.creator, oslc.name, Literal('creator')))
    g.add((oslc_kerml_shapes.creator, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.creator, oslc.propertyDefinition, DCTERMS.creator))
    g.add((oslc_kerml_shapes.creator, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.creator, oslc.valueType, oslc.AnyResource))
    g.add((oslc_kerml_shapes.creator, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.creator, oslc.representation, oslc.Either))
    g.add((oslc_kerml_shapes.creator, DCTERMS.description, Literal("Creator or creators of the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.created, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.created, oslc.name, Literal('created')))
    g.add((oslc_kerml_shapes.created, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_kerml_shapes.created, oslc.propertyDefinition, DCTERMS.created))
    g.add((oslc_kerml_shapes.created, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.created, oslc.valueType, XSD.dateTime))
    g.add((oslc_kerml_shapes.created, DCTERMS.description, Literal("Timestamp of resource creation.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.contributor, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.contributor, oslc.name, Literal('contributor')))
    g.add((oslc_kerml_shapes.contributor, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.contributor, oslc.propertyDefinition, DCTERMS.contributor))
    g.add((oslc_kerml_shapes.contributor, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.contributor, oslc.valueType, oslc.AnyResource))
    g.add((oslc_kerml_shapes.contributor, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.contributor, oslc.representation, oslc.Either))
    g.add((oslc_kerml_shapes.contributor, DCTERMS.description, Literal("Contributor or contributors to the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.modified, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.modified, oslc.name, Literal('modified')))
    g.add((oslc_kerml_shapes.modified, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_kerml_shapes.modified, oslc.propertyDefinition, DCTERMS.modified))
    g.add((oslc_kerml_shapes.modified, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.modified, oslc.valueType, XSD.dateTime))
    g.add((oslc_kerml_shapes.modified, DCTERMS.description, Literal("Timestamp of latest resource modification.", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.serviceProvider, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.serviceProvider, oslc.name, Literal('serviceProvider')))
    g.add((oslc_kerml_shapes.serviceProvider, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.serviceProvider, oslc.propertyDefinition, oslc.serviceProvider))
    g.add((oslc_kerml_shapes.serviceProvider, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.serviceProvider, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.serviceProvider, oslc.range, oslc.ServiceProvider))
    g.add((oslc_kerml_shapes.serviceProvider, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.serviceProvider, DCTERMS.description, Literal("""A link to the resource's OSLC Service Provider. There may be cases when the
subject resource is available from a service provider that implements multiple domain
specifications, which could result in multiple values for this property.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.instanceShape, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.instanceShape, oslc.name, Literal('instanceShape')))
    g.add((oslc_kerml_shapes.instanceShape, oslc.occurs, oslc['Zero-or-one']))
    g.add((oslc_kerml_shapes.instanceShape, oslc.propertyDefinition, oslc.instanceShape))
    g.add((oslc_kerml_shapes.instanceShape, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.instanceShape, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.instanceShape, oslc.range, oslc.ResourceShape))
    g.add((oslc_kerml_shapes.instanceShape, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.instanceShape, DCTERMS.description, Literal("""The URI of a Resource Shape that describes the possible properties, occurrence,
value types, allowed values and labels. This shape information is useful in displaying the subject
resource as well as guiding clients in performing modifications. Instance shapes may be specific
to the authenticated user associated with the request that retrieved the resource, the current
state of the resource and other factors and thus should not be cached.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.derives, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.derives, oslc.name, Literal('derives')))
    g.add((oslc_kerml_shapes.derives, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.derives, oslc.propertyDefinition, jazz_am.derives))
    g.add((oslc_kerml_shapes.derives, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.derives, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.derives, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.derives, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.derives, DCTERMS.description, Literal("""The resource that derives from another resource originated from or is
significantly influenced by the referenced resource. For example a model element derives from a
requirement.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.elaborates, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.elaborates, oslc.name, Literal('elaborates')))
    g.add((oslc_kerml_shapes.elaborates, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.elaborates, oslc.propertyDefinition, jazz_am.elaborates))
    g.add((oslc_kerml_shapes.elaborates, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.elaborates, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.elaborates, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.elaborates, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.elaborates, DCTERMS.description, Literal("""This resource elaborates the referenced resource.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.refine, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.refine, oslc.name, Literal('refine')))
    g.add((oslc_kerml_shapes.refine, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.refine, oslc.propertyDefinition, jazz_am.refine))
    g.add((oslc_kerml_shapes.refine, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.refine, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.refine, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.refine, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.refine, DCTERMS.description, Literal("""The target is a refinement of the source. (e.g. a use case scenario
might be a refinement of a textual requirement that describes the interaction).""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.external, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.external, oslc.name, Literal('external')))
    g.add((oslc_kerml_shapes.external, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.external, oslc.propertyDefinition, jazz_am.external))
    g.add((oslc_kerml_shapes.external, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.external, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.external, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.external, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.external, DCTERMS.description, Literal("""A generic link from a resource to an external web page.""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.satisfy, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.satisfy, oslc.name, Literal('satisfy')))
    g.add((oslc_kerml_shapes.satisfy, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.satisfy, oslc.propertyDefinition, jazz_am.satisfy))
    g.add((oslc_kerml_shapes.satisfy, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.satisfy, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.satisfy, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.satisfy, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.satisfy, DCTERMS.description, Literal("""The model element satisfies the requirement (e.g. The use case
satisfies a functional requirement).""", datatype=RDF.XMLLiteral)))

    g.add((oslc_kerml_shapes.trace, RDF.type, oslc.Property))
    g.add((oslc_kerml_shapes.trace, oslc.name, Literal('trace')))
    g.add((oslc_kerml_shapes.trace, oslc.occurs, oslc['Zero-or-many']))
    g.add((oslc_kerml_shapes.trace, oslc.propertyDefinition, jazz_am.trace))
    g.add((oslc_kerml_shapes.trace, oslc.readOnly, Literal('false',datatype=XSD.boolean)))
    g.add((oslc_kerml_shapes.trace, oslc.valueType, oslc.Resource))
    g.add((oslc_kerml_shapes.trace, oslc.range, oslc.Any))
    g.add((oslc_kerml_shapes.trace, oslc.representation, oslc.Reference))
    g.add((oslc_kerml_shapes.trace, DCTERMS.description, Literal("""The model element has a trace to the requirement (e.g. An attribute
or its value are traced to a requirement).""", datatype=RDF.XMLLiteral)))


g.serialize(destination='../KerML-shapes.ttl')



### CELL 13: markdown



## EXACT SOURCE

````json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Generate the SysML Vocabulary Terms\n",
    "\n",
    "Generate the SysML v2 vocabulary from /Users/jamsden/Developer/SysML/SysML-v2-Pilot-Implementation/org.omg.sysml/model/SysML.ecore. This will be the merged KerML and SysML into a single vocabulary with a single namespace.\n",
    "\n",
    "Set genOASIS = True to generate for OASIS, leave false to generate for OMG\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initial imports and local methods\n",
    "from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD, RDFS, OWL, DCTERMS, BNode\n",
    "from pyecore.ecore import EClass, EAttribute, EReference, EString, EObject, EEnum\n",
    "from pyecore.resources import ResourceSet, URI\n",
    "from bs4 import BeautifulSoup\n",
    "import os\n",
    "\n",
    "genOASIS = False  # set to True to generate OASIS SysML instead of OMG: Deprecated, only generate OMG\n",
    "\n",
    "# use the class name as a prefix to the attribute name to ensure they are unique\n",
    "# this should no longer be used, but the method to calculate the qualified name is retained.\n",
    "def qualident(eClass, eAttribute):\n",
    "    return eClass.name[0].lower() + eClass.name[1:] + '_' + eAttribute.name[0].capitalize() + eAttribute.name[1:]  \n",
    "\n",
    "# Get the description of the model element as the first paragraph\n",
    "# with markdown removed if strip is True (rdfs:comment is a string, not an XMLLiteral)\n",
    "def comment(eModelElement, strip=True):\n",
    "    desc = f'{eModelElement.name}.'  # rdfs:comment is required in the vocabulary, this is the default\n",
    "    a = eModelElement.getEAnnotation('http://www.eclipse.org/emf/2002/GenModel')\n",
    "    if a is None: return desc\n",
    "    description = a.details['documentation']\n",
    "    root = BeautifulSoup(str(description))\n",
    "    description = root.find('p') \n",
    "    if strip:\n",
    "        text =  description.get_text() # the first paragraph with the HTML stripped out\n",
    "        if not (text is None or text==''): desc = text\n",
    "    else:\n",
    "        # strip off the <p> and </p>, they are not needed and cause the period to appear to be missing to shapechecker\n",
    "        desc = str(description)[3:-4]  # but include the rest of the markup\n",
    "    if not desc.endswith('.'): desc = desc + '.'\n",
    "    return desc\n",
    "\n",
    "\n",
    "# some useful RDF namespaces\n",
    "vann = Namespace('http://purl.org/vocab/vann/')\n",
    "oslc = Namespace('http://open-services.net/ns/core#')\n",
    "oslc_am = Namespace('http://open-services.net/ns/am#')\n",
    "oslc_sysml = Namespace('https://www.omg.org/spec/sysml/vocabulary#')  # OMG namespace\n",
    "if genOASIS: oslc_sysml = Namespace('http://open-services.net/ns/sysml#')  # OASIS namespace\n",
    "\n",
    "# the OASIS copywrite and license information, not used for OMG \n",
    "copyright = \"\"\"\n",
    "# Copyright 2024 OASIS Open\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#     http://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License.\n",
    "\n",
    "\"\"\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate the SysML OSLC vocabulary file\n",
    "\n",
    "vocab_file = 'SysML-vocab.ttl'\n",
    "if genOASIS: vocab_file = 'sysml-vocab.ttl'\n",
    "\n",
    "# create the SysML vocabulary graph, initially empty\n",
    "g = Graph()\n",
    "g.bind('oslc_sysml', oslc_sysml)\n",
    "g.bind('oslc_am', oslc_am)\n",
    "\n",
    "# add the vocabulary ontology\n",
    "o = URIRef(oslc_sysml)\n",
    "g.add((o, RDF.type, OWL.Ontology))\n",
    "g.add((o, RDFS.label, Literal(\"OSLC SysML v2 Vocabulary\")))\n",
    "g.add((o, DCTERMS.description, Literal(\"All vocabulary URIs defined in the OSLC SysML v2 namespace.\", datatype=RDF.XMLLiteral)))\n",
    "g.add((o, DCTERMS.title, Literal(\"OSLC SysML v2 Vocabulary\")))\n",
    "g.add((o, vann.preferredNamespacePrefix, Literal(\"oslc_sysml\")))\n",
    "if genOASIS:\n",
    "    g.add((o, DCTERMS.dateCopyrighted, Literal(\"2012-2024\")))\n",
    "    g.add((o, DCTERMS.hasVersion, Literal(\"PSD01\")))\n",
    "    g.add((o, DCTERMS.isPartOf, URIRef('https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/os/sysml-spec.html')))\n",
    "    g.add((o, DCTERMS.issued, Literal(\"2024-08-01\", datatype=XSD.date)))\n",
    "    g.add((o, DCTERMS.license, URIRef('http://www.apache.org/licenses/LICENSE-2.0')))\n",
    "    g.add((o, DCTERMS.publisher,  URIRef('https://open-services.net/about/')))\n",
    "    g.add((o, DCTERMS.source, URIRef('https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/os/sysml-vocab.ttl')))\n",
    "else:\n",
    "    g.add((o, DCTERMS.publisher,  URIRef('https://www.omg.org')))\n",
    "    g.add((o, DCTERMS.issued, Literal(\"2025-02-01\", datatype=XSD.date)))\n",
    "    g.add((o, DCTERMS.hasVersion, Literal(\"V2\")))\n",
    "    g.add((o, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/SysML')))\n",
    "    g.add((o, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/SysML-vocab.ttl')))\n",
    "    g.add((o, DCTERMS.license, URIRef('')))\n",
    "\n",
    "# load the SysML.ecore model - this is the merged KerML and SysML metamodel using a single namespace\n",
    "rset = ResourceSet()\n",
    "resource = rset.get_resource(URI('/Users/jamsden/Developer/SysML-v2-Pilot-Implementation/org.omg.sysml/model/sysml_clean.ecore'))\n",
    "mm_root = resource.contents[0]\n",
    "rset.metamodel_registry[mm_root.nsURI] = mm_root\n",
    "# At this point, the .ecore is loaded in the 'rset' as a metamodel\n",
    "\n",
    "\n",
    "for c in mm_root.eClassifiers:\n",
    "    # Generate the classes\n",
    "    if isinstance(c, EClass):\n",
    "        g.add((oslc_sysml.term(c.name), RDF.type, RDFS.Class))\n",
    "        if c.name=='Element':\n",
    "            g.add((oslc_sysml.term(c.name), RDFS.subClassOf, oslc_am.Resource))  # only Element\n",
    "        if c.eSuperTypes is not None and len(c.eSuperTypes) >= 1:\n",
    "            for super in c.eSuperTypes:\n",
    "                g.add((oslc_sysml.term(c.name), RDFS.subClassOf, oslc_sysml.term(super.name)))\n",
    "        g.add((oslc_sysml.term(c.name), RDFS.label, Literal(c.name)))\n",
    "        g.add((oslc_sysml.term(c.name), RDFS.comment, Literal(comment(c))))\n",
    "        g.add((oslc_sysml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_sysml)))\n",
    "\n",
    "        # generate the properties\n",
    "        for a in c.eStructuralFeatures:\n",
    "            name = a.name  # done't use the class name as a prefix to the attribute name to ensure they are unique\n",
    "            s = oslc_sysml.term(name)\n",
    "            g.add((s, RDF.type, RDF.Property))\n",
    "            g.add((s, RDFS.label, Literal(name)))\n",
    "            # does the property already have a comment?\n",
    "            pcomment = g.value(s, RDFS.comment)\n",
    "            if pcomment is not None:\n",
    "                # This is a property with multiple domains\n",
    "                # Concatenate the comment for each domain class into a single comment\n",
    "                pcomment = pcomment + '\\n' + c.name+': '+comment(a)\n",
    "                g.remove((s, RDFS.comment, None))\n",
    "                g.add((s, RDFS.comment, Literal(pcomment)))\n",
    "            else:\n",
    "                g.add((s, RDFS.comment, Literal(c.name+': '+comment(a))))\n",
    "            g.add((s, RDFS.isDefinedBy, URIRef(oslc_sysml)))\n",
    "    if isinstance(c, EEnum):\n",
    "        g.add((oslc_sysml.term(c.name), RDF.type, RDFS.Class))\n",
    "        g.add((oslc_sysml.term(c.name), RDFS.label, Literal(c.name)))\n",
    "        g.add((oslc_sysml.term(c.name), RDFS.comment, Literal(comment(c))))\n",
    "        g.add((oslc_sysml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_sysml)))\n",
    "\n",
    "        # generate the enumeration literals\n",
    "        for a in c.eLiterals:\n",
    "            name = a.name  # don't use the class name as a prefix to the attribute name to ensure they are unique\n",
    "            s = oslc_sysml.term(name)\n",
    "            g.add((s, RDF.type, oslc_sysml.term(c.name)))\n",
    "            g.add((s, RDFS.label, Literal(name)))\n",
    "            g.add((s, RDFS.comment, Literal(comment(a))))\n",
    "            g.add((s, RDFS.isDefinedBy, URIRef(oslc_sysml)))\n",
    "        \n",
    "g.serialize(destination=f'../{vocab_file}')\n",
    "\n",
    "if genOASIS:  # add the copyright for OASIS\n",
    "    with open('../sysml-vocab.ttl','r') as f:\n",
    "        with open('../temp.ttl','w') as f2: \n",
    "            f2.write(copyright)\n",
    "            f2.write(f.read())\n",
    "    os.remove('../sysml-vocab.ttl')\n",
    "    os.rename('../temp.ttl','../sysml-vocab.ttl')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Generate the SysML OSLC constraints\n",
    "Generate the SysML v2 constraints from /Users/jamsden/Developer/SysML/SysML-v2-Pilot-Implementation/org.omg.sysml/model/SysML.ecore. This will be the merged KerML and SysML into a single vocabulary with a single namespace. \n",
    "\n",
    "This depends on the vocabulary that was generated above.\n",
    "\n",
    "The ResourceShape properties also do not need class prefixes because they are added to the classes using blank nodes which makes them unique.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get a list of the properties that are defined in more than one class (ignoring inheritance)\n",
    "# These need to be added as shape properties using blank nodes to ensure they are properly scoped by the class\n",
    "# Iterate over all the EClasses in the model and collect the EAttribute and EReference property names\n",
    "# Then find all the ones that are duplicated\n",
    "import pandas as pd\n",
    "\n",
    "allProperties = []\n",
    "for c in mm_root.eClassifiers:\n",
    "    if isinstance(c, EClass):\n",
    "         for a in c.eStructuralFeatures:\n",
    "              allProperties.append(a.name)\n",
    "allProperties = pd.Series(allProperties)\n",
    "multiDefProps = set(allProperties[allProperties.duplicated()]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate the SysML OSLC constraints\n",
    "from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD, RDFS, OWL, DCTERMS\n",
    "from pyecore.ecore import EClassifier, EClass, EAttribute, EReference, EString, EObject, EEnum\n",
    "from pyecore.resources import ResourceSet, URI\n",
    "from bs4 import BeautifulSoup\n",
    "import os\n",
    "\n",
    "shapes_file = 'SysML-shapes.ttl'\n",
    "if genOASIS: shapes_file = 'sysml-shapes.ttl'\n",
    "\n",
    "def multiplicity(eAttribute):\n",
    "    lower = eAttribute.lowerBound\n",
    "    upper = eAttribute.upperBound\n",
    "    if lower==1 and upper==1: return oslc['Exactly-one']\n",
    "    if lower==1 and upper !=0: return oslc['One-or-many']\n",
    "    if lower==0 and upper==1: return oslc['Zero-or-one']\n",
    "    if lower==0 and upper !=0: return oslc['Zero-or-many']\n",
    "\n",
    "def valueType(a):\n",
    "    match a.eType.name:\n",
    "        case 'Boolean': return XSD.boolean\n",
    "        case 'String': return XSD.string\n",
    "        case 'Real': return XSD.float\n",
    "        case 'Integer': return XSD.integer\n",
    "        case _: return oslc_sysml.term(a.eType.name)\n",
    "\n",
    "def propertyAlreadyAdded(propname, eclass, shape, graph):\n",
    "    # is the property already ready in this shape\n",
    "    # Note: the property could be a global property definition or in a blank node\n",
    "    props = list(graph.objects(shape, oslc.property))\n",
    "    props = list(map(lambda s: graph.value(s, oslc.name).value, props))\n",
    "    return propname in props\n",
    "\n",
    "\n",
    "def addClassProperties(eclass, shape, graph, vocab_namespace, shape_namespace):\n",
    "    # generate the properties specific to this ResourceShape\n",
    "    for a in eclass.eStructuralFeatures:\n",
    "        name = a.name\n",
    "        cls = vocab_namespace.term(eclass.name)\n",
    "        prop = vocab_namespace.term(name)\n",
    "        # does the uninherited property appear in more than one class?\n",
    "        # if it does, then add the Property constraint using a blank node for the class\n",
    "        # if not, then define the property so it can be reused where it is inherited\n",
    "        propval = shape_namespace.term(name)\n",
    "        if propertyAlreadyAdded(name, eclass, shape, graph): return\n",
    "        if name in multiDefProps:\n",
    "            propval = BNode()\n",
    "        graph.add((shape, oslc.property, propval))\n",
    "\n",
    "        # and create the oslc:Property elements defined by this EClass\n",
    "        graph.add((propval, RDF.type, oslc.Property))\n",
    "        graph.add((propval, oslc.name, Literal(name)))\n",
    "        graph.add((propval, oslc.occurs, multiplicity(a)))\n",
    "        graph.add((propval, oslc.propertyDefinition, URIRef(prop)))\n",
    "        graph.add((propval, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "        if isinstance(a, EReference):\n",
    "            graph.add((propval, oslc.valueType, oslc.Resource))\n",
    "            graph.add((propval, oslc.range, vocab_namespace.term(a.eType.name)))\n",
    "            graph.add((propval, oslc.representation, oslc.Either))\n",
    "        graph.add((propval, DCTERMS.description, Literal(comment(a,strip=False), datatype=RDF.XMLLiteral)))\n",
    "        # is the property a redefinition? If so, remove the inherited property\n",
    "        # Commented out because we decide that 1) redefined properties are inherited in SysML v2\n",
    "        # and this is the behavior of the Services REST API JSON representation\n",
    "        \"\"\"\n",
    "        redefinitions = a.getEAnnotation('redefines')\n",
    "        if redefinitions is not None:\n",
    "            reference = redefinitions.references[0].name\n",
    "            prop = shape_namespace.term(reference)\n",
    "            graph.remove((shape, oslc.property, prop))\n",
    "            # the property could have been added with a blank node\n",
    "        \"\"\"\n",
    "\n",
    "\n",
    "def addSuperclassProperties(eclass, shape, graph, vocab_namespace, shape_namespace):\n",
    "    if eclass.eSuperTypes is not None and len(eclass.eSuperTypes) >= 1:\n",
    "        for super in eclass.eSuperTypes:\n",
    "            # recursively add the properties for the superclasses up the hierarchy\n",
    "            addSuperclassProperties(super, shape, graph, vocab_namespace, shape_namespace)\n",
    "            # and add the properties for this superclass\n",
    "            addClassProperties(super, shape, graph, vocab_namespace, shape_namespace)\n",
    "\n",
    "    # some useful RDF namespaces\n",
    "vann = Namespace('http://purl.org/vocab/vann/')\n",
    "oslc = Namespace('http://open-services.net/ns/core#')\n",
    "oslc_am = Namespace('http://open-services.net/ns/am#')\n",
    "oslc_sysml_shapes = Namespace('https://www.omg.org/spec/SysML/20250201/shapes/')  # OMG namespace versioned for constraints\n",
    "if genOASIS: oslc_sysml_shapes = Namespace('http://open-services.net/ns/sysml/shapes/20250201#')  # OASIS namespace\n",
    "\n",
    "jazz_am = Namespace('http://jazz.net/ns/dm/linktypes#')\n",
    "\n",
    "# create the SysML constraints graph, initially empty\n",
    "g = Graph()\n",
    "g.bind('oslc_sysml', oslc_sysml)\n",
    "g.bind('oslc_am', oslc_am)\n",
    "g.bind('oslc', oslc)\n",
    "g.bind('oslc_sysml_shapes', oslc_sysml_shapes)\n",
    "g.bind('jazz_am', jazz_am)\n",
    "\n",
    "s = URIRef(oslc_sysml_shapes)\n",
    "g.add((s, RDF.type, oslc.ResourceShapeConstraints))\n",
    "g.add((s, RDFS.label, Literal(\"OSLC  System Modeling Language (SysML) Constraints\")))\n",
    "g.add((s, DCTERMS.description, Literal(\"<p>Constraints on vocabulary terms defined in the OSLC System Modeling Language (SysML) namespace.</p>\", datatype=RDF.XMLLiteral)))\n",
    "g.add((s, DCTERMS.title, Literal(\"OSLC System Modeling Language (SysML) Version 2.0 Constraints\")))\n",
    "\n",
    "if genOASIS:\n",
    "    g.add((s, DCTERMS.dateCopyrighted, Literal(\"2012-2024\")))\n",
    "    g.add((s, DCTERMS.issued, Literal(\"2025-02-01\", datatype=XSD.date)))\n",
    "    g.add((s, DCTERMS.hasVersion, Literal(\"PSD01\")))\n",
    "    g.add((s, DCTERMS.isPartOf, URIRef(\"https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/psd01/sysml-spec.html\")))\n",
    "    g.add((s, DCTERMS.license, URIRef(\"http://www.apache.org/licenses/LICENSE-2.0\")))\n",
    "    g.add((s, DCTERMS.source, URIRef(\"https://docs.oasis-open-projects.org/oslc-op/sysml/v2.0/psd01/sysml-shapes.ttl\")))\n",
    "else:\n",
    "    g.add((s, DCTERMS.publisher, URIRef(\"https://www.omg.org\")))\n",
    "    g.add((s, DCTERMS.issued, Literal(\"2025-02-01\", datatype=XSD.date)))\n",
    "    g.add((s, DCTERMS.hasVersion, Literal(\"V2\")))\n",
    "    g.add((s, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/SysML')))\n",
    "    g.add((s, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/SysML-vocab.ttl')))\n",
    "    g.add((s, DCTERMS.license, URIRef('')))\n",
    "\n",
    "# load the SysML.ecore model - this is the merged KerML and SysML metamodel using a single namespace\n",
    "rset = ResourceSet()\n",
    "resource = rset.get_resource(URI('/Users/jamsden/Developer/SysML-v2-Pilot-Implementation/org.omg.sysml/model/sysml_clean.ecore'))\n",
    "mm_root = resource.contents[0]\n",
    "rset.metamodel_registry[mm_root.nsURI] = mm_root\n",
    "# At this point, the .ecore is loaded in the 'rset' as a metamodel\n",
    "\n",
    "\n",
    "for c in mm_root.eClassifiers:\n",
    "    # Generate the ResourceShape\n",
    "    if isinstance(c, EClass):\n",
    "        shape = oslc_sysml_shapes.term(c.name+'Shape')\n",
    "        g.add((shape, RDF.type, oslc.ResourceShape))  # only Element\n",
    "        g.add((shape, DCTERMS.title, Literal(c.name+'Shape', datatype=RDF.XMLLiteral)))\n",
    "        g.add((shape, DCTERMS.description, Literal(comment(c,strip=False),datatype=RDF.XMLLiteral)))\n",
    "        g.add((shape, oslc.describes, URIRef(oslc_sysml.term(c.name))))\n",
    "\n",
    "        # add all the properties inherited from all superclasses up to Element\n",
    "        addSuperclassProperties(c, shape, g, oslc_sysml, oslc_sysml_shapes)\n",
    "        addClassProperties(c, shape, g, oslc_sysml, oslc_sysml_shapes)\n",
    "\n",
    "        # add the inherited oslc_am:Resource properties\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.type))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.dctype))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.identifier))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.title))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.shortTitle))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.description))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.source))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.creator))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.created))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.contributor))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.modified))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.serviceProvider))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.instanceShape))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.derives))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.elaborates))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.refine))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.external))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.satisfy))\n",
    "        g.add((shape, oslc.property, oslc_sysml_shapes.trace))\n",
    "        \n",
    "    # and create the oslc_am:Resource inherited oslc:Property items\n",
    "    g.add((oslc_sysml_shapes.type, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.type, oslc.name, Literal('type')))\n",
    "    g.add((oslc_sysml_shapes.type, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.type, oslc.propertyDefinition, RDF.type))\n",
    "    g.add((oslc_sysml_shapes.type, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.type, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.type, oslc.range, RDFS.Class))\n",
    "    g.add((oslc_sysml_shapes.type, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.type, DCTERMS.description, Literal(\"The resource type URIs.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.dctype, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.dctype, oslc.name, Literal('dctype')))\n",
    "    g.add((oslc_sysml_shapes.dctype, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.dctype, oslc.propertyDefinition, DCTERMS.type))\n",
    "    g.add((oslc_sysml_shapes.dctype, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.dctype, oslc.valueType, XSD.string))\n",
    "    g.add((oslc_sysml_shapes.dctype, DCTERMS.description, Literal(\"A short string representation for the type, for example ‘Car’.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.identifier, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.identifier, oslc.name, Literal('identifier')))\n",
    "    g.add((oslc_sysml_shapes.identifier, oslc.occurs, oslc['Exactly-one']))\n",
    "    g.add((oslc_sysml_shapes.identifier, oslc.propertyDefinition, DCTERMS.identifier))\n",
    "    g.add((oslc_sysml_shapes.identifier, oslc.readOnly, Literal('true',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.identifier, oslc.valueType, XSD.string))\n",
    "    g.add((oslc_sysml_shapes.identifier, DCTERMS.description, Literal(\"\"\"A unique identifier for a resource. Typically read-only and assigned by the\n",
    "service provider when a resource is created. Not typically intended for end-user display.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.title, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.title, oslc.name, Literal('title')))\n",
    "    g.add((oslc_sysml_shapes.title, oslc.occurs, oslc['Exactly-one']))\n",
    "    g.add((oslc_sysml_shapes.title, oslc.propertyDefinition, DCTERMS.title))\n",
    "    g.add((oslc_sysml_shapes.title, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.title, oslc.valueType, RDF.XMLLiteral))\n",
    "    g.add((oslc_sysml_shapes.title, DCTERMS.description, Literal(\"Title of the resource represented as rich text in XHTML content.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.shortTitle, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.shortTitle, oslc.name, Literal('shortTitle')))\n",
    "    g.add((oslc_sysml_shapes.shortTitle, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_sysml_shapes.shortTitle, oslc.propertyDefinition, oslc.shortTitle))\n",
    "    g.add((oslc_sysml_shapes.shortTitle, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.shortTitle, oslc.valueType, RDF.XMLLiteral))\n",
    "    g.add((oslc_sysml_shapes.shortTitle, DCTERMS.description, Literal(\"{{Short name identifying a resource, often used as an abbreviated identifier for presentation to end-users. SHOULD include only content that is valid inside an XHTML &lt;span&gt; element}}.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.description, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.description, oslc.name, Literal('description')))\n",
    "    g.add((oslc_sysml_shapes.description, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_sysml_shapes.description, oslc.propertyDefinition, DCTERMS.description))\n",
    "    g.add((oslc_sysml_shapes.description, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.description, oslc.valueType, RDF.XMLLiteral))\n",
    "    g.add((oslc_sysml_shapes.description, DCTERMS.description, Literal(\"Descriptive text about resource represented as rich text in XHTML content.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.source, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.source, oslc.name, Literal('source')))\n",
    "    g.add((oslc_sysml_shapes.source, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_sysml_shapes.source, oslc.propertyDefinition, DCTERMS.source))\n",
    "    g.add((oslc_sysml_shapes.source, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.source, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.source, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.source, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.source, DCTERMS.description, Literal(\"The resource URI a client can perform a get on to obtain the original non-OSLC AM formatted resource that was used to create this resource. The source resource is usually a binary or proprietary format that the service provider can consume and convert into an OSLC AM format. The service may use content negotiation with the Accept header to obtain the desired content type.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.creator, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.creator, oslc.name, Literal('creator')))\n",
    "    g.add((oslc_sysml_shapes.creator, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.creator, oslc.propertyDefinition, DCTERMS.creator))\n",
    "    g.add((oslc_sysml_shapes.creator, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.creator, oslc.valueType, oslc.AnyResource))\n",
    "    g.add((oslc_sysml_shapes.creator, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.creator, oslc.representation, oslc.Either))\n",
    "    g.add((oslc_sysml_shapes.creator, DCTERMS.description, Literal(\"Creator or creators of the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.created, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.created, oslc.name, Literal('created')))\n",
    "    g.add((oslc_sysml_shapes.created, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_sysml_shapes.created, oslc.propertyDefinition, DCTERMS.created))\n",
    "    g.add((oslc_sysml_shapes.created, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.created, oslc.valueType, XSD.dateTime))\n",
    "    g.add((oslc_sysml_shapes.created, DCTERMS.description, Literal(\"Timestamp of resource creation.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.contributor, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.contributor, oslc.name, Literal('contributor')))\n",
    "    g.add((oslc_sysml_shapes.contributor, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.contributor, oslc.propertyDefinition, DCTERMS.contributor))\n",
    "    g.add((oslc_sysml_shapes.contributor, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.contributor, oslc.valueType, oslc.AnyResource))\n",
    "    g.add((oslc_sysml_shapes.contributor, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.contributor, oslc.representation, oslc.Either))\n",
    "    g.add((oslc_sysml_shapes.contributor, DCTERMS.description, Literal(\"Contributor or contributors to the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.modified, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.modified, oslc.name, Literal('modified')))\n",
    "    g.add((oslc_sysml_shapes.modified, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_sysml_shapes.modified, oslc.propertyDefinition, DCTERMS.modified))\n",
    "    g.add((oslc_sysml_shapes.modified, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.modified, oslc.valueType, XSD.dateTime))\n",
    "    g.add((oslc_sysml_shapes.modified, DCTERMS.description, Literal(\"Timestamp of latest resource modification.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, oslc.name, Literal('serviceProvider')))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, oslc.propertyDefinition, oslc.serviceProvider))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, oslc.range, oslc.ServiceProvider))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.serviceProvider, DCTERMS.description, Literal(\"\"\"A link to the resource's OSLC Service Provider. There may be cases when the\n",
    "subject resource is available from a service provider that implements multiple domain\n",
    "specifications, which could result in multiple values for this property.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.instanceShape, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, oslc.name, Literal('instanceShape')))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, oslc.propertyDefinition, oslc.instanceShape))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, oslc.range, oslc.ResourceShape))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.instanceShape, DCTERMS.description, Literal(\"\"\"The URI of a Resource Shape that describes the possible properties, occurrence,\n",
    "value types, allowed values and labels. This shape information is useful in displaying the subject\n",
    "resource as well as guiding clients in performing modifications. Instance shapes may be specific\n",
    "to the authenticated user associated with the request that retrieved the resource, the current\n",
    "state of the resource and other factors and thus should not be cached.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.derives, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.derives, oslc.name, Literal('derives')))\n",
    "    g.add((oslc_sysml_shapes.derives, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.derives, oslc.propertyDefinition, jazz_am.derives))\n",
    "    g.add((oslc_sysml_shapes.derives, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.derives, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.derives, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.derives, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.derives, DCTERMS.description, Literal(\"\"\"The resource that derives from another resource originated from or is\n",
    "significantly influenced by the referenced resource. For example a model element derives from a\n",
    "requirement.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.elaborates, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.elaborates, oslc.name, Literal('elaborates')))\n",
    "    g.add((oslc_sysml_shapes.elaborates, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.elaborates, oslc.propertyDefinition, jazz_am.elaborates))\n",
    "    g.add((oslc_sysml_shapes.elaborates, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.elaborates, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.elaborates, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.elaborates, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.elaborates, DCTERMS.description, Literal(\"\"\"This resource elaborates the referenced resource.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.refine, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.refine, oslc.name, Literal('refine')))\n",
    "    g.add((oslc_sysml_shapes.refine, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.refine, oslc.propertyDefinition, jazz_am.refine))\n",
    "    g.add((oslc_sysml_shapes.refine, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.refine, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.refine, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.refine, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.refine, DCTERMS.description, Literal(\"\"\"The target is a refinement of the source. (e.g. a use case scenario\n",
    "might be a refinement of a textual requirement that describes the interaction).\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.external, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.external, oslc.name, Literal('external')))\n",
    "    g.add((oslc_sysml_shapes.external, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.external, oslc.propertyDefinition, jazz_am.external))\n",
    "    g.add((oslc_sysml_shapes.external, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.external, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.external, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.external, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.external, DCTERMS.description, Literal(\"\"\"A generic link from a resource to an external web page.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.satisfy, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.satisfy, oslc.name, Literal('satisfy')))\n",
    "    g.add((oslc_sysml_shapes.satisfy, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.satisfy, oslc.propertyDefinition, jazz_am.satisfy))\n",
    "    g.add((oslc_sysml_shapes.satisfy, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.satisfy, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.satisfy, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.satisfy, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.satisfy, DCTERMS.description, Literal(\"\"\"The model element satisfies the requirement (e.g. The use case\n",
    "satisfies a functional requirement).\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_sysml_shapes.trace, RDF.type, oslc.Property))\n",
    "    g.add((oslc_sysml_shapes.trace, oslc.name, Literal('trace')))\n",
    "    g.add((oslc_sysml_shapes.trace, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_sysml_shapes.trace, oslc.propertyDefinition, jazz_am.trace))\n",
    "    g.add((oslc_sysml_shapes.trace, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_sysml_shapes.trace, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_sysml_shapes.trace, oslc.range, oslc.Any))\n",
    "    g.add((oslc_sysml_shapes.trace, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_sysml_shapes.trace, DCTERMS.description, Literal(\"\"\"The model element has a trace to the requirement (e.g. An attribute\n",
    "or its value are traced to a requirement).\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "\n",
    "g.serialize(destination=f'../{shapes_file}')\n",
    "\n",
    "if genOASIS:  # add the copywrite header\n",
    "    with open('../sysml-shapes.ttl','r') as f:\n",
    "        with open('../temp.ttl','w') as f2: \n",
    "            f2.write(copyright)\n",
    "            f2.write(f.read())\n",
    "    os.remove('../sysml-shapes.ttl')\n",
    "    os.rename('../temp.ttl','../sysml-shapes.ttl')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Get SysML v2 classes\n",
    "A notebook to get a list of the SysML v2 classes and generate the vocabToShape div sections needed in sysml-shapes.html.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Graph identifier=N99bfa89dc90247038d7de2d2494cccc6 (<class 'rdflib.graph.Graph'>)>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read and parse the sysml-vocab.ttl file\n",
    "from rdflib import Graph, URIRef, Literal, Namespace, RDF\n",
    "\n",
    "# some useful RDF namespaces\n",
    "rdf = Namespace(\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\")\n",
    "rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')\n",
    "DCTERMS = Namespace('http://purl.org/dc/terms/')\n",
    "oslc = Namespace('http://open-services.net/ns/core#')\n",
    "oslc_am = Namespace('http://open-services.net/ns/am#')\n",
    "\n",
    "g = Graph()\n",
    "g.parse('../SysML-vocab.ttl')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AcceptActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#AcceptActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ActionDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ActionDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ActorMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#ActorMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AllocationDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#AllocationDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AllocationUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#AllocationUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AnalysisCaseDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#AnalysisCaseDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AnalysisCaseUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#AnalysisCaseUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AnnotatingElement\"\n",
      "        data-include=\"./SysML-shapes.ttl#AnnotatingElementShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Annotation\"\n",
      "        data-include=\"./SysML-shapes.ttl#AnnotationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AssertConstraintUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#AssertConstraintUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AssignmentActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#AssignmentActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Association\"\n",
      "        data-include=\"./SysML-shapes.ttl#AssociationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AssociationStructure\"\n",
      "        data-include=\"./SysML-shapes.ttl#AssociationStructureShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AttributeDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#AttributeDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for AttributeUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#AttributeUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Behavior\"\n",
      "        data-include=\"./SysML-shapes.ttl#BehaviorShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for BindingConnector\"\n",
      "        data-include=\"./SysML-shapes.ttl#BindingConnectorShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for BindingConnectorAsUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#BindingConnectorAsUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for BooleanExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#BooleanExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for CalculationDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#CalculationDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for CalculationUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#CalculationUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for CaseDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#CaseDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for CaseUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#CaseUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Class\"\n",
      "        data-include=\"./SysML-shapes.ttl#ClassShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Classifier\"\n",
      "        data-include=\"./SysML-shapes.ttl#ClassifierShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for CollectExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#CollectExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Comment\"\n",
      "        data-include=\"./SysML-shapes.ttl#CommentShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConcernDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConcernDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConcernUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConcernUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConjugatedPortDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConjugatedPortDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConjugatedPortTyping\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConjugatedPortTypingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Conjugation\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConjugationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConnectionDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConnectionDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConnectionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConnectionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Connector\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConnectorShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConnectorAsUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConnectorAsUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConstraintDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConstraintDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConstraintUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConstraintUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ConstructorExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#ConstructorExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ControlNode\"\n",
      "        data-include=\"./SysML-shapes.ttl#ControlNodeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for CrossSubsetting\"\n",
      "        data-include=\"./SysML-shapes.ttl#CrossSubsettingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for DataType\"\n",
      "        data-include=\"./SysML-shapes.ttl#DataTypeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for DecisionNode\"\n",
      "        data-include=\"./SysML-shapes.ttl#DecisionNodeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Definition\"\n",
      "        data-include=\"./SysML-shapes.ttl#DefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Dependency\"\n",
      "        data-include=\"./SysML-shapes.ttl#DependencyShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Differencing\"\n",
      "        data-include=\"./SysML-shapes.ttl#DifferencingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Disjoining\"\n",
      "        data-include=\"./SysML-shapes.ttl#DisjoiningShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Documentation\"\n",
      "        data-include=\"./SysML-shapes.ttl#DocumentationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Element\"\n",
      "        data-include=\"./SysML-shapes.ttl#ElementShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ElementFilterMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#ElementFilterMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for EndFeatureMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#EndFeatureMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for EnumerationDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#EnumerationDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for EnumerationUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#EnumerationUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for EventOccurrenceUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#EventOccurrenceUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ExhibitStateUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ExhibitStateUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Expose\"\n",
      "        data-include=\"./SysML-shapes.ttl#ExposeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Expression\"\n",
      "        data-include=\"./SysML-shapes.ttl#ExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Feature\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureChainExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureChainExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureChaining\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureChainingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureDirectionKind\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureDirectionKindShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureInverting\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureInvertingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureReferenceExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureReferenceExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureTyping\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureTypingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FeatureValue\"\n",
      "        data-include=\"./SysML-shapes.ttl#FeatureValueShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Flow\"\n",
      "        data-include=\"./SysML-shapes.ttl#FlowShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FlowDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#FlowDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FlowEnd\"\n",
      "        data-include=\"./SysML-shapes.ttl#FlowEndShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FlowUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#FlowUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ForLoopActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ForLoopActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ForkNode\"\n",
      "        data-include=\"./SysML-shapes.ttl#ForkNodeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for FramedConcernMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#FramedConcernMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Function\"\n",
      "        data-include=\"./SysML-shapes.ttl#FunctionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for IfActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#IfActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Import\"\n",
      "        data-include=\"./SysML-shapes.ttl#ImportShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for IncludeUseCaseUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#IncludeUseCaseUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for IndexExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#IndexExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for InstantiationExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#InstantiationExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Interaction\"\n",
      "        data-include=\"./SysML-shapes.ttl#InteractionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for InterfaceDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#InterfaceDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for InterfaceUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#InterfaceUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Intersecting\"\n",
      "        data-include=\"./SysML-shapes.ttl#IntersectingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Invariant\"\n",
      "        data-include=\"./SysML-shapes.ttl#InvariantShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for InvocationExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#InvocationExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ItemDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ItemDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ItemUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ItemUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for JoinNode\"\n",
      "        data-include=\"./SysML-shapes.ttl#JoinNodeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LibraryPackage\"\n",
      "        data-include=\"./SysML-shapes.ttl#LibraryPackageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LiteralBoolean\"\n",
      "        data-include=\"./SysML-shapes.ttl#LiteralBooleanShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LiteralExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#LiteralExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LiteralInfinity\"\n",
      "        data-include=\"./SysML-shapes.ttl#LiteralInfinityShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LiteralInteger\"\n",
      "        data-include=\"./SysML-shapes.ttl#LiteralIntegerShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LiteralRational\"\n",
      "        data-include=\"./SysML-shapes.ttl#LiteralRationalShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LiteralString\"\n",
      "        data-include=\"./SysML-shapes.ttl#LiteralStringShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for LoopActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#LoopActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Membership\"\n",
      "        data-include=\"./SysML-shapes.ttl#MembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MembershipExpose\"\n",
      "        data-include=\"./SysML-shapes.ttl#MembershipExposeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MembershipImport\"\n",
      "        data-include=\"./SysML-shapes.ttl#MembershipImportShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MergeNode\"\n",
      "        data-include=\"./SysML-shapes.ttl#MergeNodeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Metaclass\"\n",
      "        data-include=\"./SysML-shapes.ttl#MetaclassShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MetadataAccessExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#MetadataAccessExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MetadataDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#MetadataDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MetadataFeature\"\n",
      "        data-include=\"./SysML-shapes.ttl#MetadataFeatureShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MetadataUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#MetadataUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Multiplicity\"\n",
      "        data-include=\"./SysML-shapes.ttl#MultiplicityShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for MultiplicityRange\"\n",
      "        data-include=\"./SysML-shapes.ttl#MultiplicityRangeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Namespace\"\n",
      "        data-include=\"./SysML-shapes.ttl#NamespaceShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for NamespaceExpose\"\n",
      "        data-include=\"./SysML-shapes.ttl#NamespaceExposeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for NamespaceImport\"\n",
      "        data-include=\"./SysML-shapes.ttl#NamespaceImportShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for NullExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#NullExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ObjectiveMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#ObjectiveMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for OccurrenceDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#OccurrenceDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for OccurrenceUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#OccurrenceUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for OperatorExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#OperatorExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for OwningMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#OwningMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Package\"\n",
      "        data-include=\"./SysML-shapes.ttl#PackageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ParameterMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#ParameterMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PartDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#PartDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PartUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#PartUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PayloadFeature\"\n",
      "        data-include=\"./SysML-shapes.ttl#PayloadFeatureShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PerformActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#PerformActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PortConjugation\"\n",
      "        data-include=\"./SysML-shapes.ttl#PortConjugationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PortDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#PortDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PortUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#PortUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for PortionKind\"\n",
      "        data-include=\"./SysML-shapes.ttl#PortionKindShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Predicate\"\n",
      "        data-include=\"./SysML-shapes.ttl#PredicateShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Redefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#RedefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ReferenceSubsetting\"\n",
      "        data-include=\"./SysML-shapes.ttl#ReferenceSubsettingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ReferenceUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ReferenceUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Relationship\"\n",
      "        data-include=\"./SysML-shapes.ttl#RelationshipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for RenderingDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#RenderingDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for RenderingUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#RenderingUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for RequirementConstraintKind\"\n",
      "        data-include=\"./SysML-shapes.ttl#RequirementConstraintKindShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for RequirementConstraintMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#RequirementConstraintMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for RequirementDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#RequirementDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for RequirementUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#RequirementUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for RequirementVerificationMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#RequirementVerificationMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ResultExpressionMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#ResultExpressionMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ReturnParameterMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#ReturnParameterMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for SatisfyRequirementUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#SatisfyRequirementUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for SelectExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#SelectExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for SendActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#SendActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Specialization\"\n",
      "        data-include=\"./SysML-shapes.ttl#SpecializationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for StakeholderMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#StakeholderMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for StateDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#StateDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for StateSubactionKind\"\n",
      "        data-include=\"./SysML-shapes.ttl#StateSubactionKindShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for StateSubactionMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#StateSubactionMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for StateUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#StateUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Step\"\n",
      "        data-include=\"./SysML-shapes.ttl#StepShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Structure\"\n",
      "        data-include=\"./SysML-shapes.ttl#StructureShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Subclassification\"\n",
      "        data-include=\"./SysML-shapes.ttl#SubclassificationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for SubjectMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#SubjectMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Subsetting\"\n",
      "        data-include=\"./SysML-shapes.ttl#SubsettingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Succession\"\n",
      "        data-include=\"./SysML-shapes.ttl#SuccessionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for SuccessionAsUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#SuccessionAsUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for SuccessionFlow\"\n",
      "        data-include=\"./SysML-shapes.ttl#SuccessionFlowShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for SuccessionFlowUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#SuccessionFlowUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TerminateActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#TerminateActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TextualRepresentation\"\n",
      "        data-include=\"./SysML-shapes.ttl#TextualRepresentationShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TransitionFeatureKind\"\n",
      "        data-include=\"./SysML-shapes.ttl#TransitionFeatureKindShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TransitionFeatureMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#TransitionFeatureMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TransitionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#TransitionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TriggerInvocationExpression\"\n",
      "        data-include=\"./SysML-shapes.ttl#TriggerInvocationExpressionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TriggerKind\"\n",
      "        data-include=\"./SysML-shapes.ttl#TriggerKindShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Type\"\n",
      "        data-include=\"./SysML-shapes.ttl#TypeShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for TypeFeaturing\"\n",
      "        data-include=\"./SysML-shapes.ttl#TypeFeaturingShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Unioning\"\n",
      "        data-include=\"./SysML-shapes.ttl#UnioningShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for Usage\"\n",
      "        data-include=\"./SysML-shapes.ttl#UsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for UseCaseDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#UseCaseDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for UseCaseUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#UseCaseUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for VariantMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#VariantMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for VerificationCaseDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#VerificationCaseDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for VerificationCaseUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#VerificationCaseUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ViewDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ViewDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ViewRenderingMembership\"\n",
      "        data-include=\"./SysML-shapes.ttl#ViewRenderingMembershipShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ViewUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ViewUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ViewpointDefinition\"\n",
      "        data-include=\"./SysML-shapes.ttl#ViewpointDefinitionShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for ViewpointUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#ViewpointUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for VisibilityKind\"\n",
      "        data-include=\"./SysML-shapes.ttl#VisibilityKindShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n",
      "\n",
      "\n",
      "<div\n",
      "        title=\"Constraints for WhileLoopActionUsage\"\n",
      "        data-include=\"./SysML-shapes.ttl#WhileLoopActionUsageShape\"\n",
      "        data-oninclude=\"shapeToSpec\"\n",
      "        data-include-sync=\"true\"\n",
      "        data-include-replace=\"true\"\n",
      "        data-include-format=\"html\"\n",
      "      ></div>\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# get a list of the classes and create the dev elements needed for shapeToSpec\n",
    "classes = g.subjects(rdf.type, rdfs.Class)\n",
    "\n",
    "# and now create the shapeToSpec div for each class\n",
    "for c in classes:\n",
    "    name = str(c)\n",
    "    name = name[name.index('#')+1:]\n",
    "    print(\n",
    "f\"\"\"\n",
    "\n",
    "<div\n",
    "        title=\"Constraints for {name}\"\n",
    "        data-include=\"./SysML-shapes.ttl#{name}Shape\"\n",
    "        data-oninclude=\"shapeToSpec\"\n",
    "        data-include-sync=\"true\"\n",
    "        data-include-replace=\"true\"\n",
    "        data-include-format=\"html\"\n",
    "      ></div>\n",
    "\"\"\"        \n",
    "    )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Generate OSLC KerML vocab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Graph identifier=Nd9d2c7f624334c759cce0aeb8451c365 (<class 'rdflib.graph.Graph'>)>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create the KerML vocabulary graph, initially empty\n",
    "\n",
    "oslc_kerml = Namespace('https://www.omg.org/spec/kerml/vocabulary#')\n",
    "\n",
    "g = Graph()\n",
    "g.bind('oslc_kerml', oslc_kerml)\n",
    "g.bind('oslc_am', oslc_am)\n",
    "\n",
    "# add the vocabulary ontology\n",
    "o = URIRef(oslc_kerml)\n",
    "g.add((o, RDF.type, OWL.Ontology))\n",
    "g.add((o, RDFS.label, Literal(\"OSLC KerML Vocabulary\")))\n",
    "g.add((o, DCTERMS.description, Literal(\"All vocabulary URIs defined in the OSLC KerML namespace.\", datatype=RDF.XMLLiteral)))\n",
    "g.add((o, DCTERMS.issued, Literal(\"2025-02-01\", datatype=XSD.date)))\n",
    "g.add((o, DCTERMS.license, URIRef('')))\n",
    "g.add((o, DCTERMS.publisher,  URIRef('https://www.omg.org')))\n",
    "g.add((o, DCTERMS.title, Literal(\"OSLC KerML Vocabulary\")))\n",
    "g.add((o, vann.preferredNamespacePrefix, Literal(\"oslc_kerml\")))\n",
    "g.add((o, DCTERMS.hasVersion, Literal(\"V2\")))\n",
    "g.add((o, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/KerML')))\n",
    "g.add((o, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/KerML-vocab.ttl')))\n",
    "\n",
    "# load the KerML.ecore model\n",
    "rset = ResourceSet()\n",
    "resource = rset.get_resource(URI('/Users/jamsden/Developer/SysML-v2-Pilot-Implementation/org.omg.sysml/model/KerML.ecore'))\n",
    "mm_root = resource.contents[0]\n",
    "rset.metamodel_registry[mm_root.nsURI] = mm_root\n",
    "# At this point, the .ecore is loaded in the 'rset' as a metamodel\n",
    "\n",
    "\n",
    "for c in mm_root.eClassifiers:\n",
    "    # Generate the classes\n",
    "    if isinstance(c, EClass):\n",
    "        g.add((oslc_kerml.term(c.name), RDF.type, RDFS.Class))\n",
    "        if c.name=='Element':\n",
    "            g.add((oslc_kerml.term(c.name), RDFS.subClassOf, oslc_am.Resource))  # only Element\n",
    "        if c.eSuperTypes is not None and len(c.eSuperTypes) >= 1:\n",
    "            for super in c.eSuperTypes:\n",
    "                g.add((oslc_kerml.term(c.name), RDFS.subClassOf, oslc_kerml.term(super.name)))\n",
    "        g.add((oslc_kerml.term(c.name), RDFS.label, Literal(c.name)))\n",
    "        g.add((oslc_kerml.term(c.name), RDFS.comment, Literal(comment(c))))\n",
    "        g.add((oslc_kerml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_kerml)))\n",
    "\n",
    "        # generate the properties\n",
    "        for a in c.eStructuralFeatures:\n",
    "            name = a.name  # use the class name as a prefix to the attribute name to ensure they are unique\n",
    "            s = oslc_kerml.term(name)\n",
    "            g.add((s, RDF.type, RDF.Property))\n",
    "            g.add((s, RDFS.label, Literal(name)))\n",
    "            pcomment = g.value(s, RDFS.comment)\n",
    "            if pcomment is not None:\n",
    "                # This is a property with multiple domains\n",
    "                # Concatenate the comment for each domain class into a single comment\n",
    "                pcomment = pcomment + '\\n' + c.name+': '+comment(a)\n",
    "                g.remove((s, RDFS.comment, None))\n",
    "                g.add((s, RDFS.comment, Literal(pcomment)))\n",
    "            else:\n",
    "                g.add((s, RDFS.comment, Literal(c.name+': '+comment(a))))\n",
    "            g.add((s, RDFS.isDefinedBy, URIRef(oslc_kerml)))\n",
    "    if isinstance(c, EEnum):\n",
    "        g.add((oslc_kerml.term(c.name), RDF.type, RDFS.Class))\n",
    "        g.add((oslc_kerml.term(c.name), RDFS.label, Literal(c.name)))\n",
    "        g.add((oslc_kerml.term(c.name), RDFS.comment, Literal(comment(c))))\n",
    "        g.add((oslc_kerml.term(c.name), RDFS.isDefinedBy, URIRef(oslc_kerml)))\n",
    "\n",
    "        # generate the enumeration literals\n",
    "        for a in c.eLiterals:\n",
    "            name = a.name  # don't use the class name as a prefix to the attribute name to ensure they are unique\n",
    "            s = oslc_kerml.term(name)\n",
    "            g.add((s, RDF.type, oslc_kerml.term(c.name)))\n",
    "            g.add((s, RDFS.label, Literal(name)))\n",
    "            g.add((s, RDFS.comment, Literal(comment(a))))\n",
    "            g.add((s, RDFS.isDefinedBy, URIRef(oslc_kerml)))\n",
    "        \n",
    "g.serialize(destination='../KerML-vocab.ttl')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Graph identifier=N1c9b988e5a4648dfba27a16c770d9f7e (<class 'rdflib.graph.Graph'>)>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Generate KerML Constraints\n",
    "\n",
    "    \n",
    "\n",
    "# create the SysML constraints graph, initially empty\n",
    "oslc_kerml_shapes = Namespace('https://www.omg.org/spec/kerml/20250201/shapes#')\n",
    "jazz_am = Namespace('http://jazz.net/ns/dm/linktypes#')\n",
    "\n",
    "g = Graph()\n",
    "g.bind('oslc_kerml', oslc_kerml)\n",
    "g.bind('oslc_am', oslc_am)\n",
    "g.bind('oslc', oslc)\n",
    "g.bind('', oslc_kerml_shapes)\n",
    "g.bind('jazz_am', jazz_am)\n",
    "\n",
    "s = URIRef(oslc_kerml_shapes)\n",
    "g.add((s, RDF.type, oslc.ResourceShapeConstraints))\n",
    "g.add((s, RDFS.label, Literal(\"OSLC  Kernel Modeling Language (KerML) Constraints\")))\n",
    "g.add((s, DCTERMS.dateCopyrighted, Literal(\"2012-2024\")))\n",
    "g.add((s, DCTERMS.description, Literal(\"<p>Constraints on vocabulary terms defined in the OSLC Kernel Modeling Language (KerML) namespace.</p>\", datatype=RDF.XMLLiteral)))\n",
    "g.add((s, DCTERMS.publisher,  URIRef('https://www.omg.org')))\n",
    "g.add((s, DCTERMS.title, Literal(\"OSLC Kernel Modeling Language (SysML) Version 2.0 Constraints\")))\n",
    "g.add((s, DCTERMS.hasVersion, Literal(\"V2\")))\n",
    "g.add((s, DCTERMS.isPartOf, URIRef('https://www.omg.org/spec/KerML')))\n",
    "g.add((s, DCTERMS.source, URIRef('https://github.com/Systems-Modeling/SysML-v2-API-Services/tree/master/public/oslc/KerML-vocab.ttl')))\n",
    "g.add((s, DCTERMS.license, URIRef('')))\n",
    "\n",
    "for c in mm_root.eClassifiers:\n",
    "    # Generate the ResourceShape\n",
    "    if isinstance(c, EClass):\n",
    "        shape = oslc_kerml_shapes.term(c.name+'Shape')\n",
    "        g.add((shape, RDF.type, oslc.ResourceShape))  # only Element\n",
    "        g.add((shape, DCTERMS.title, Literal(c.name+'Shape', datatype=RDF.XMLLiteral)))\n",
    "        g.add((shape, DCTERMS.description, Literal(comment(c,strip=False),datatype=RDF.XMLLiteral)))\n",
    "        g.add((shape, oslc.describes, URIRef(oslc_kerml.term(c.name))))\n",
    "\n",
    "        # add all the properties inherited from all superclasses up to Element\n",
    "        addSuperclassProperties(c, shape, g, oslc_kerml, oslc_kerml_shapes)\n",
    "        addClassProperties(c, shape, g, oslc_kerml, oslc_kerml_shapes)\n",
    "\n",
    "        # add the inherited oslc_am:Resource properties\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.type))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.dctype))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.identifier))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.title))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.shortTitle))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.description))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.source))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.creator))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.created))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.contributor))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.modified))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.serviceProvider))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.instanceShape))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.derives))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.elaborates))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.refine))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.external))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.satisfy))\n",
    "        g.add((shape, oslc.property, oslc_kerml_shapes.trace))\n",
    "        \n",
    "    # and create the oslc_am:Resource inherited oslc:Property items\n",
    "    g.add((oslc_kerml_shapes.type, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.type, oslc.name, Literal('type')))\n",
    "    g.add((oslc_kerml_shapes.type, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.type, oslc.propertyDefinition, RDF.type))\n",
    "    g.add((oslc_kerml_shapes.type, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.type, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.type, oslc.range, RDFS.Class))\n",
    "    g.add((oslc_kerml_shapes.type, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.type, DCTERMS.description, Literal(\"The resource type URIs.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.dctype, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.dctype, oslc.name, Literal('dctype')))\n",
    "    g.add((oslc_kerml_shapes.dctype, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.dctype, oslc.propertyDefinition, DCTERMS.type))\n",
    "    g.add((oslc_kerml_shapes.dctype, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.dctype, oslc.valueType, XSD.string))\n",
    "    g.add((oslc_kerml_shapes.dctype, DCTERMS.description, Literal(\"A short string representation for the type, for example ‘Car’.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.identifier, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.identifier, oslc.name, Literal('identifier')))\n",
    "    g.add((oslc_kerml_shapes.identifier, oslc.occurs, oslc['Exactly-one']))\n",
    "    g.add((oslc_kerml_shapes.identifier, oslc.propertyDefinition, DCTERMS.identifier))\n",
    "    g.add((oslc_kerml_shapes.identifier, oslc.readOnly, Literal('true',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.identifier, oslc.valueType, XSD.string))\n",
    "    g.add((oslc_kerml_shapes.identifier, DCTERMS.description, Literal(\"\"\"A unique identifier for a resource. Typically read-only and assigned by the\n",
    "service provider when a resource is created. Not typically intended for end-user display.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.title, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.title, oslc.name, Literal('title')))\n",
    "    g.add((oslc_kerml_shapes.title, oslc.occurs, oslc['Exactly-one']))\n",
    "    g.add((oslc_kerml_shapes.title, oslc.propertyDefinition, DCTERMS.title))\n",
    "    g.add((oslc_kerml_shapes.title, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.title, oslc.valueType, RDF.XMLLiteral))\n",
    "    g.add((oslc_kerml_shapes.title, DCTERMS.description, Literal(\"Title of the resource represented as rich text in XHTML content.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.shortTitle, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.shortTitle, oslc.name, Literal('shortTitle')))\n",
    "    g.add((oslc_kerml_shapes.shortTitle, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_kerml_shapes.shortTitle, oslc.propertyDefinition, oslc.shortTitle))\n",
    "    g.add((oslc_kerml_shapes.shortTitle, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.shortTitle, oslc.valueType, RDF.XMLLiteral))\n",
    "    g.add((oslc_kerml_shapes.shortTitle, DCTERMS.description, Literal(\"{{Short name identifying a resource, often used as an abbreviated identifier for presentation to end-users. SHOULD include only content that is valid inside an XHTML &lt;span&gt; element}}.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.description, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.description, oslc.name, Literal('description')))\n",
    "    g.add((oslc_kerml_shapes.description, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_kerml_shapes.description, oslc.propertyDefinition, DCTERMS.description))\n",
    "    g.add((oslc_kerml_shapes.description, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.description, oslc.valueType, RDF.XMLLiteral))\n",
    "    g.add((oslc_kerml_shapes.description, DCTERMS.description, Literal(\"Descriptive text about resource represented as rich text in XHTML content.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.source, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.source, oslc.name, Literal('source')))\n",
    "    g.add((oslc_kerml_shapes.source, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_kerml_shapes.source, oslc.propertyDefinition, DCTERMS.source))\n",
    "    g.add((oslc_kerml_shapes.source, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.source, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.source, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.source, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.source, DCTERMS.description, Literal(\"The resource URI a client can perform a get on to obtain the original non-OSLC AM formatted resource that was used to create this resource. The source resource is usually a binary or proprietary format that the service provider can consume and convert into an OSLC AM format. The service may use content negotiation with the Accept header to obtain the desired content type.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.creator, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.creator, oslc.name, Literal('creator')))\n",
    "    g.add((oslc_kerml_shapes.creator, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.creator, oslc.propertyDefinition, DCTERMS.creator))\n",
    "    g.add((oslc_kerml_shapes.creator, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.creator, oslc.valueType, oslc.AnyResource))\n",
    "    g.add((oslc_kerml_shapes.creator, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.creator, oslc.representation, oslc.Either))\n",
    "    g.add((oslc_kerml_shapes.creator, DCTERMS.description, Literal(\"Creator or creators of the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.created, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.created, oslc.name, Literal('created')))\n",
    "    g.add((oslc_kerml_shapes.created, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_kerml_shapes.created, oslc.propertyDefinition, DCTERMS.created))\n",
    "    g.add((oslc_kerml_shapes.created, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.created, oslc.valueType, XSD.dateTime))\n",
    "    g.add((oslc_kerml_shapes.created, DCTERMS.description, Literal(\"Timestamp of resource creation.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.contributor, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.contributor, oslc.name, Literal('contributor')))\n",
    "    g.add((oslc_kerml_shapes.contributor, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.contributor, oslc.propertyDefinition, DCTERMS.contributor))\n",
    "    g.add((oslc_kerml_shapes.contributor, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.contributor, oslc.valueType, oslc.AnyResource))\n",
    "    g.add((oslc_kerml_shapes.contributor, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.contributor, oslc.representation, oslc.Either))\n",
    "    g.add((oslc_kerml_shapes.contributor, DCTERMS.description, Literal(\"Contributor or contributors to the resource. It is likely that the target resource will be a foaf:Person but that is not necessarily the case.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.modified, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.modified, oslc.name, Literal('modified')))\n",
    "    g.add((oslc_kerml_shapes.modified, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_kerml_shapes.modified, oslc.propertyDefinition, DCTERMS.modified))\n",
    "    g.add((oslc_kerml_shapes.modified, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.modified, oslc.valueType, XSD.dateTime))\n",
    "    g.add((oslc_kerml_shapes.modified, DCTERMS.description, Literal(\"Timestamp of latest resource modification.\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, oslc.name, Literal('serviceProvider')))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, oslc.propertyDefinition, oslc.serviceProvider))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, oslc.range, oslc.ServiceProvider))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.serviceProvider, DCTERMS.description, Literal(\"\"\"A link to the resource's OSLC Service Provider. There may be cases when the\n",
    "subject resource is available from a service provider that implements multiple domain\n",
    "specifications, which could result in multiple values for this property.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.instanceShape, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, oslc.name, Literal('instanceShape')))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, oslc.occurs, oslc['Zero-or-one']))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, oslc.propertyDefinition, oslc.instanceShape))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, oslc.range, oslc.ResourceShape))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.instanceShape, DCTERMS.description, Literal(\"\"\"The URI of a Resource Shape that describes the possible properties, occurrence,\n",
    "value types, allowed values and labels. This shape information is useful in displaying the subject\n",
    "resource as well as guiding clients in performing modifications. Instance shapes may be specific\n",
    "to the authenticated user associated with the request that retrieved the resource, the current\n",
    "state of the resource and other factors and thus should not be cached.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.derives, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.derives, oslc.name, Literal('derives')))\n",
    "    g.add((oslc_kerml_shapes.derives, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.derives, oslc.propertyDefinition, jazz_am.derives))\n",
    "    g.add((oslc_kerml_shapes.derives, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.derives, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.derives, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.derives, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.derives, DCTERMS.description, Literal(\"\"\"The resource that derives from another resource originated from or is\n",
    "significantly influenced by the referenced resource. For example a model element derives from a\n",
    "requirement.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.elaborates, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.elaborates, oslc.name, Literal('elaborates')))\n",
    "    g.add((oslc_kerml_shapes.elaborates, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.elaborates, oslc.propertyDefinition, jazz_am.elaborates))\n",
    "    g.add((oslc_kerml_shapes.elaborates, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.elaborates, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.elaborates, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.elaborates, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.elaborates, DCTERMS.description, Literal(\"\"\"This resource elaborates the referenced resource.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.refine, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.refine, oslc.name, Literal('refine')))\n",
    "    g.add((oslc_kerml_shapes.refine, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.refine, oslc.propertyDefinition, jazz_am.refine))\n",
    "    g.add((oslc_kerml_shapes.refine, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.refine, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.refine, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.refine, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.refine, DCTERMS.description, Literal(\"\"\"The target is a refinement of the source. (e.g. a use case scenario\n",
    "might be a refinement of a textual requirement that describes the interaction).\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.external, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.external, oslc.name, Literal('external')))\n",
    "    g.add((oslc_kerml_shapes.external, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.external, oslc.propertyDefinition, jazz_am.external))\n",
    "    g.add((oslc_kerml_shapes.external, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.external, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.external, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.external, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.external, DCTERMS.description, Literal(\"\"\"A generic link from a resource to an external web page.\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.satisfy, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.satisfy, oslc.name, Literal('satisfy')))\n",
    "    g.add((oslc_kerml_shapes.satisfy, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.satisfy, oslc.propertyDefinition, jazz_am.satisfy))\n",
    "    g.add((oslc_kerml_shapes.satisfy, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.satisfy, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.satisfy, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.satisfy, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.satisfy, DCTERMS.description, Literal(\"\"\"The model element satisfies the requirement (e.g. The use case\n",
    "satisfies a functional requirement).\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "    g.add((oslc_kerml_shapes.trace, RDF.type, oslc.Property))\n",
    "    g.add((oslc_kerml_shapes.trace, oslc.name, Literal('trace')))\n",
    "    g.add((oslc_kerml_shapes.trace, oslc.occurs, oslc['Zero-or-many']))\n",
    "    g.add((oslc_kerml_shapes.trace, oslc.propertyDefinition, jazz_am.trace))\n",
    "    g.add((oslc_kerml_shapes.trace, oslc.readOnly, Literal('false',datatype=XSD.boolean)))\n",
    "    g.add((oslc_kerml_shapes.trace, oslc.valueType, oslc.Resource))\n",
    "    g.add((oslc_kerml_shapes.trace, oslc.range, oslc.Any))\n",
    "    g.add((oslc_kerml_shapes.trace, oslc.representation, oslc.Reference))\n",
    "    g.add((oslc_kerml_shapes.trace, DCTERMS.description, Literal(\"\"\"The model element has a trace to the requirement (e.g. An attribute\n",
    "or its value are traced to a requirement).\"\"\", datatype=RDF.XMLLiteral)))\n",
    "\n",
    "\n",
    "g.serialize(destination='../KerML-shapes.ttl')\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

````
