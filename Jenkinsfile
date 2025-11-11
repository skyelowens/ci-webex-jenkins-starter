pipeline {
  agent any
  options { timestamps() }
  environment {
    WEBEX_TOKEN   = credentials('webex-bot-token')
    WEBEX_ROOM_ID = credentials('webex-room-id')
  }
  triggers {
    githubPush()
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Set up Python') {
      steps {
        sh '''
          if ! command -v python3 >/dev/null 2>&1; then
            echo "Installing Python 3 + pip (Jenkins container must run as root)..."
            apt-get update && apt-get install -y python3 python3-pip jq
          else
            if ! command -v jq >/dev/null 2>&1; then
              apt-get update && apt-get install -y jq
            fi
          fi
          python3 --version
          pip3 --version || (curl -sS https://bootstrap.pypa.io/get-pip.py | python3 -)
        '''
      }
    }
    stage('Install dependencies') {
      steps { sh 'pip3 install -r requirements.txt' }
    }
    stage('Run tests') {
      steps { sh 'pytest -q --maxfail=1 --disable-warnings' }
    }
  }
  post {
    success {
      sh '''
        TEXT="**✅ Build SUCCESS**: ${JOB_NAME} #${BUILD_NUMBER} on `${BRANCH_NAME}`\\n- Commit: ${GIT_COMMIT}\\n- Link: ${BUILD_URL}"
        /bin/bash ci/webex_notify.sh SUCCESS "$TEXT"
      '''
    }
    failure {
      sh '''
        TEXT="**❌ Build FAILED**: ${JOB_NAME} #${BUILD_NUMBER} on `${BRANCH_NAME}`\\n- Link: ${BUILD_URL}"
        /bin/bash ci/webex_notify.sh FAILURE "$TEXT"
      '''
    }
  }
}
