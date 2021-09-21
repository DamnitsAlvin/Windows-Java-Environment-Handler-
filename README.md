# Windows-Java-Environment-Handler-
Python script that would change the PATH and JAVA_HOME variables windows registry whether in user or local machine settings. 

<h1> Usage </h1>
The script is written in python and must be run with administrative privelege. In the command prompt or  powershell type 
<code> python JavaEnvironmentHandler.py [options] [arguments] </code>
<p>Options</p>
<li>
  <ul> -u INDEX /t changes USER environment settings </ul>  
  <ul> -s INDEX /t changes SYSTEM/LOCAL MACHINE environment settings </ul>  
  <ul> -a "PATH" /t add the path of java home directory to a text file</ul>
  <ul> -r  /t reads the java home directories that is written on a file </ul>  
</li>


