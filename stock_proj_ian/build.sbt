ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.11.10"

// https://mvnrepository.com/artifact/commons-io/commons-io
//libraryDependencies += "commons-io" % "commons-io" % "2.6"
// https://mvnrepository.com/artifact/org.apache.spark/spark-core
libraryDependencies += "org.apache.spark" %% "spark-core" % "2.4.3"
// https://mvnrepository.com/artifact/org.apache.spark/spark-sql
libraryDependencies += "org.apache.spark" %% "spark-sql" % "2.4.3"
// https://mvnrepository.com/artifact/org.apache.spark/spark-streaming
//libraryDependencies += "org.apache.spark" %% "spark-streaming" % "2.4.3"
// https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-client
//libraryDependencies += "org.apache.hadoop" % "hadoop-client" % "2.7.1"
libraryDependencies += "org.scalaj" %% "scalaj-http" % "2.4.2"


lazy val root = (project in file("."))
  .settings(
    name := "stock_proj_ian",
    idePackagePrefix := Some("org.ian.stock")
  )
