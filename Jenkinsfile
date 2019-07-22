pipeline {
	agent any 
	stages	{
		stage("Git checkout")
		{
			steps {
				git clone https://github.com/eldo26/tc-demo.git
			}
		}
		stage("Run Playbook")
		{
			steps {
				ansible-playbook site.yaml -v
			}
		}

	}
}