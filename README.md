![alt text](images/Diagrama_solution.png)
# aws-terraform-iac
Este projeto tem como objetivo prover uma fluxo de self service para desenvolvedores que precisam de uma instância do tipo EC2 para desenvolvimento ou validação.

## Requirements on AWS
- [x] [Lambda Function](https://console.aws.amazon.com/lambda/) - com runtime `Python 3.6` e com a função conforme arquivo `AWS/lambda_funtion.py`

- [x] [API Gateway](https://console.aws.amazon.com/apigateway/)  com um método POST configurado linkado ao `Lambda`

- [x] [Dynamo DB](https://console.aws.amazon.com/dynamodb/) - Foi criado uma tabela `infrastructure` com 2 items 

| quantity | reource |
| -------- |:-------:|
|    `1`  |  `ec2` |

## Requirements on Jenkins
- [x] Terraform

- [x] Webhook trigger on Jenkins Pipeline

## Requirements on Dialog flow

