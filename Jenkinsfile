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

	stage ('Test'){
	steps {
			echo 'Testing'
		}
	}

	stage('Deploy'){
	    steps {
	        echo "Deploy"
	    }
	}

    }
}
