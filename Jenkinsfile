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
		stage('Parallel Stage') {
			parallel {     

				stage('Stage 2 : Run the Appliation') {
					steps {
						bat 'echo "Lets trigger the application"'
						bat 'python Hello.py'
						bat 'echo "Application Run Successful"'
					}
				}
				stage('Stage 3 : verify the failed scenaio') {
					steps {
						bat 'echo "Lets trigger the application with failed scenario"'
						bat 'python failed_scenario'
						bat 'echo "Application Run Successful with failed scenario"'
					}
				}	
				stage('Stage 4 : verify the calculator') {
					steps {
						bat 'echo "Lets trigger the application with calculator"'
						bat 'python calculator.py'
						bat 'echo "Application Run Successful with calculator"'
					}
				}
			
			}
		}      
    }
}
