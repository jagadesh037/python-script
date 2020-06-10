pipeline {
	agent any
     
	stages {
		stage('Stage 1 : Check Python Installed or not -- Pre-requestic') {
			steps {
				bat 'echo off'
				echo "Check Python Version"
				bat 'python --version'
				bat 'python pip.py'
				echo "Python latest version is installed, up and running"
				bat 'echo on'
                           
            		}
        	}
    	}
}
