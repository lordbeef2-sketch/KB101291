# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/application.conf

- repository: `SysML-v2-API-Services`
- source_path: `conf/application.conf`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/application.conf
- source_bytes: 851
- source_sha256: `4279b1ce46b7d3c9036ce0b06839ec99f6b9557a917f3bede3d857fb65b24d40`
- decoded_as: `utf-8`


## EXACT SOURCE

````text
# https://www.playframework.com/documentation/latest/Configuration
play.editor="http://localhost:63342/api/file/?file=%s&line=%s"

play.http.secret.key="whatever"
play.modules.enabled += "play.modules.swagger.SwaggerModule"
play.filters.headers.contentSecurityPolicy = null
play.filters.disabled += play.filters.csrf.CSRFFilter
play.http.errorHandler = play.http.JsonHttpErrorHandler
play.http.parser.maxMemoryBuffer = 1G
play.server.http.idleTimeout = infinite

play.filters.enabled += play.filters.cors.CORSFilter
play.http.fileMimeTypes = ${play.http.fileMimeTypes} """
  jsonld=application/ld+json
"""

# https://www.playframework.com/documentation/2.7.x/JavaJPA
db.default.jndiName = DefaultDS
jpa.default = sysml2-hibernate
PlayKeys.externalizeResourcesExcludes += baseDirectory.value / "conf" / "META-INF" / "persistence.xml"
````
