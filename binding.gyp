{
  "targets": [
    {
      "target_name": "ldapauth",
      "sources": [ "ldapauth.cc" ],
      'include_dirs': [ 
        '/usr/local/include'
      ],
      'defines': [
        'LDAP_DEPRECATED'
      ],
      'cflags': [
        '-Wall',
        '-g'
      ],
      'libraries': [
        '-llber -lldap'
      ],
      'ldflags': [
        '-L/usr/local/lib'
      ],
      'conditions': [
        ['OS=="linux"', {
            'ldflags': [
              '-luuid'
            ]
          }
        ],
        ['OS=="mac"', {
          "link_settings": {
            "libraries": [
              "-lldap"
            ]
          }
         }
        ]
      ]   
    }
  ]
}
