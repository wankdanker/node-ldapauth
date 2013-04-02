#!/bin/sh

node-gyp configure build && cp build/Release/ldapauth.node ./
