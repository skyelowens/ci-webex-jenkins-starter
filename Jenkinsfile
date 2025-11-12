pipeline {
  agent any
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
    }
  }
}
