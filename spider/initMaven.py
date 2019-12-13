#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import sys


def initMaven(mvn, url):
    child = subprocess.Popen(mvn, shell=True, cwd=url, stdout=subprocess.PIPE)
    return child.stdout.read()


def getResult(mvn, url):
    if mvn is None or mvn.strip() == "":
        mvn = "mvn archetype:generate -DgroupId=com.spdb -DartifactId=test -DpackageName=com.spdb " \
              "-Dversion=0.0.1-SNAPSHOT -DapplicationName=component -DarchetypeArtifactId=maven-archetype-webapp " \
              "-DinteractiveMode=false "
    return initMaven(mvn, url)


if __name__ == '__main__':
    url = sys.argv[1]
    groupId = sys.argv[2]
    artifactId = sys.argv[3]
    applicationName = sys.argv[4]

    mvn = "mvn archetype:generate -DgroupId=" + groupId \
          + " -DartifactId=" + artifactId \
          + " -DpackageName=com.spdb -Dversion=0.0.1-SNAPSHOT" \
            " -DapplicationName=" + applicationName \
          + " -DarchetypeArtifactId=maven-archetype-webapp " \
            "-DinteractiveMode=false "
    print(mvn)
    if url is not None and groupId is not None and artifactId is not None and applicationName is not None:
        result = getResult(mvn, url)
        print(result)
