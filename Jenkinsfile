#!groovy

properties([disableConcurrentBuilds()])

pipeline {
    agent { label 'pkles-gt0012105-pd15 || pkles-gt0012100-pd15 || pkles-gt0012102-pd15 || pkles-gt0012098-pd15 || pkles-gt0012099-pd15' }
    options {
        buildDiscarder(logRotator(numToKeepStr: "30", artifactNumToKeepStr: "30"))
        timestamps()
        ansiColor("xterm")
    }

    environment {
        PYTHONWARNINGS = "ignore:Unverified HTTPS request"
        DG = credentials("DG")
        DG_URL = "https://cmdb.gos-tech.xyz/rest/"
        DG_MONGODB = credentials("DG_MONGODB")
        DG_MONGODB_HOST = "p-infra-internallb.common.novalocal:27017/cmdb"
        REGISTRY =  "https://base.sw.sbc.space/"
        IMAGE =  "pid/pid_registry/datagerry-cmdb/datagerry-cmdb:0.0.3"
        REGISTRY_CRED = "tuz_pid_pidefs"
        MONGO_DB =  "p-infra-internallb.common.novalocal:172.26.106.3"
    }
    stages {
        stage("Update CMDB Info Portal-PD15") {
            environment {
                PORTAL_URL = "https://portal.gos.sbercloud.dev"
                K8S_METRICS = "http://p-infra-internallb.common.novalocal:8481/select/1/prometheus/api/v1/query?query=sum%20(kube_resourcequota)%20by%20(monitor%2C%20namespace%2C%20cluster%2C%20resource%2C%20type);http://vm_select.pd15.admin.gtp:8481/select/1/prometheus/api/v1/query?query=sum%20(kube_resourcequota)%20by%20(monitor%2C%20namespace%2C%20cluster%2C%20resource%2C%20type)"
                APP_VERSIONS = "http://infra-jenkinsslave-04.pd15.admin.gtp:5002/versions-pd15"
                PORTAL_TOKEN = credentials("PORTAL_TOKEN")
            }
            agent {
                docker {
                    registryUrl REGISTRY
                    image IMAGE
                    registryCredentialsId REGISTRY_CRED
                    args "-u root --privileged --add-host $MONGO_DB"
                    reuseNode true
                }
            }
            steps {
                catchError(buildResult: "SUCCESS", stageResult: "FAILURE") {
                    sh "./main.py PD15"
                }
            }
        }
/*
        stage("Update CMDB Info Portal-PD20") {
            environment {
                PORTAL_URL_PD20 = "https://portal.pd20.gtp"
                OS_METRICS_PD20 = "http://infra-victoriametrics-01.pd20.common.gtp:8428/api/v1/query?query=sum%20(kube_resourcequota)%20by%20(monitor%2C%20namespace%2C%20cluster%2C%20resource%2C%20type)"
                APP_VERSIONS_PD20 = "http://infra-jenkins-01.pd20.common.gtp:5002/versions-pd20"
                PORTAL_TOKEN_PD20 = credentials("PORTAL_TOKEN_PD20")
                FORTI_VPN_HOST = "37.18.109.130:18443"
                FORTI_VPN_CRED = credentials("fortivpn_cred")
            }
            agent {
                docker {
                    registryUrl REGISTRY
                    image IMAGE
                    registryCredentialsId REGISTRY_CRED
                    args "-u root --privileged --add-host $MONGO_DB"
                    reuseNode true
                }
            }
            steps {
                catchError(buildResult: "SUCCESS", stageResult: "FAILURE") {
                    sh "screen -dm openfortivpn $FORTI_VPN_HOST -u $FORTI_VPN_CRED_USR -p '$FORTI_VPN_CRED_PSW' --trusted-cert=0e20fa39ca5240b386ed527c9f10506bd7e996ad179ec555e2a3616f82e7c7e0"
                    sh "sleep 5"
                    sh "./main.py PD20"
               }
           }
       }

        stage("Update CMDB Info Portal-PD23") {
            environment {
                PORTAL_URL_PD23 = "https://portal.pd23.gtp"
                OS_METRICS_PD23 = "http://infra-victoriametrics-01.pd23.common.gtp:8428/api/v1/query?query=sum%20(kube_resourcequota)%20by%20(monitor%2C%20namespace%2C%20cluster%2C%20resource%2C%20type)"
                APP_VERSIONS_PD23 = "http://infra-jenkins-01.pd23.common.gtp:5002/versions-pd23"
                PORTAL_TOKEN_PD23 = credentials("PORTAL_TOKEN_PD23")
                FORTI_VPN_HOST = "2.63.168.132:15443"
                FORTI_VPN_CRED = credentials("fortivpn_cred_pd23")
            }
            agent {
                docker {
                    registryUrl REGISTRY
                    image IMAGE
                    registryCredentialsId REGISTRY_CRED
                    args "-u root --privileged --add-host $MONGO_DB"
                    reuseNode true
                }
            }
            steps {
                catchError(buildResult: "SUCCESS", stageResult: "FAILURE") {
                    sh "screen -dm openfortivpn $FORTI_VPN_HOST -u $FORTI_VPN_CRED_USR -p '$FORTI_VPN_CRED_PSW' --trusted-cert=03d57a4c8e580bd17424283763d7e0da8a844715290f789a056906f7f4654260"
                    sh "sleep 5"
                    sh "./main.py PD23"
                }
            }
        }

        stage("Update CMDB Info Portal-PD24") {
            environment {
                PORTAL_URL_PD24 = "https://portal.pd24.gtp"
//                 OS_METRICS_PD24 = "http://infra-victoriametrics-01.pd24.common.gtp:8428/api/v1/query?query=sum(kube_resourcequota)%20by%20(monitor,%20namespace,%20cluster,%20resource,%20type)"
                OS_METRICS_PD24 = "http://infra-victoriametrics-01.pd24.common.gtp:8428/api/v1/query?query=sum%20(kube_resourcequota)%20by%20(monitor%2C%20namespace%2C%20cluster%2C%20resource%2C%20type)"
                APP_VERSIONS_PD24 = "http://infra-jenkinsslave-alt-01.pd24.common.gtp:5002/versions-pd24"
                PORTAL_TOKEN_PD24 = credentials("PORTAL_TOKEN_PD24")
                FORTI_VPN_HOST = "2.63.137.212:15443"
                FORTI_VPN_CRED = credentials("fortivpn_cred_pd24")
            }
            agent {
                docker {
                    registryUrl REGISTRY
                    image IMAGE
                    registryCredentialsId REGISTRY_CRED
                    args "-u root --privileged --add-host $MONGO_DB"
                    reuseNode true
                }
            }
            steps {
                catchError(buildResult: "SUCCESS", stageResult: "FAILURE") {
                    sh "screen -dm openfortivpn $FORTI_VPN_HOST -u $FORTI_VPN_CRED_USR -p '$FORTI_VPN_CRED_PSW' --trusted-cert=36fd0c49c63b3bda068fec30c751291cd498376a523c0a1b5f47252fe8798670"
                    sh "sleep 5"
                    sh "./main.py PD24"
                }
            }
        }
*/
/*
        stage("Update visible settings") {
            agent {
                docker {
                    registryUrl REGISTRY
                    image IMAGE
                    registryCredentialsId REGISTRY_CRED
                    args "-u root --privileged --add-host $MONGO_DB"
                    reuseNode true
                }
            }
            steps {
                    sh "./view_settings.py"
            }
        }
*/
    }
}