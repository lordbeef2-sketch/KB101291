# NOMAGIC ATTACHMENT: authserver.properties

- attachment_id: `247046559`
- space_key: `MCS`
- parent_page_id: `247046553`
- parent_page_title: Installing Web Application Platform manually
- media_type: `application/octet-stream`
- reported_bytes: 9901
- download_url: https://docs.nomagic.com/download/attachments/247046553/authserver.properties?version=1&modificationDate=1754923593813&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `f69d5b7d096eda4be49e0569aad61e0671bd0c37289560ecd9fe026af3e4f498`

## EXACT ATTACHMENT SOURCE

````text
#---------------------------------------------------
# List of allowed redirect URIs. Authentication server
# client should pass valid redirect URI to /authorize endpoint.
#---------------------------------------------------
authentication.redirect.uri.whitelist=https://127.0.0.1:8443/,https://127.0.0.1:8111/,https://md_redirect

#-------------------------------------------------------------------------------
# Authentication ID token expiration time in seconds.
#-------------------------------------------------------------------------------
#authentication.token.expirity=604800

#-------------------------------------------------------------------------------
# Authentication code expiration time in seconds.
#-------------------------------------------------------------------------------
#authentication.code.token.expirity=15

#-------------------------------------------------------------------------------
# Authentication refresh token expiration time in seconds.
#-------------------------------------------------------------------------------
#authentication.refresh.token.expirity=1209600

#-------------------------------------------------------------------------------
# Authentication ID token expiration time in seconds
# for the implicit authentication flow (for ex., used
# for MagicDraw UML).
#-------------------------------------------------------------------------------
#authentication.implicit.token.expirity=86400

#-------------------------------------------------------------------------------
# Authentication ID token that has extremely long
# expiration time and should only be used in
# server-server requests when there is a need to
# perform regular batch jobs.
#-------------------------------------------------------------------------------
#authentication.unlimited.token.expirity=630720000

#-------------------------------------------------------------------------------
# Properties used for keystore reading:
#
# - Path to keystore file (absolute or relative)
# - Keystore type (JKS or PKCS12)
# - Keystore password
# - Private key password
# - Private key alias in the keystore
#
# If service is deployed on a cluster, all instances should use the same keystore.
#-------------------------------------------------------------------------------
authentication.server.key-store=../TeamworkCloud/configuration/keystore.p12
authentication.server.key-store-type=PKCS12
authentication.server.key-store-password=nomagic
authentication.server.key-password=nomagic
authentication.server.key-alias=teamworkcloud

#-------------------------------------------------------------------------------
# Valid client IDs (separated by commas).
#-------------------------------------------------------------------------------
#authentication.client.ids=MAGICDRAW,webApplicationPlatform,twcSynchronizationManager

#-------------------------------------------------------------------------------
# Implicit authentication flow client IDs (separated by commas).
#-------------------------------------------------------------------------------
#authentication.client.implicit=MAGICDRAW

#-------------------------------------------------------------------------------
# Client IDs that use token ID of unlimited expiration (separated by commas).
#-------------------------------------------------------------------------------
#authentication.client.unlimited=twcSynchronizationManager

#-------------------------------------------------------------------------------
# IDs of clients that do not see Remember Me flag (separated by commas).
#-------------------------------------------------------------------------------
#authentication.remember.me.hidden.client.ids=MAGICDRAW

#---------------------------------------------------
# SAML integration parameters:
# * Enabling/disabling flag
# * Name of Authentication Server as service provider
# configured in SAML based Identity Provider.
# * SAML Identity Provider metadata URL (for IdP that
# has metadata URL, for ex., Forgerock OpenAM).
# * Path to SAML Identity Provider metadata file (for IdP
# that has no metadata URL, for ex., WSO2). File should
# be created in accordance with IdP provided specification.
# * Title of the button for SAML user login displayed
# in login page.
# * Flag indicating if ForceAuthn is changed in the AuthnRequest.
# * Signature algorithm (SHA1, SHA256 or SHA512).
# * List of AuthN Contexts separated by comma.
# * AuthN Context comparison type (exact, better, maximum, minimum).
# * Flag indicating if SAML authentication detailed error text should be displayed for user.
#---------------------------------------------------
authentication.saml.enabled=false
#authentication.saml.entity.id=com.nomagic.authentication.server
#authentication.saml.name.id.format=urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName
#authentication.saml.idp.metadata.url=
#authentication.saml.idp.metadata.file=
#authentication.saml.link=SAML User
#authentication.saml.disable.force.authentication=false
#authentication.saml.signature.algorithm=SHA1
#authentication.saml.authn.contexts=
#authentication.saml.authn.context.comparison.type=exact
#authentication.saml.error.visible=false

#-------------------------------------------------------------------------------
# Indicates if authentication by certificate is available.
#-------------------------------------------------------------------------------
authentication.certificate.enabled=false

