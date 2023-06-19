
# EDCS - eTora Voting System AWS Infrastructure

---

| Project Description                                      |
|---------------------------------------------------------|
| **Author:** Bruno Axel Kamere                                   |
| **Supervisor:** Daczuk Victor                                   |
| **Course:** Distributed Computing Systems (103B-CSCSN-MSA-EDCS)  |
| **University:** Warsaw University of Technology  |
| **Faculty:** Faculty of Electronics and Information Technology  |
| **Programme:** Master of Science in Computer Science and Networks (Msc. CSN)  |
| **Project Title:**  eTora Voting System AWS Infrastructure|
| **Project Implementation Period:** Summer Semester 2022/2023                    |
| **Description:**                                         |
| Add proper description |
| **Key Features:**                                        |
| - Feature 1          |
| **Objectives:**                                          |
| - Objective a |
| **Expected Outcome:**                                    |
| What is the expected outcome? |

---

This is a project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation

Enjoy!
