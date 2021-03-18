```
$ poetry install
$ poetry run python foo.py
{"message": "hello", "context_id": "e3b8c5b0-1586-4b4e-b49c-97e5757e04cb"}
{"message": "foo"}
```

next version

```
$ poetry run python bar.py 2>&1 | jq ".record.message,.record.extra"
"main"
{}
"logging out"
{}
"logging.logger out"
{}
"logging out"
{}
"logging.logger out"
{}
"logging out with-in context"
{
  "context": "dummy"
}
"logging.logger out with-in context"
{
  "context": "dummy"
}
"logging out"
{
  "context": "2c32c76f-41c9-4bc5-9f3e-11215025b78c"
}
"logging.logger out"
{
  "context": "2c32c76f-41c9-4bc5-9f3e-11215025b78c"
}
"logging out with-in context"
{
  "context": "dummy2"
}
"logging.logger out with-in context"
{
  "context": "dummy2"
}
"logging out with-in context"
{
  "context": "2c32c76f-41c9-4bc5-9f3e-11215025b78c",
  "another_context": "dummy_another"
}
"logging.logger out with-in context"
{
  "context": "2c32c76f-41c9-4bc5-9f3e-11215025b78c",
  "another_context": "dummy_another"
}
"logging out"
{
  "context": "2c32c76f-41c9-4bc5-9f3e-11215025b78c"
}
"logging.logger out"
{
  "context": "2c32c76f-41c9-4bc5-9f3e-11215025b78c"
}
"logging out"
{}
"logging.logger out"
{}
```
