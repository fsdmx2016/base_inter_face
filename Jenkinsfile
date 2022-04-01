pipeline{
    agent{
    label:'agent2'}
    stages('build'){
        steps{
        sh 'pip install -r requirments.txt'}

    }
     stages('test'){
        steps{
        sh 'python3 main.py '}

    }
}