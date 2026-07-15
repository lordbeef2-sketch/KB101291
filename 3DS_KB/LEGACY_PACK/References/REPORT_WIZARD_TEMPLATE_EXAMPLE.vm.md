# LEGACY SOURCE RECORD: References/REPORT_WIZARD_TEMPLATE_EXAMPLE.vm

<!--LEGACY_SOURCE path=References/REPORT_WIZARD_TEMPLATE_EXAMPLE.vm sha256=6e48547b4c022b21e4b503b8f0b5e2b52ef1eaeb520c53055c30988cc5739061 bytes=409 -->

- original_path: `References/REPORT_WIZARD_TEMPLATE_EXAMPLE.vm`
- original_sha256: `6e48547b4c022b21e4b503b8f0b5e2b52ef1eaeb520c53055c30988cc5739061`
- original_bytes: 409

````velocity
## Simple Report Wizard / Velocity pattern

#set($elements = $project.getPrimaryModel().ownedElement)

Project: $project.name

#foreach($element in $elements)
- $element.humanName
#end

## Notes
- In real use, replace broad traversal with a tighter scope.
- Pair this with helper modules and explicit sorting/filtering.
- Prefer stable exported schemas over raw free-form report output for machine pipelines.
````
