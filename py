python -m unittest one.py
javac Hello.java
java Hello



MAVEN_HOME (paste that link)
%MAVEN_HOME%\bin
mvn --version
mvn archetype:generate -DgroupId=com.MSRIT.app -DartifactId=Abhishek -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
cd Abhishek
mvn package
java -cp target/Abhishek-1.0-SNAPSHOT.jar com.MSRIT.app.App
