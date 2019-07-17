from sample_pytest_bdd_python.hello_world import HelloWorld

test_message = "Hi_batman"
hello_batman = HelloWorld("")

def test_should_set_hello_world_message_correct():
    hello_batman.set_message(test_message)
    assert hello_batman.get_message() == test_message

def test_should_set_hello_world_message_incorrect():
    hello_batman.set_message("Bye_batman")
    assert hello_batman.get_message() == test_message