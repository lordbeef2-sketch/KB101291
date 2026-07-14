# NOMAGIC ATTACHMENT: Teamwork Cloud Dashboard.json

- attachment_id: `304002961`
- space_key: `MCS`
- parent_page_id: `304002934`
- parent_page_title: (2026x Refresh1) Automated installation using scripts
- media_type: `application/octet-stream`
- reported_bytes: 307775
- download_url: https://docs.nomagic.com/download/attachments/304002934/Teamwork%20Cloud%20Dashboard.json?version=1&modificationDate=1777452501824&api=v2
- payload_kind: `text-exact`
- downloaded_sha256: `322a46eab20c87f524b8cf67ec33c609c097ffc41c6bf5718fed1e5f7a13397f`

## EXACT ATTACHMENT SOURCE

````json
{
  "__inputs": [
    {
      "name": "DS_TELEGRAF",
      "label": "Telegraf",
      "description": "",
      "type": "datasource",
      "pluginId": "influxdb",
      "pluginName": "InfluxDB"
    },
    {
      "name": "DS_CASSANDRA",
      "label": "Cassandra",
      "description": "",
      "type": "datasource",
      "pluginId": "influxdb",
      "pluginName": "InfluxDB"
    },
    {
      "name": "DS_TEAMWORK_CLOUD",
      "label": "Teamwork Cloud",
      "description": "",
      "type": "datasource",
      "pluginId": "influxdb",
      "pluginName": "InfluxDB"
    }
  ],
  "__requires": [
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "5.2.1"
    },
    {
      "type": "panel",
      "id": "graph",
      "name": "Graph",
      "version": "5.0.0"
    },
    {
      "type": "datasource",
      "id": "influxdb",
      "name": "InfluxDB",
      "version": "5.0.0"
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "gnetId": null,
  "graphTooltip": 0,
  "id": null,
  "iteration": 1636550382326,
  "links": [],
  "panels": [
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 45,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 1
          },
          "id": 1,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "system",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"load1\") FROM \"system\" WHERE \"host\" =~ /^$server$/ AND $timeFilter GROUP BY time($__interval) fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "load1"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "load1"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "load5"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "load5"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "load15"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "load15"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Load",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 8
          },
          "id": 2,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "processes",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "running"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "running"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "total"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "total"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "total_threads"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "threads"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Processes",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 15
          },
          "id": 39,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $m:$col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "cpu",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "usage_user"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "user"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "usage_system"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "sys"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "usage_nice"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "nice"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "usage_idle"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "idle"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "usage_iowait"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "wait"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "CPU Utilization",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "percent",
              "label": "",
              "logBase": 1,
              "max": "100",
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "CPU",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 1
      },
      "id": 46,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "decimals": 2,
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 23
          },
          "id": 3,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 12,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "mem",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "available"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "available"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "System Memory",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "decimals": 2,
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 30
          },
          "id": 4,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 12,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $2 $3",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "jvm.memory.heap.used",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $2 $3",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "jvm.memory.non-heap.used",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Cassandra JVM Memory",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 37
          },
          "id": 44,
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": true,
            "show": true,
            "sortDesc": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/time/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host.$1.$2.$3",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvm.gc.ConcurrentMarkSweep.count",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"jvm.gc.ConcurrentMarkSweep.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host.$1.$2.$3",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvm.gc.ParNew.count",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"jvm.gc.ConcurrentMarkSweep.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host.$1.$2.$3",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvm.gc.ConcurrentMarkSweep.time",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"jvm.gc.ConcurrentMarkSweep.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  },
                  {
                    "params": [
                      "30s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host.$1.$2.$3",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvm.gc.ParNew.time",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT max(\"value\") FROM \"jvm.gc.ParNew.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  },
                  {
                    "params": [
                      "30s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Cassandra Garbage Collection",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "ms",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "decimals": 2,
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 44
          },
          "id": 36,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvmMemory",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"HeapMemoryUsage_used\") AS \"heap used\" FROM \"jvmMemory\" WHERE (\"host\" =~ /^$server$/ AND \"attributeName\" = 'HeapMemoryUsage') AND $timeFilter GROUP BY time($__interval), \"host\"",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "HeapMemoryUsage_used"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "heap used"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "attributeName",
                  "operator": "=",
                  "value": "HeapMemoryUsage"
                }
              ]
            },
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvmMemory",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"NonHeapMemoryUsage_used\") AS \"non-heap used\" FROM \"jvmMemory\" WHERE (\"host\" =~ /^$server$/ AND \"attributeName\" = 'NonHeapMemoryUsage') AND $timeFilter GROUP BY time($__interval), \"host\" fill(previous)",
              "rawQuery": false,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "NonHeapMemoryUsage_used"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "non-heap used"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "attributeName",
                  "operator": "=",
                  "value": "NonHeapMemoryUsage"
                }
              ]
            },
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "jvmMemory",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"used\") AS \"heap used\" FROM \"jvmMemory\" WHERE (\"host\" =~ /^$server$/ AND \"attributeName\" = 'HeapMemoryUsage') AND $timeFilter GROUP BY time($__interval), \"host\" fill(previous)",
              "rawQuery": false,
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "used"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "heap used"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "attributeName",
                  "operator": "=",
                  "value": "HeapMemoryUsage"
                }
              ]
            },
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "jvmMemory",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"used\") AS \"heap used\" FROM \"jvmMemory\" WHERE (\"host\" =~ /^$server$/ AND \"attributeName\" = 'NonHeapMemoryUsage') AND $timeFilter GROUP BY time($__interval), \"host\"",
              "rawQuery": false,
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "used"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "heap used"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "attributeName",
                  "operator": "=",
                  "value": "NonHeapMemoryUsage"
                }
              ]
            },
            {
              "alias": "$tag_host: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvmMemory",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"HeapMemoryUsage_used\") AS \"heap used\" FROM \"jvmMemory\" WHERE (\"host\" =~ /^$server$/ AND \"attributeName\" = 'HeapMemoryUsage') AND $timeFilter GROUP BY time($__interval), \"host\"",
              "rawQuery": false,
              "refId": "E",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "HeapMemoryUsage_max"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "heap max"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "attributeName",
                  "operator": "=",
                  "value": "HeapMemoryUsage"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Teamwork Cloud JVM Memory",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 51
          },
          "id": 43,
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": true,
            "show": true,
            "sortDesc": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Time/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host.$tag_typeName.$tag_attributeName",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "typeName"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "attributeName"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvmGC",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "CollectionCount"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "attributeName",
                  "operator": "=",
                  "value": "CollectionCount"
                },
                {
                  "condition": "AND",
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host.$tag_typeName.$tag_attributeName",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "typeName"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "attributeName"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "jvmGC",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "CollectionTime"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  },
                  {
                    "params": [
                      "30s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "attributeName",
                  "operator": "=",
                  "value": "CollectionTime"
                },
                {
                  "condition": "AND",
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Teamwork Cloud Garbage Collection",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "ms",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Memory",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 2
      },
      "id": 47,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 24
          },
          "id": 11,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/in$/",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": true,
          "targets": [
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(max(bytes_recv),1s)*8 as \"in\"  FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), * fill(none)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(max(bytes_sent),1s)*8 as \"out\" FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), * fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Network Usage",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bps",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": true,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 31
          },
          "id": 12,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": false,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/in$/",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(max(packets_recv), 1s) as \"in\" FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), * fill(none)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative( max(packets_sent) ,1s) as \"out\" FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), * fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Network Packets",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "pps",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 38
          },
          "id": 13,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/in$/",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(drop_in), 1s) as \"in\" FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), host,interface fill(none)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(drop_out), 1s) as \"out\" FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), host,interface fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Packets Drop",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "none",
              "label": "Packets dropped",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 45
          },
          "id": 14,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/in$/",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(err_in), 1s) as \"in\" FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), host,interface fill(none)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "$tag_host: $tag_interface: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(err_out), 1s) as \"out\" FROM \"net\" WHERE host =~ /$server/ AND interface =~ /(vlan|eth|bond|ens).*/ AND $timeFilter GROUP BY time($interval), host,interface fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Packets Error",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "none",
              "label": "Packets Error",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Network",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 3
      },
      "id": 48,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 25
          },
          "id": 15,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "sort": null,
            "sortDesc": null,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/read/",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": true,
          "targets": [
            {
              "alias": "$tag_host: $tag_name: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(reads),1s) as \"read\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "$tag_host: $tag_name: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(writes),1s) as \"write\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Disk I/O Requests",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "ops",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 25
          },
          "id": 16,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "show": true,
            "sort": null,
            "sortDesc": null,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/read/",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": true,
          "targets": [
            {
              "alias": "$tag_host: $tag_name: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(read_bytes),1s) as \"read\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "$tag_host: $tag_name: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(write_bytes),1s) as \"write\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Disk I/O Throughput",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "Bps",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 34
          },
          "id": 17,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "show": true,
            "sort": "max",
            "sortDesc": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/read/",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": true,
          "targets": [
            {
              "alias": "$tag_host: $tag_name: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(read_time),1s) as \"read\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "$tag_host: $tag_name: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT non_negative_derivative(mean(write_time),1s)  as \"write\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Disk I/O TIme",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "decimals": null,
              "format": "ms",
              "label": "",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 34
          },
          "id": 18,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "show": true,
            "sort": "max",
            "sortDesc": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": true,
          "targets": [
            {
              "alias": "$tag_host: $tag_name: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(iops_in_progress) as \"iops\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Disk IOPS",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Disk Performance",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 4
      },
      "id": 49,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 26
          },
          "id": 33,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 12,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Percent/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_path: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "path"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "disk",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "used"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "Used"
                    ],
                    "type": "alias"
                  }
                ],
                [
                  {
                    "params": [
                      "used_percent"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "Percent"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "path",
                  "operator": "!=",
                  "value": "/boot"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Storage Utilization",
          "tooltip": {
            "shared": false,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": [
              "total"
            ]
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "percent",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TELEGRAF}",
          "decimals": null,
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 33
          },
          "id": 35,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "sideWidth": null,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Percent/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_path: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "path"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "disk",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"inodes_used\")/mean(\"inodes_total\")*100 AS \"used_percent\" FROM \"disk\" WHERE (\"host\" =~ /^$server$/ AND \"path\" != '/boot') AND $timeFilter GROUP BY time($__interval), \"host\", \"path\" fill(null)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "inodes_used"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "used_percent"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "path",
                  "operator": "!=",
                  "value": "/boot"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Inode Utilization",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "percent",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "percent",
              "label": "",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Disk Utilization",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 5
      },
      "id": 50,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 6
          },
          "id": 19,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 12,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $5",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.LiveSSTableCount.all",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "SSTables",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 6
          },
          "id": 20,
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "org.apache.cassandra.metrics.Compaction.PendingTasks",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Pending Tasks",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": false
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 13
          },
          "id": 21,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 12,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/derivative/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5:$col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "org.apache.cassandra.metrics.Compaction.CompletedTasks",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "1s"
                    ],
                    "type": "non_negative_derivative"
                  },
                  {
                    "params": [
                      "derivative"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5:$col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "org.apache.cassandra.metrics.Compaction.CompletedTasks",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "cumulative"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Completed Tasks",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 13
          },
          "id": 22,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/derivative/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "org.apache.cassandra.metrics.Compaction.BytesCompacted.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "1s"
                    ],
                    "type": "non_negative_derivative"
                  },
                  {
                    "params": [
                      "derivative"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "org.apache.cassandra.metrics.Compaction.BytesCompacted.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "cumulative"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Bytes Compacted",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "bytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 20
          },
          "id": 23,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/derivative/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "org.apache.cassandra.metrics.Compaction.TotalCompactionsCompleted.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "1s"
                    ],
                    "type": "non_negative_derivative"
                  },
                  {
                    "params": [
                      "derivative"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "org.apache.cassandra.metrics.Compaction.TotalCompactionsCompleted.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  },
                  {
                    "params": [
                      "cumulative"
                    ],
                    "type": "alias"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Completed Compactions",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "decimals": 2,
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 20
          },
          "id": 24,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 12,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.SSTablesPerReadHistogram.all.p98",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.SSTablesPerReadHistogram.all.p95",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.SSTablesPerReadHistogram.all.p50",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.SSTablesPerReadHistogram.all.p75",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "SSTables per read histogram",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "decimals": 2,
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 27
          },
          "id": 42,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "sortDesc": false,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.TombstoneScannedHistogram.all.p75",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"org.apache.cassandra.metrics.Table.TombstoneScannedHistogram.esi.Branch.p75\" WHERE \"host\" =~ /^$server$/ AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.TombstoneScannedHistogram.all.p50",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.TombstoneScannedHistogram.all.p95",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Table.TombstoneScannedHistogram.all.p99",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Tombstone Scanned Histogram",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Cassandra Compaction",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 6
      },
      "id": 51,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 28
          },
          "id": 25,
          "legend": {
            "alignAsTable": true,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Capacity|Size/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Cache.Capacity.KeyCache",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Cache.FifteenMinuteHitRate.KeyCache",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Cache.FiveMinuteHitRate.KeyCache",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Cache.OneMinuteHitRate.KeyCache",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Cache.Size.KeyCache",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Cache Hit Rate",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "decimals": 2,
              "format": "none",
              "label": "Hit Rate",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "decimals": 2,
              "format": "bytes",
              "label": "Size",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Cassandra Cache",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 7
      },
      "id": 52,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 29
          },
          "id": 27,
          "interval": "$inter",
          "legend": {
            "alignAsTable": false,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Client.connectedNativeClients",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.Client.connectedThriftClients",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Connected Clients",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 29
          },
          "id": 32,
          "interval": "$inter",
          "legend": {
            "alignAsTable": false,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Timeouts|Failures/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Latency.RangeSlice.p99",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"org.apache.cassandra.metrics.ClientRequest.Latency.Read.count\" WHERE \"host\" =~ /^$server$/ AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Timeouts.RangeSlice.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Failures.RangeSlice.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Range Slice",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 36
          },
          "id": 28,
          "interval": "$inter",
          "legend": {
            "alignAsTable": false,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Timeouts|Failures/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Latency.CASRead.p99",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Timeouts.CASRead.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Failures.CASRead.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "CAS Read",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 36
          },
          "id": 29,
          "interval": "$inter",
          "legend": {
            "alignAsTable": false,
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Timeouts|Failures/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Latency.CASWrite.p99",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Timeouts.CASWrite.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Failures.CASWrite.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "CAS Write",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "decimals": null,
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 43
          },
          "id": 30,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "sideWidth": null,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Timeouts|Failures|count/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Latency.Read.p99",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"org.apache.cassandra.metrics.ClientRequest.Latency.Read.count\" WHERE \"host\" =~ /^$server$/ AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Timeouts.Read.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Failures.Read.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Latency.Read.count",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"org.apache.cassandra.metrics.ClientRequest.Latency.Read.count\" WHERE \"host\" =~ /^$server$/ AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Read",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_CASSANDRA}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 43
          },
          "id": 31,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Timeouts|Failures|count/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Latency.Write.p99",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"org.apache.cassandra.metrics.ClientRequest.Latency.Read.count\" WHERE \"host\" =~ /^$server$/ AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Timeouts.Write.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Failures.Write.count",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "alias": "$tag_host: $4.$5.$6.$7",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "org.apache.cassandra.metrics.ClientRequest.Latency.Write.count",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"org.apache.cassandra.metrics.ClientRequest.Latency.Read.count\" WHERE \"host\" =~ /^$server$/ AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "max"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Write",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Cassandra Client Metrics",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 8
      },
      "id": 53,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 9
          },
          "id": 37,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 24,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "host"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "typeName"
                  ],
                  "type": "tag"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twc\" WHERE (\"objDomain\" = 'TWCloud' AND \"typeName\" = 'type=Metrics,item1=Client,item2=Connection' AND \"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Client,item2=Connection"
                },
                {
                  "condition": "AND",
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Connections",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 16
          },
          "id": 38,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 24,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "repeat": null,
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /ThreadPools*/ AND \"typeName\" =~ /Persistence*/ AND  \"typeName\" =~ /(ActiveTasks|PendingTasks|Blocked)/ AND $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "alias": "",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=serverCoreEventListener,item3=ActiveTasks"
                },
                {
                  "condition": "AND",
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                }
              ]
            },
            {
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": true,
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /ThreadPools*/ AND \"typeName\" =~ /clienthandler*/ AND  \"typeName\" =~ /(ActiveTasks|PendingTasks|Blocked)/ AND $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            },
            {
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /ThreadPools*/ AND \"typeName\" =~ /server*/ AND  \"typeName\" =~ /(ActiveTasks|PendingTasks|Blocked)/ AND $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Thread Pools",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 23
          },
          "id": 40,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 24,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/derivative/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") as cumulative, non_negative_derivative(max(Count),1s) as derivative FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Operation*/ AND  $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Operations",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 30
          },
          "id": 41,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "minSpan": 24,
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Count/",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: Operation: $col",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"50thPercentile\") as p50,  mean(\"99thPercentile\") as p99 FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Operation/ AND $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Latencies",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "ms",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "",
              "logBase": 1,
              "max": null,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "repeat": null,
      "title": "Teamwork Cloud",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 9
      },
      "id": 55,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 10
          },
          "id": 87,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*eObjectDataCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  eObjectData Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 10
          },
          "id": 58,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*eObjectDataCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  eObjectData Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 19
          },
          "id": 71,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*sessionCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  Session Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 19
          },
          "id": 88,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*sessionCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  Session Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 10,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 28
          },
          "id": 57,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*AssigneeInfoAndIDCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  AssigneeInfoAndID Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 28
          },
          "id": 72,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*AssigneeInfoAndIDCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  AssigneeInfoAndID Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 10,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 37
          },
          "id": 59,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*EObjectKeyIndex */ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  EObjectKeyIndex Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 37
          },
          "id": 60,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*EObjectKeyIndex */ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  EObjectKeyIndex Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "kbytes",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 46
          },
          "id": 61,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*branchHierarchyCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  BranchHierarchy Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 46
          },
          "id": 62,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*branchHierarchyCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  BranchHierarchy Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 10,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 55
          },
          "id": 63,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*branchRevisionCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  BranchRevision Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 55
          },
          "id": 64,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*branchRevisionCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  BranchRevision Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 10,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 64
          },
          "id": 65,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*ePackageUriToIdCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  ePackageUriToId Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 64
          },
          "id": 66,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*ePackageUriToIdCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  ePackageUriToId Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 10,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 73
          },
          "id": 67,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*metadataCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  Metadata Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 73
          },
          "id": 68,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*metadataCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  Metadata Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 82
          },
          "id": 69,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*roleCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  Role Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 82
          },
          "id": 70,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": false,
            "hideZero": false,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "previous"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2021x*/  AND \"typeName\" =~ /.*roleCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "Value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "distinct"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=AssigneeInfoAndIDCache,item4=Hit"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "TeamworkCloud  Role Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "transparent": false,
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 10,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "title": "TeamworkCloud Caches",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 10
      },
      "id": 74,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 141
          },
          "id": 76,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*ClientConnectionSynchronizeActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Client Connection Synchronize Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 141
          },
          "id": 77,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*ClientHandlerActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Client Handler Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 150
          },
          "id": 78,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*ClusterHealthActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Cluster Health Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 150
          },
          "id": 86,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*FirstContactActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "First Contact Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 159
          },
          "id": 79,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*LicenseActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "License Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 159
          },
          "id": 80,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*LoginActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Login Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 168
          },
          "id": 85,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*PublisherActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Publisher Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 168
          },
          "id": 84,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*SessionActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Session Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 177
          },
          "id": 82,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*TaskManagerActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Task Manager Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": "${DS_TEAMWORK_CLOUD}",
          "fill": 1,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 177
          },
          "id": 83,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Count\") FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Actors*/  AND \"typeName\" =~ /.*WorkerManagerActor*/ AND  \"typeName\" =~ /(IncomingRequests|ProcessedRequests)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(none)",
              "rawQuery": true,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "mean"
                  }
                ]
              ],
              "tags": []
            }
          ],
          "thresholds": [],
          "timeFrom": null,
          "timeShift": null,
          "title": "Worker Manager Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "buckets": null,
            "mode": "time",
            "name": null,
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ],
          "yaxis": {
            "align": false,
            "alignLevel": null
          }
        }
      ],
      "title": "Teamwork Cloud Actors",
      "type": "row"
    }
  ],
  "refresh": "5s",
  "schemaVersion": 16,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": [
      {
        "allValue": null,
        "current": {},
        "datasource": "${DS_TELEGRAF}",
        "hide": 0,
        "includeAll": true,
        "label": "Server",
        "multi": true,
        "name": "server",
        "options": [],
        "query": "SHOW TAG VALUES FROM \"system\" WITH KEY=host",
        "refresh": 1,
        "regex": "",
        "sort": 1,
        "tagValuesQuery": "",
        "tags": [],
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "auto": true,
        "auto_count": 100,
        "auto_min": "30s",
        "current": {
          "text": "auto",
          "value": "$__auto_interval_inter"
        },
        "hide": 0,
        "label": "Interval",
        "name": "inter",
        "options": [
          {
            "selected": true,
            "text": "auto",
            "value": "$__auto_interval_inter"
          },
          {
            "selected": false,
            "text": "30s",
            "value": "30s"
          },
          {
            "selected": false,
            "text": "1m",
            "value": "1m"
          },
          {
            "selected": false,
            "text": "2m",
            "value": "2m"
          },
          {
            "selected": false,
            "text": "5m",
            "value": "5m"
          },
          {
            "selected": false,
            "text": "10m",
            "value": "10m"
          },
          {
            "selected": false,
            "text": "30m",
            "value": "30m"
          },
          {
            "selected": false,
            "text": "1h",
            "value": "1h"
          }
        ],
        "query": "30s,1m,2m,5m,10m,30m,1h",
        "refresh": 2,
        "type": "interval"
      }
    ]
  },
  "time": {
    "from": "now-1h",
    "to": "now"
  },
  "timepicker": {
    "nowDelay": "",
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ],
    "time_options": [
      "5m",
      "15m",
      "1h",
      "6h",
      "12h",
      "24h",
      "2d",
      "7d",
      "30d"
    ]
  },
  "timezone": "",
  "title": "Teamwork Cloud Dashboard",
  "uid": "dBILY1Gmk",
  "version": 33
}
````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "304002961",
  "type": "attachment",
  "status": "current",
  "title": "Teamwork Cloud Dashboard.json",
  "version": {
    "by": {
      "type": "known",
      "username": "jse21",
      "userKey": "2c9f81f87be2b373017e241b5e8b0001",
      "profilePicture": {
        "path": "/download/attachments/85767822/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Jonė Š.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=2c9f81f87be2b373017e241b5e8b0001"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2026-04-29T10:48:21.824+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/304002961/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/304002961"
    }
  },
  "position": -1,
  "container": {
    "id": "304002934",
    "type": "page",
    "status": "current",
    "title": "(2026x Refresh1) Automated installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS/pages/304002934/2026x+Refresh1+Automated+installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=304002934",
      "tinyui": "/x/drceEg",
      "self": "https://docs.nomagic.com/rest/api/content/304002934"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/304002934/child",
      "restrictions": "/rest/api/content/304002934/restriction/byOperation",
      "history": "/rest/api/content/304002934/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/304002934/descendant",
      "space": "/rest/api/space/MCS",
      "relevantViewRestrictions": "/rest/api/content/304002934/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/octet-stream"
  },
  "extensions": {
    "mediaType": "application/octet-stream",
    "fileSize": 307775,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/304002934/Teamwork%20Cloud%20Dashboard.json?version=1&modificationDate=1777452501824&api=v2",
    "webui": "/spaces/MCS/pages/304002934/2026x+Refresh1+Automated+installation+using+scripts?preview=%2F304002934%2F304002961%2FTeamwork+Cloud+Dashboard.json",
    "self": "https://docs.nomagic.com/rest/api/content/304002961"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/304002961/child",
    "restrictions": "/rest/api/content/304002961/restriction/byOperation",
    "history": "/rest/api/content/304002961/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/304002961/descendant",
    "space": "/rest/api/space/MCS",
    "relevantViewRestrictions": "/rest/api/content/304002961/restriction/relevantViewRestrictions"
  }
}
````
