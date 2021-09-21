# Windows-Java-Environment-Handler-
Python script that would change the PATH and JAVA_HOME variables windows registry whether in user or local machine settings. 

<h1> Usage </h1>
The script is written in python and must be run with administrative privelege. In the command prompt or  powershell type 
<code> python JavaEnvironmentHandler.py [options] [arguments] </code>
<p>Options</p>
<ul>
  <li> -u INDEX       changes USER environment settings </li>  
  <li> -s INDEX       changes SYSTEM/LOCAL MACHINE environment settings </li> 
  <li> -a "PATH"      add the path of java home directory to a text file </li>
  <li> -r             reads the java home directories that is written on a file </li>  
</ul>



<h1> Issues </h1>
<ol>
  <li>There seems to be a problem when changing system variables, windows registry and environment variables are changed but other applications doesn't respond immediately </li>
  <li>Problems in the .exe file </li>
</ol>
