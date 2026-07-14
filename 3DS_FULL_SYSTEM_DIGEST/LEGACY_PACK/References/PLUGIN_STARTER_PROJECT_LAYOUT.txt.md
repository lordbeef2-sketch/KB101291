# LEGACY SOURCE RECORD: References/PLUGIN_STARTER_PROJECT_LAYOUT.txt

<!--LEGACY_SOURCE path=References/PLUGIN_STARTER_PROJECT_LAYOUT.txt sha256=9ffa0b2511b184a568ebd0de64ff66e73edba7fe390db980e5aa988e0240b1ee bytes=508 -->

- original_path: `References/PLUGIN_STARTER_PROJECT_LAYOUT.txt`
- original_sha256: `9ffa0b2511b184a568ebd0de64ff66e73edba7fe390db980e5aa988e0240b1ee`
- original_bytes: 508

````text
plugin-starter/
  README.md
  build.gradle or pom.xml
  src/
    main/
      java/
        example/
          ExamplePlugin.java
      resources/
        plugin.xml
        icons/
  libs/
    optional third-party jars if policy allows
  docs/
    supported-versions.md
    deployment.md
    rollback.md
  samples/
    expected-output.csv

Recommended minimum docs:
- supported Cameo line(s)
- supported Java line
- whether the plugin is read-only or write-capable
- deployment steps
- removal/rollback steps
````
