pipeline {
    agent any
    stages {
        stage('Initialize') {
            steps {
                sh 'python --version'
            }
        }

	stage ('Build'){
		steps {
			echo 'Hello World'
		}
	}

	stage('Deploy'){
	    steps {
	        sh 'python manage.py runserver'
	    }
	}

    }
}