#-------------------------------------------------------------------------------
# If certificate authentication is enabled, following parameters are used for
# username extraction from the certificate subject DN (distinguished name) or
# SAN (subject alternative name) field. User name is stored in the TWCloud
# server.
# * Source of the user name. Available values: dn (distinguished name), san 
#   (subject alternative name)
# * SAN type. Available values: 0 (other name), 1 (RFC 822 name), 2 (DNS name),
#   4 (directory name).
# * SAN identifier to use if SAN type is 0.
# * Template to use if user name source is DN or SAN type is 4.
#-------------------------------------------------------------------------------
#authentication.certificate.username.source=dn
#authentication.certificate.username.san.type=4
#authentication.certificate.username.san.id=
#authentication.certificate.username.template=(CN)

#-------------------------------------------------------------------------------
# If certificate authentication is enabled, following parameters are used for
# user display name extraction from the certificate subject DN (distinguished
# name) or SAN (subject alternative name) field. Display name is used for
# display purposes only, and describes the text that is shown on authentication
# button.
# * Source of the display name. Available values: dn (distinguished name), san 
#   (subject alternative name)
# * SAN type. Available values: 0 (other name), 1 (RFC 822 name), 2 (DNS name),
#   4 (directory name).
# * SAN identifier to use if SAN type is 0.
# * Template to use if display name source is DN or SAN type is 4.
#-------------------------------------------------------------------------------
#authentication.certificate.displayname.source=dn
#authentication.certificate.displayname.san.type=4
#authentication.certificate.displayname.san.id=
#authentication.certificate.displayname.template=(CN)

#-------------------------------------------------------------------------------
# URL or absolute filesystem path to the CRL file that
# contains the list of the certificates revoked by the
# certificate authority.
#-------------------------------------------------------------------------------
#authentication.certificate.revocation.list.url=
#authentication.certificate.revocation.list.file=

#-------------------------------------------------------------------------------
# Flag indicating of secured connection is used to communicate with Cassandra.
# Flag indicating if SSL certificate check should be done while connecting to Cassandra.
# Cassandra contact points, separated by commas;
# Cassandra seeds path registered in Zookeeper (not enabled by default);
# Cassandra port for CQL clients;
# Cassandra keyspace replication factor;
# Number of max attempts to connect to Cassandra on server startup;
# Time interval between attempts in milliseconds.
#-------------------------------------------------------------------------------
cassandra.ssl.enabled=false
cassandra.ssl.ignore.certificate=true
cassandra.contactPoints=127.0.0.1
#cassandra.contactPoints.zookeeper.path=/cassandra/seeds
cassandra.port=9042
cassandra.keyspace.replication.factor=1
cassandra.connection.max.attempts=10
cassandra.connection.sleep.before.attempt=30000
#cassandra.username=cassandra
#cassandra.password=cassandra

#-------------------------------------------------------------------------------
# Properties for GUI transformation:
# 1. Path to the banner logo if such used, for ex., ./banner.png.
# File types JPEG, GIF and PNG are supported.
# 2. Banner text. Only new line (\n) special symbol is supported.
# 3. Color for login page background. Different formats allowed,
# for ex., #FFFFFF, rgb(220,220,220), etc. Default color is rgb(250,250,250).
#-------------------------------------------------------------------------------
#classification.loginbannerlogo=
#classification.loginbannertext=
#classification.loginbackground=

#-------------------------------------------------------------------------------
# Ability to disable username/password authentication
# if external user authentication (CAC, SAML) is used.
#-------------------------------------------------------------------------------
#authentication.disable.credentials=false
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "247046559",
  "type": "attachment",
  "status": "current",
  "title": "authserver.properties",
  "version": {
    "by": {
      "type": "known",
      "username": "ingabe",
      "userKey": "ff80808151f3008c0152c05ba1a40003",
      "profilePicture": {
        "path": "/download/attachments/7415957/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Inga A.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151f3008c0152c05ba1a40003"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2025-08-11T16:46:33.813+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/247046559/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/247046559"
    }
  },
  "position": -1,
  "container": {
    "id": "247046553",
    "type": "page",
    "status": "current",
    "title": "Installing Web Application Platform manually",
    "position": 4,
    "extensions": {
      "position": 4
    },
    "_links": {
      "webui": "/spaces/MCS/pages/247046553/Installing+Web+Application+Platform+manually",
      "edit": "/pages/resumedraft.action?draftId=247046553",
      "tinyui": "/x/maG5Dg",
      "self": "https://docs.nomagic.com/rest/api/content/247046553"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/247046553/child",
      "restrictions": "/rest/api/content/247046553/restriction/byOperation",
      "history": "/rest/api/content/247046553/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/247046553/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/247046553/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/octet-stream"
  },
  "extensions": {
    "mediaType": "application/octet-stream",
    "fileSize": 9901,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/247046553/authserver.properties?version=1&modificationDate=1754923593813&api=v2",
    "webui": "/spaces/MCS/pages/247046553/Installing+Web+Application+Platform+manually?preview=%2F247046553%2F247046559%2Fauthserver.properties",
    "self": "https://docs.nomagic.com/rest/api/content/247046559"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/247046559/child",
    "restrictions": "/rest/api/content/247046559/restriction/byOperation",
    "history": "/rest/api/content/247046559/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/247046559/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/247046559/restriction/relevantViewRestrictions"
  }
}
````
