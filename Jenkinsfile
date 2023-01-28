pipeline {
    agent any

    stages 
    {
        stage('Hello')
        {
            steps 
            {
                echo 'Hello World'
            }
        }
        stage('build')
        {
            steps 
            {
                echo 'this is build'
            }
        }
        stage('test')
        {
            steps 
            {
                echo 'this is test'
            }
        }
        stage('deploy')
        {
            steps 
            {
                echo 'this is deploy'
            }
        }
       
    }
     post
        {
            always
            {
                emailext body: 'summary', replyTo: 'varshithashetty03@gmail.com', subject: 'pipe notify ', to: 'varshithashetty03@gmail.com'
            }
        }
}
