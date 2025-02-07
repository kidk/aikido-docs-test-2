# Aikido never stores your code

> In short: Aikido does not store your code after analysis has taken place. Some of the analysis jobs such as SAST or Secrets Detection require a git clone operation. Below we talk about the technical measures we take to ensure your code is protected:

- We perform different actions such as git clones in a fresh docker container for each repository. After analysis, the data is wiped and the docker container is terminated.
- For GitHub, no refresh or access tokens are ever stored in our database. We use the new GitHub Apps which do not require this. Even a database breach of Aikido itself would not result in your GitHub code being downloadable.
- By default, our integrations require a very minimal read-only scope. Only if you enable special features such as Autofix Pull Requests, Aikido will request write accesses.
- If you want to keep your code completely on-premise, without ever leaving your environment, you can use our [Local Scanner](https://help.aikido.dev/category/aikido-local-scan-setup/sg4xF4OsJciW). The results will seamlessly populate on the Aikido platform. 
- Aikido has SOC2 Type 2 & ISO27001:2022 certification. A report is available [upon request](https://aikido.trust.page/resources). That means we adhere to several organizational and technical policies by default.
- Aikido runs on AWS in the EU-west-1 region in Ireland. That means all processing and storage will stay in that location.

The process we use to ensure code security:

![Image](https://ucarecdn.com/411acc55-32e2-4db5-88e5-c26b0896eb7a/)