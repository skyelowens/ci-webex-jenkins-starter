pipeline {
  agent any
<<<<<<< HEAD
  environment { VENV = ".venv" }
  triggers { githubPush() }
  options { timestamps(); ansiColor('xterm') }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'echo "Last commit:" && git log -1 --pretty=format:"%h - %an: %s" || true'
      }
    }
    stage('Setup Python') {
      steps {
        sh '''
          set -euxo pipefail
          python3 --version
          python3 -m venv ${VENV}
          . ${VENV}/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          chmod +x scripts/notify_webex.py || true
        '''
      }
    }
    stage('Test') {
      steps {
        sh '''
          set -euxo pipefail
          . ${VENV}/bin/activate
          pytest --junitxml=pytest-report.xml
        '''
      }
    }
    stage('Publish JUnit') { steps { junit 'pytest-report.xml' } }
  }
  post {
    success {
      withCredentials([
        string(credentialsId: 'WEBEX_TOKEN', variable: 'WEBEX_BOT_TOKEN'),
        string(credentialsId: 'WEBEX_ROOM_ID', variable: 'WEBEX_ROOM_ID')
      ]) {
        sh '''
          set -euxo pipefail
          . ${VENV}/bin/activate
          python scripts/notify_webex.py "$WEBEX_BOT_TOKEN" "$WEBEX_ROOM_ID" "✅ Build ${JOB_NAME} #${BUILD_NUMBER} *SUCCESS* on branch ${BRANCH_NAME:-unknown} (commit $(git rev-parse --short HEAD))."
        '''
      }
    }
    failure {
      withCredentials([
        string(credentialsId: 'WEBEX_TOKEN', variable: 'WEBEX_BOT_TOKEN'),
        string(credentialsId: 'WEBEX_ROOM_ID', variable: 'WEBEX_ROOM_ID')
      ]) {
        sh '''
          set -euxo pipefail
          . ${VENV}/bin/activate
          python scripts/notify_webex.py "$WEBEX_BOT_TOKEN" "$WEBEX_ROOM_ID" "❌ Build ${JOB_NAME} #${BUILD_NUMBER} *FAILED* on branch ${BRANCH_NAME:-unknown} (commit $(git rev-parse --short HEAD)). Check console: ${BUILD_URL}console"
        '''
      }
=======
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
>>>>>>> 0a06da347926d392404c22a6705d09e93790b92a
    }
  }
}
