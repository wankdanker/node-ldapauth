{
	'targets' : [
		{
			'target_name' : 'ldapauth',
			'sources' : [ 
				'ldapauth.cc'
			],
			'defines' : [
				  'LDAP_DEPRECATED'
			],
			'conditions' : [
				[ 'OS == "linux"', {
					'libraries' : [ 
						'-lldap' 
					]
				}],
				[ 'OS == "mac"', {
					'libraries' : [ 
						'-lldap' 
					]
				}]
			]
		}
	]
}
