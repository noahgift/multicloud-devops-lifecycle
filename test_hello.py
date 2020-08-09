from click.testing import CliRunner
from hello import callapi


def test_callapi():
  runner = CliRunner()
  result = runner.invoke(callapi, ['--key', '1234', '--phrase', 'bob'])
  assert result.exit_code == 0
  assert 'bob' in result.output