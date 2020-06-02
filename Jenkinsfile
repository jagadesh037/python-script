pipeline {
	agent any
     
	stages {
		stage('Stage 1 : Check Python Installed or not -- Pre-requestic') {
			steps {
				bat 'echo off'
				echo "Check Python Version"
				bat 'python --version'
				echo "Python latest version is installed, up and running"
				bat 'echo on'
                           
            }
        }
      

		stage('Stage 2 : Run the Appliation') {
			steps {
				bat 'echo "Lets trigger the application"'
				bat 'python Hello.py'
				bat 'echo "Application Run Successful"'
			}
		}
      
    }
}
