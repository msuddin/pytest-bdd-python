from sample_pytest_bdd_python.hello_world import HelloWorld

from pytest_bdd import given, scenario, then, parsers

helloWorld = HelloWorld("Hi Superman")

@scenario('features/hello_world.feature', 'Hello world should return the correct message')
def test_hello_world_should_return_the_correct_message():
    """Hello world should return the correct message."""

@given(parsers.parse('I create a hello world object with the message "{message:S}"'))
def i_create_a_hello_world_object_with_the_message_hi_batman(message):
    helloWorld.set_message(message)

@then(parsers.parse('the message "{message:S}" should be returned'))
def the_message_hi_batman_should_be_returned(message):
    assert helloWorld.get_message() == message
