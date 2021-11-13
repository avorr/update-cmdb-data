#!groovy
//variables from jenkins
properties([disableConcurrentBuilds()])
// agent = env.agent // work agent
// token = env.token // sbercaud token
// stand = env.stand // sbercloud stand
// group = env.group // sbercloud group
// hosts_limit = env.hosts_limit // hosts limit
// keys_repo_url = env.keys_repo_url // url for keys repo
// keys_repo_cred = env.keys_repo_cred // key repository credantials

pipeline {
    agent any
    options {
//         buildDiscarder(logRotator(numToKeepStr: '1', artifactNumToKeepStr: '1'))
        timestamps()
    }

    environment {
        PATH = "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin"
        PORTAL_TOKEN_PD15 = "TEST"
        CMDB_LOGIN = credantials('cmdb-cred')
        CMDB_PASSWORD = "TEST"
        imagename = "datagerry-test"
        registryCredential = 'yenigul-dockerhub'
        dockerImage = ''
    }


    stages {
//         stage("Prepare build image") {
//             steps {
//                 sh "docker build -f Dockerfile . -t datagerry"
//             }
//         }
        stage("Prepare build image") {
            steps {
                script {
                    dockerImage = docker.build imagename
            }

//                 sh "docker build -f Dockerfile . -t datagerry"
            }
        }

        stage("Build project") {
            agent {
                docker {
//                     Dockerfile 'Dockerfile'
                    image "datagerry-test"
                    args "-e CMDB_LOGIN=CMDB_LOGIN"
                    reuseNode true
//                     label "build-image"
                }
            }
            steps {
                sh "python3 -V"
                sh "cat /etc/*-release"
                sh CMDB_LOGIN
            }
        }
    }


//     stages {
//         stage('Build') {
//             agent {
//                 dockerfile {
//                     filename 'Dockerfile'
//                     args '-e CMDB_LOGIN=CMDB_LOGIN'
//                 }
//             }
//             steps {
////                 sh "echo ${env}"
//                 sh "python3 env.py"
//                 sh 'env | grep CMD'
////                 sh "cat /etc/*-release"
//             }
//         }
//     }




}