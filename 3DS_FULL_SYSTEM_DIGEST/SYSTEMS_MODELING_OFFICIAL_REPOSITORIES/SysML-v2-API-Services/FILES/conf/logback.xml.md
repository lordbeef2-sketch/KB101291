# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/conf/logback.xml

- repository: `SysML-v2-API-Services`
- source_path: `conf/logback.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/conf/logback.xml
- source_bytes: 1557
- source_sha256: `3d36803e86d74e18b61bb266090cf828775795e57de991239b4288a62b152530`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<!-- https://www.playframework.com/documentation/latest/SettingsLogger -->
<configuration>

  <conversionRule conversionWord="coloredLevel" converterClass="play.api.libs.logback.ColoredLevel" />

  <appender name="FILE" class="ch.qos.logback.core.FileAppender">
    <file>${application.home:-.}/logs/application.log</file>
    <encoder>
      <pattern>%date [%level] from %logger in %thread - %message%n%xException</pattern>
    </encoder>
  </appender>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%coloredLevel %logger{15} - %message%n%xException{10}</pattern>
    </encoder>
  </appender>

  <appender name="ASYNCFILE" class="ch.qos.logback.classic.AsyncAppender">
    <appender-ref ref="FILE" />
  </appender>

  <appender name="ASYNCSTDOUT" class="ch.qos.logback.classic.AsyncAppender">
    <appender-ref ref="STDOUT" />
  </appender>

  <logger name="play" level="INFO" />
  <logger name="application" level="DEBUG" />

  <!-- Off these ones as they are annoying, and anyway we manage configuration ourselves -->
  <logger name="com.avaje.ebean.config.PropertyMapLoader" level="OFF" />
  <logger name="com.avaje.ebeaninternal.server.core.XmlConfigLoader" level="OFF" />
  <logger name="com.avaje.ebeaninternal.server.lib.BackgroundThread" level="OFF" />
  <logger name="com.gargoylesoftware.htmlunit.javascript" level="OFF" />

  <root level="WARN">
    <appender-ref ref="ASYNCFILE" />
    <appender-ref ref="ASYNCSTDOUT" />
  </root>

</configuration>

````
