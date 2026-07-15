# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/build.sbt

- repository: `SysML-v2-API-Services`
- source_path: `build.sbt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/build.sbt
- source_bytes: 1837
- source_sha256: `a70d7b6b390acee7aeee5472efdf0fb76a95a92f0db00f2ec389b4a12a753e10`
- decoded_as: `utf-8`


## EXACT SOURCE

````scala
name := """SysML-v2-API-Services"""
organization := "org.omg"

version := "2025-02"

javacOptions ++= Seq("-source", "11", "-target", "11", "-Xlint")

lazy val root = (project in file(".")).enablePlugins(PlayJava)

scalaVersion := "2.12.6"

libraryDependencies += guice
libraryDependencies += "org.hibernate" % "hibernate-core" % "5.4.1.Final"
libraryDependencies += "org.hibernate" % "hibernate-jpamodelgen" % "5.4.1.Final"
libraryDependencies += "org.postgresql" % "postgresql" % "42.2.5"
libraryDependencies += "com.fasterxml.jackson.core" % "jackson-annotations" % "2.9.8"
libraryDependencies += "com.fasterxml.jackson.core" % "jackson-databind" % "2.9.8"
libraryDependencies += "com.fasterxml.jackson.datatype" % "jackson-datatype-hibernate5" % "2.9.8"
libraryDependencies += "io.swagger" % "swagger-play2_2.12" % "1.6.0"
libraryDependencies += "org.reflections" % "reflections" % "0.9.10"

javacOptions ++= Seq("-s", "app")

// https://stackoverflow.com/questions/42568234/intellij-idea-support-for-immutables-with-sbt
// tell sbt (and by extension IDEA) that there is source code in target/generated_sources
managedSourceDirectories in Compile += baseDirectory.value / "generated"
// before compilation happens, create the target/generated_sources directory
compile in Compile := (compile in Compile).dependsOn(Def.task({
  (baseDirectory.value / "generated").mkdirs()
})).value
// tell the java compiler to output generated source files to target/generated_sources
javacOptions in Compile ++= Seq("-s", "generated")

sources in(Compile, doc) := Seq.empty
publishArtifact in(Compile, packageDoc) := false

// https://github.com/playframework/playframework/issues/8286#issuecomment-488733669
// hopefully fixed in Play 2.8
PlayKeys.devSettings += "play.server.http.idleTimeout" -> "infinite"

````
