oshino-statsd
=====================
Agent for collecting statsd metrics

For more info, refer to parent project [Oshino](https://github.com/CodersOfTheNight/oshino)

Installing
==========
`pip install oshino-statsd`

Add agent to configuration:
```yaml
module: oshino_statsd.agent.StatsdAgent
```

Config
======
- `host` - Host to bind statsd server (default: localhost)
- `port` - Port to bind statsd server (default: 8787)
- `queue-size` - How much metrics to fit in the queue before sending
Example config
--------------
```yaml
---
interval: 10
loglevel: DEBUG
riemann:
  host: localhost
  port: 5555
agents:
  - name: statsd
    module: oshino_statsd.agent.StatsdAgent
    host: localhost
    port: 8787
    queue-size: 10000
    tag: statsd
```
