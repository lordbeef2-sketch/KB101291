# NOMAGIC ATTACHMENT: monitoring-stack_2024xRefresh2.zip

- attachment_id: `218759800`
- space_key: `MCS2024xR2`
- parent_page_id: `218759799`
- parent_page_title: Installation using scripts
- media_type: `application/zip`
- reported_bytes: 55580
- download_url: https://docs.nomagic.com/download/attachments/218759799/monitoring-stack_2024xRefresh2.zip?version=1&modificationDate=1742303747773&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `243357050c07a14c0830d8097132a1a6082ab466a6d026b95ac0eb1e8c208434`

## ARCHIVE CONTENTS

### ENTRY: Monitoring-Node-Install/Grafana-Dashboard.json

- bytes: 396795
- crc32: `ea758275`
- decoded_as: `utf-8`

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
  "__elements": {},
  "__requires": [
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "9.2.10"
    },
    {
      "type": "panel",
      "id": "graph",
      "name": "Graph (old)",
      "version": ""
    },
    {
      "type": "datasource",
      "id": "influxdb",
      "name": "InfluxDB",
      "version": "1.0.0"
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "datasource",
          "uid": "grafana"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": null,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Shows the percent usage of CPU resources over 1 minute, 5 minute, and 15 minute timeframes.\nHigh CPU load can mean the system is busy and might struggle to handle more tasks.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 1
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "System CPU Load",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Percent",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Displays the current number of processes running on the system:\n\nRunning: The processes actively being executed.\nTotal: The overall number of processes, including both active and idle ones.\nThreads: The total number of threads across all processes.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 8
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "Number of running processes",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Number of running processes",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "CPU utilization refers to the percentage of the CPU's total capacity that is being used by different types of system activities. This is broken down into the following categories:\n\ncpu:user: The percentage of CPU time used by user processes (applications and programs running on the system). High user CPU time suggests that applications are consuming significant processing power.\n\ncpu:sys: The percentage of CPU time used by system processes (the operating system's tasks, like handling hardware operations). High system CPU time can indicate that the operating system is handling many background tasks.\n\ncpu:nice: The percentage of CPU time used by processes with a \"nice\" priority (processes that have been given higher or lower priority by the system). This metric is usually low and helps track how much time is spent on prioritized tasks.\n\ncpu:wait: The percentage of CPU time spent waiting for input/output (I/O) operations, such as disk reads or network requests. A high wait time indicates the system is waiting for slower operations, which may cause performance bottlenecks.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 15
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT mean(\"usage_user\") AS \"user\", mean(\"usage_system\") AS \"sys\", mean(\"usage_nice\") AS \"nice\", mean(\"usage_iowait\") AS \"wait\" FROM \"cpu\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
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
          "timeRegions": [],
          "title": "CPU Utilization",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "percent",
              "label": "Percent",
              "logBase": 1,
              "max": "100",
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "CPU",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "decimals": 2,
          "description": "System Memory shows the available RAM  for Teamwork Cloud and/or Cassandra servers. TWC is configured with 8 Gb of RAM by default, as well as using 8GB of ram for Cassandra by default.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 2
          },
          "hiddenSeries": false,
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
          "maxPerRow": 2,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "System Memory",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": "Available system memory",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "decimals": 2,
          "description": "Tracks how much memory is being used by Cassandra’s Java Virtual Machine (JVM). It helps you monitor how well Cassandra is managing its memory.\n\nHeap Used: Memory used by objects in the JVM heap.\nNon-Heap Used: Memory used for internal caches and other non-object data.\nXMX (Max Heap Size): The maximum memory that the JVM can use for its heap.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 9
          },
          "hiddenSeries": false,
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
          "maxPerRow": 2,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
            },
            {
              "alias": "$tag_host: Total Memory",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "jvm.memory.heap.max",
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
                    "type": "last"
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
          "timeRegions": [],
          "title": "Cassandra JVM Memory",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": "Heap/NonHeap used memory and Xmx",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "This metric monitors the performance of the garbage collection (GC) process in Cassandra's JVM. Garbage collection is crucial for reclaiming memory used by objects that are no longer needed. ",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 16
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
            },
            {
              "alias": "$tag_host.$1.$2.$3",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "jvm.gc.G1-Old-Generation.count",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"jvm.gc.ConcurrentMarkSweep.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "E",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "jvm.gc.G1-Young-Generation.count",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"jvm.gc.ConcurrentMarkSweep.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "F",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "jvm.gc.G1-Old-Generation.time",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"jvm.gc.ConcurrentMarkSweep.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "G",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "jvm.gc.G1-Young-Generation.time",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT max(\"value\") FROM \"jvm.gc.ParNew.count\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
              "rawQuery": false,
              "refId": "H",
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
          "timeRegions": [],
          "title": "Cassandra Garbage Collection",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "ms",
              "label": "GC time",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "decimals": 2,
          "description": "Tracks the memory usage of the JVM running Teamwork Cloud. It helps ensure the application is using memory efficiently without performance issues",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 23
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"HeapMemoryUsage_used\") AS \"heap used\" FROM \"jvmMemory\" WHERE (\"host\" =~ /^$server$/ AND \"attributeName\" = 'HeapMemoryUsage') AND $timeFilter GROUP BY time($__interval), \"host\" fill(previous)",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
            },
            {
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "jvmMemory",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "F",
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
                  "key": "attributeName",
                  "operator": "=",
                  "value": "HeapMemoryUsage"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Teamwork Cloud JVM Memory",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": "TWcloud Used Heap and Xmx",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "Monitors garbage collection in the JVM running Teamwork Cloud. Garbage collection is crucial for reclaiming memory used by objects that are no longer needed.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 30
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Teamwork Cloud Garbage Collection",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "ms",
              "label": "GC Time",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Memory",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Shows how much data is being sent and received over the network. It helps you understand if the bottleneck in the performance is a slow interface, or if TWC server is using too much bandwidth, or if the network is performing well.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 3
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "Network Usage",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bps",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": true,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Tracks how many data packets are being sent and received. A high number of packets can indicate heavy network traffic, which might affect performance.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 10
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "Network Packets",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "pps",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Monitors how many network packets are lost during transmission. Packet drops can be caused by congestion, errors, or even a failing network port. All effect the system's ability to communicate properly.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 17
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "Packets Drop",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "none",
              "label": "Packets dropped",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Tracks the number of errors encountered when sending or receiving network packets. Packet errors can signal problems with the network, affecting data transfer and system performance.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 24
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "Packets Error",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "none",
              "label": "Packets Error",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Network",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Shows how many times the system requests data to be read from or written to the disk. Too many I/O requests can slow down the system.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 4
          },
          "hiddenSeries": false,
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
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT non_negative_derivative(mean(reads),1s) as \"read\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m|f)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT non_negative_derivative(mean(writes),1s) as \"write\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m|f)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
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
          "timeRegions": [],
          "title": "Disk I/O Requests",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "ops",
              "label": "Disk read(-) and write (+) operation requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Measures the rate at which data is read from and written to the disk. High throughput indicates heavily load on the system.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 4
          },
          "hiddenSeries": false,
          "id": 16,
          "interval": "$inter",
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "max": true,
            "min": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT non_negative_derivative(mean(read_bytes),1s) as \"read\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m|f)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT non_negative_derivative(mean(write_bytes),1s) as \"write\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m|f)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
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
          "timeRegions": [],
          "title": "Disk I/O Throughput",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "Bps",
              "label": "Disk read(-) and write (+) throughput",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Shows how long the system is waiting for disk read and write operations to finish. Long wait times can indicate disk performance issues.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 13
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT non_negative_derivative(mean(read_time),1s) as \"read\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m|f)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT non_negative_derivative(mean(write_time),1s)  as \"write\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m|f)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
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
          "timeRegions": [],
          "title": "Disk I/O TIme",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "ms",
              "label": "Disk read(-) and write (+) operation time",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Measures how many read and write operations the system performs on the disk per second. High IOPS means the disk is handling many operations, which can affect performance if the disk is overloaded.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 13
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
              "query": "SELECT mean(iops_in_progress) as \"iops\" FROM \"diskio\" WHERE \"host\" =~ /$server$/ AND \"name\" =~ /(v|s|n)(d|v)(a|b|c|d|m|f)((e)[09](n)[0-9])?$/ AND $timeFilter GROUP BY time($interval), *",
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
          "timeRegions": [],
          "title": "Disk IOPS",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Disk input/output operation count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "label": "",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Disk Performance",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Shows how much disk space is being used. High disk usage can slow down the system, so monitoring this ensures there’s enough space for smooth operations.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 5
          },
          "hiddenSeries": false,
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
          "maxPerRow": 2,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "Storage Utilization",
          "tooltip": {
            "shared": false,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": [
              "total"
            ]
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": "Used disk space",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "percent",
              "label": "Utilized Percent",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TELEGRAF}"
          },
          "description": "Monitors how many inodes (data structures that store file information) are being used. Even with free disk space, the system can’t create new files if it runs out of available inodes",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "hiddenSeries": false,
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
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TELEGRAF}"
              },
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
          "timeRegions": [],
          "title": "Inode Utilization",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "percent",
              "label": "Used Percent",
              "logBase": 1,
              "max": "100",
              "min": "0",
              "show": true
            },
            {
              "format": "percent",
              "label": "",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Disk Utilization",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Stored String Tables (sstables) are non-modifiable data files that Cassandra uses for persisting data on disk.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 6
          },
          "hiddenSeries": false,
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
          "maxPerRow": 2,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "SSTables",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Number of SStables",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Pending compactions is the number of compaction tasks that are waiting for a thread to become available.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 6
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Pending Tasks",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Compaction pending task count",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "The number of compaction operations that have finished successfully since the server restarted.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 13
          },
          "hiddenSeries": false,
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
          "maxPerRow": 2,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Completed Tasks",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Completed task count (Cumulative)",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "label": "Completed task count (Derivative)",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Total number of bytes compacted since server [re]start",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 13
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Bytes Compacted",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": "Bytes compacted (Cumulative)",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "bytes",
              "label": "Bytes compacted (Derivative)",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Total number of compactions since server [re]start",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 21
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Completed Compactions",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Completed compactions (Cumulative)",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Completed compactions (Derivative)",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "decimals": 2,
          "description": "Histogram of the number of sstable data files accessed per read",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 21
          },
          "hiddenSeries": false,
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
          "maxPerRow": 2,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "org.apache.cassandra.metrics.Table.SSTablesPerReadHistogram.all.p99",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "SSTables read count per read operation",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "SStables read count",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "decimals": 2,
          "description": "Tombstones scanned in queries on this Keyspace",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 29
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Tombstone Scanned Histogram",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Tombstones scanned per operation",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Cassandra Compaction",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Key cache hit rate for this table.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 7
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "refId": "E",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Cache Hit Rate",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "decimals": 2,
              "format": "none",
              "label": "Hit Rate (0-1)",
              "logBase": 1,
              "max": "1",
              "min": "0",
              "show": true
            },
            {
              "decimals": 2,
              "format": "bytes",
              "label": "Cache Size",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Cassandra Cache",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Number of clients connected to this nodes native protocol server",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 8
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "org.apache.cassandra.metrics.Client.ConnectedNativeClients",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"value\") FROM \"org.apache.cassandra.metrics.Client.ConnectedNativeClients\" WHERE (\"host\" =~ /^$server$/) AND $timeFilter GROUP BY time($__interval), \"host\" fill(null)",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "org.apache.cassandra.metrics.Client.ConnectedThriftClients",
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
              "alias": "$tag_host: $4.$5",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "measurement": "org.apache.cassandra.metrics.Client.ConnectedNativeClients",
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
          "timeRegions": [],
          "title": "Connected Clients",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Number of connections to Cassandra",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Latency for a read request.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 8
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Range Slice",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Transaction read latency",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 15
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "CAS Read",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Transaction write latency",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 15
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "CAS Write",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Read latency for a request.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 22
          },
          "hiddenSeries": false,
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
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Read",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_CASSANDRA}"
          },
          "description": "Write latency for a request.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 22
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_CASSANDRA}"
              },
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
          "timeRegions": [],
          "title": "Write",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "µs",
              "label": "Latency",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Count",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Cassandra Client Metrics",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "The number of connected users to TWC. This correlates to the number of connections in the TWC license.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 9
          },
          "hiddenSeries": false,
          "id": 37,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "$tag_host: $tag_typeName",
              "yaxis": 2
            },
            {
              "alias": "Total Sessions",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Client,item2=Connection"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Active Connections",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Number of active TWC sessions",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Total sessions",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "This the number of connections forked from a primary connection. This does not take away from the total number of connections in a license.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 9
          },
          "hiddenSeries": false,
          "id": 96,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "$tag_host: $tag_typeName",
              "yaxis": 2
            },
            {
              "alias": "Total Sessions",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
                  "value": "type=Metrics,item1=Client,item2=ProxiesIncoming"
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
          "timeRegions": [],
          "title": "Proxy Connections",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Number of active TWC sessions",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Total sessions",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "TWC message handling metrics broken into fail and succeed.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 16
          },
          "hiddenSeries": false,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Operations",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Success Operations",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Failed Operations",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "TWC operation speed. P99 equates to speed that 99% of operations complete, P50 equates to speed that 50% of operations complete.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 23
          },
          "hiddenSeries": false,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "/Count/",
              "yaxis": 2
            },
            {
              "alias": "2022x-twcloud-cluster-600.ec2.nomagic.com24851: Operation: F_p99",
              "yaxis": 2
            },
            {
              "alias": "2022x-twcloud-cluster-600.ec2.nomagic.com24851: Operation: F_p50",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: Operation: $col",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"50thPercentile\") as F_p50,  mean(\"99thPercentile\") as F_p99 FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Operation,item5=Fail/ AND $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(previous)",
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
              "alias": "$tag_host: Operation: $col",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"50thPercentile\") as S_p50,  mean(\"99thPercentile\") as S_p99 FROM \"twc\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Operation,item5=Success/ AND $timeFilter GROUP BY time($__interval), \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "Latencies",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "ms",
              "label": "Success operations latency",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "decimals": 0,
              "format": "ms",
              "label": "Failed operation latency",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Teamwork Cloud",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
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
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "Rate of how much TWC has to reach out to pull data into its cache vice using data in cache.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 10
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*eObjectData*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  eObjectData Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "Size of caches vs number of entries in cache.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 10
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "2022x-twcloud-cluster-600.ec2.nomagic.com24851: type=Metrics,item1=Cache,item2=Persistence-2021x[ec783980-ef07-42cd-ac25-451d304755dc],item3=eObjectDataCache,item4=NumberOfEntries",
              "yaxis": 1
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: $tag_typeName",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*eObjectDataCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": true,
              "refId": "C",
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2022x[ec783980-ef07-42cd-ac25-451d304755dc],item3=eObjectDataCache,item4=Utilization"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "TeamworkCloud  eObjectData Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "bytes",
              "label": "Cache size and used size",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "bytes",
              "label": "Used",
              "logBase": 1,
              "min": "0",
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "TWC cache hit rate and miss rate.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 19
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*sessionCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  Session Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "TWC size of cache vs number of entries in cache.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 19
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*sessionCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  Session Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache size and used size",
              "logBase": 10,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 28
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /.*AssigneeInfoAndIDCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  AssigneeInfoAndID Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 28
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*AssigneeInfoAndIDCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  AssigneeInfoAndID Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache size and used size",
              "logBase": 10,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 37
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*EObjectKeyIndex */ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  eObjectKeyIndex Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 37
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*EObjectKeyIndex */ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  EObjectKeyIndex Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "kbytes",
              "label": "Cache size and used size",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 46
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*branchHierarchyCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  BranchHierarchy Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 46
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*branchHierarchyCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  BranchHierarchy Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache size and used size",
              "logBase": 10,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 55
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*branchRevisionCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  BranchRevision Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 55
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*branchRevisionCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  BranchRevision Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache size and used size",
              "logBase": 10,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 64
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2022x*/  AND \"typeName\" =~ /.*ePackageUriToIdCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": false,
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
                  "value": "type=Metrics,item1=Cache,item2=Persistence,item3=ePackageUriToIdCache,item4=Hit"
                }
              ]
            },
            {
              "alias": "$tag_host: $tag_typeName",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2022x*/  AND \"typeName\" =~ /.*ePackageUriToIdCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": false,
              "refId": "C",
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
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2022x[ec783980-ef07-42cd-ac25-451d304755dc],item3=ePackageUriToIdCache,item4=HitPercent"
                }
              ]
            },
            {
              "alias": "$tag_host: $tag_typeName",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2022x*/  AND \"typeName\" =~ /.*ePackageUriToIdCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
                  "value": "type=Metrics,item1=Cache,item2=Persistence,item3=ePackageUriToIdCache,item4=Miss"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "TeamworkCloud  ePackageUriToId Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 64
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /.*ePackageUriToIdCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  ePackageUriToId Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache size and used size",
              "logBase": 10,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 73
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*metadataCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  Metadata Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 73
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud'  AND \"typeName\" =~ /.*metadataCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  Metadata Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache size and used size",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 82
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
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
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2022x*/  AND \"typeName\" =~ /.*roleCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": false,
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
                  "value": "type=Metrics,item1=Cache,item2=Persistence,item3=roleCache,item4=Hit"
                }
              ]
            },
            {
              "alias": "$tag_host: $tag_typeName",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
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
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2022x*/  AND \"typeName\" =~ /.*roleCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
                  "value": "type=Metrics,item1=Cache,item2=Persistence,item3=roleCache,item4=Miss"
                }
              ]
            },
            {
              "alias": "$tag_host: $tag_typeName",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
              "groupBy": [
                {
                  "params": [
                    "$__interval"
                  ],
                  "type": "time"
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
              "measurement": "twcCacheInt",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence-2022x*/  AND \"typeName\" =~ /.*roleCache*/ AND  \"typeName\" =~ /(Hit|Miss)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
              "rawQuery": false,
              "refId": "C",
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
                  "value": "type=Metrics,item1=Cache,item2=Persistence-2022x[ec783980-ef07-42cd-ac25-451d304755dc],item3=roleCache,item4=Miss"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "TeamworkCloud  Role Cache Hit/Miss",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache Hit/Miss Count",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 82
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "query": "SELECT mean(\"Value\") FROM \"twcCacheInt\" WHERE \"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" =~ /Persistence*/  AND \"typeName\" =~ /.*roleCache*/ AND  \"typeName\" =~ /(MaxEntries|NumberOfEntries)/ AND $timeFilter  GROUP BY time($__interval),  \"host\", \"typeName\" fill(previous)",
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
          "timeRegions": [],
          "title": "TeamworkCloud  Role Cache Size/Used",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Cache size and used size",
              "logBase": 10,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "TeamworkCloud Caches",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 10
      },
      "id": 90,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "Tasks TWC is processing.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 19
          },
          "hiddenSeries": false,
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
            "total": true,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "Active",
              "bars": true
            },
            {
              "alias": "2022x-twcloud-cluster-402.ec2.nomagic.com35079: clienthandler - Active tasks",
              "yaxis": 2
            },
            {
              "alias": "2022x-twcloud-cluster-402.ec2.nomagic.com51933: clienthandler - Active tasks",
              "yaxis": 2
            },
            {
              "alias": "2022x-twcloud-cluster-402.ec2.nomagic.com63912: clienthandler - Active tasks",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: clienthandler - Active tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "E",
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=clienthandler,item3=ActiveTasks"
                }
              ]
            },
            {
              "alias": "$tag_host: clienthandler - Completed tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "F",
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=clienthandler,item3=CompletedTasks"
                }
              ]
            },
            {
              "alias": "$tag_host: clienthandler - Pending tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "G",
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=clienthandler,item3=PendingTasks"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Client Handler Thread Pool",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Active/Pending Tasks",
              "logBase": 10,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Completed Tasks",
              "logBase": 1,
              "min": "0",
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 26
          },
          "hiddenSeries": false,
          "id": 92,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "clienthandler - Completed tasks",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host: Active tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twc\" WHERE (\"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" = 'type=Metrics,item1=ThreadPools,item2=FirstContactActor,item3=ActiveTasks') AND $timeFilter GROUP BY time($__interval) fill(previous)",
              "rawQuery": false,
              "refId": "E",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=FirstContactActor,item3=ActiveTasks"
                }
              ]
            },
            {
              "alias": "$tag_host: Completed tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "F",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=FirstContactActor,item3=CompletedTasks"
                }
              ]
            },
            {
              "alias": "$tag_host: Pending tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "G",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=FirstContactActor,item3=PendingTasks"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "FirstContactActor Thread Pool",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Active/Pending Tasks",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Completed Tasks",
              "logBase": 10,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 33
          },
          "hiddenSeries": false,
          "id": 93,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "clienthandler - Completed tasks",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "EobjectDataKeyGetter - Active tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "E",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=EobjectDataKeyGetter,item3=ActiveTasks"
                }
              ]
            },
            {
              "alias": "EobjectDataKeyGetter - Completed tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "F",
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
                    "type": "count"
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=EobjectDataKeyGetter,item3=CompletedTasks"
                }
              ]
            },
            {
              "alias": "EobjectDataKeyGetter - Pending tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "G",
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
                    "type": "count"
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=EobjectDataKeyGetter,item3=PendingTasks"
                }
              ]
            },
            {
              "alias": "EobjectDataKeyGetter - Blocked tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
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
                    "type": "max"
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=EobjectDataKeyGetter,item3=CurrentlyBlockedThreads"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "EobjectDataKeyGetter Thread Pool",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Active/Pending Tasks",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Completed Tasks",
              "logBase": 10,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 40
          },
          "hiddenSeries": false,
          "id": 91,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "clienthandler - Completed tasks",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "BFS Query - Active tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "E",
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
                    "type": "count"
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=BFSQuery,item3=ActiveTasks"
                }
              ]
            },
            {
              "alias": "BFS Query - Completed tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "F",
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
                    "type": "count"
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=BFSQuery,item3=CompletedTasks"
                }
              ]
            },
            {
              "alias": "BFS Query - Pending tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "G",
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
                    "type": "count"
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=BFSQuery,item3=PendingTasks"
                }
              ]
            },
            {
              "alias": "BFS Query - Blocked tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
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
                    "type": "count"
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
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=BFSQuery,item3=CurrentlyBlockedThreads"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "BFS Query Thread Pool",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Active/Pending Tasks",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Completed Tasks",
              "logBase": 10,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 47
          },
          "hiddenSeries": false,
          "id": 94,
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
          "maxPerRow": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "alias": "clienthandler - Completed tasks",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "$tag_host:  Active tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twc\" WHERE (\"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" = 'type=Metrics,item1=ThreadPools,item2=Persistence-DispatchDeletePool,item3=ActiveTasks') AND $timeFilter GROUP BY time($__interval) fill(previous)",
              "rawQuery": false,
              "refId": "E",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=Persistence-DispatchDeletePool,item3=ActiveTasks"
                }
              ]
            },
            {
              "alias": "$tag_host: Completed tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "query": "SELECT mean(\"Value\") FROM \"twc\" WHERE (\"host\" =~ /^$server$/ AND \"objDomain\" = 'TWCloud' AND \"typeName\" = 'type=Metrics,item1=ThreadPools,item2=Persistence-DispatchDeletePool,item3=CompletedTasks') AND $timeFilter GROUP BY time($__interval) fill(previous)",
              "rawQuery": false,
              "refId": "F",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=Persistence-DispatchDeletePool,item3=PendingTasks"
                }
              ]
            },
            {
              "alias": "$tag_host: Pending tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
              "refId": "G",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=Persistence-DispatchDeletePool,item3=PendingTasks"
                }
              ]
            },
            {
              "alias": "$tag_host: Blocked tasks",
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
              "measurement": "twc",
              "orderByTime": "ASC",
              "policy": "default",
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
                  "key": "host",
                  "operator": "=~",
                  "value": "/^$server$/"
                },
                {
                  "condition": "AND",
                  "key": "objDomain",
                  "operator": "=",
                  "value": "TWCloud"
                },
                {
                  "condition": "AND",
                  "key": "typeName",
                  "operator": "=",
                  "value": "type=Metrics,item1=ThreadPools,item2=Persistence-DispatchDeletePool,item3=CurrentlyBlockedThreads"
                }
              ]
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Persistence-DispatchDeletePool Thread Pool",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Active/Pending Tasks",
              "logBase": 1,
              "min": "0",
              "show": true
            },
            {
              "format": "short",
              "label": "Completed Tasks",
              "logBase": 10,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "TeamworkCloud ThreadPool",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 11
      },
      "id": 74,
      "panels": [
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 12
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Client Connection Synchronize Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "label": "",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "Messages from modeling tool.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 12
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Client Handler Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 21
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Cluster Health Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "description": "Login actor for modeling tool.",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 21
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "First Contact Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 30
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "License Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 30
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Login Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 39
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Publisher Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 39
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Session Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 0,
            "y": 48
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Task Manager Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {},
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "influxdb",
            "uid": "${DS_TEAMWORK_CLOUD}"
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 12,
            "y": 48
          },
          "hiddenSeries": false,
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
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.2.10",
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
              "datasource": {
                "type": "influxdb",
                "uid": "${DS_TEAMWORK_CLOUD}"
              },
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
          "timeRegions": [],
          "title": "Worker Manager Actor",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Incoming/Processed requests",
              "logBase": 1,
              "show": true
            },
            {
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "datasource",
            "uid": "grafana"
          },
          "refId": "A"
        }
      ],
      "title": "Teamwork Cloud Actors",
      "type": "row"
    }
  ],
  "refresh": false,
  "schemaVersion": 37,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {},
        "datasource": {
          "type": "influxdb",
          "uid": "${DS_TELEGRAF}"
        },
        "definition": "",
        "hide": 0,
        "includeAll": true,
        "label": "Server",
        "multi": true,
        "name": "server",
        "options": [],
        "query": "SHOW TAG VALUES FROM \"system\" WITH KEY=host",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 1,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "auto": true,
        "auto_count": 100,
        "auto_min": "30s",
        "current": {
          "selected": false,
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
        "skipUrlSync": false,
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
  "uid": "Dy-6GWcNz",
  "version": 1,
  "weekStart": ""
}
````

### ENTRY: Monitoring-Node-Install/add_twc_monitor.sh

- bytes: 1057
- crc32: `a94032e9`
- decoded_as: `utf-8`

````text
#!/bin/bash
if [ "$EUID" -ne 0 ]; then
	echo "Please run as root or sudo."
	exit 1
fi
if ! [ -f /etc/systemd/system/jmxtrans.service ]; then
	echo "Monitoring stack installation not found." 
	echo "Please add telemetry node from the monitoring stack server/node."
	exit 1
fi
echo "====================================="
echo "Monitoring Stack - Add Telemetry Node"
echo "====================================="
read -e -p "Please enter the hostname of the telemetry node (as obtained via the hostname command):  "  -i ""  TNODE_HOSTNAME
echo "" 
read -e -p "Please enter the IP Address or FQDN of the telemetry node:  "  -i ""  IPADDRESS
echo "" 
JMXFILE=twcloud-$TNODE_HOSTNAME.json
sed -e "s/HOST_NAME/$TNODE_HOSTNAME/g" twcloud.json.template > $JMXFILE
sed -i "s/IP_ADDRESS/$IPADDRESS/g" $JMXFILE
chmod 755 $JMXFILE
if [ -f /var/lib/jmxtrans/$JMXFILE ]; then echo "Replacing current telemetry node profile for $TNODE_HOSTNAME."; fi
\cp -fR $JMXFILE /var/lib/jmxtrans/
systemctl restart jmxtrans
echo ""
echo "Added $TNODE_HOSTNAME telemetry node."
echo ""
````

### ENTRY: Monitoring-Node-Install/createguest.json

- bytes: 92
- crc32: `6e0e6c4f`
- decoded_as: `utf-8`

````json
{
  "name":"guest",
  "email":"guest2@localhost",
  "login":"guest",
  "password":"guest"
}

````

### ENTRY: Monitoring-Node-Install/datasource1.json

- bytes: 353
- crc32: `5f00992d`
- decoded_as: `utf-8`

````json
   {  

      "name":"Cassandra",
      "type":"influxdb",
      "typeLogoUrl":"public/app/plugins/datasource/influxdb/img/influxdb_logo.svg",
      "access":"proxy",
      "url":"http://localhost:8086",
      "password":"",
      "user":"",
      "database":"graphite",
      "basicAuth":false,
      "isDefault":false,
      "jsonData":{  

      }
	}
````

### ENTRY: Monitoring-Node-Install/datasource2.json

- bytes: 354
- crc32: `8160f6a9`
- decoded_as: `utf-8`

````json

   {  
      "name":"Telegraf",
      "type":"influxdb",
      "typeLogoUrl":"public/app/plugins/datasource/influxdb/img/influxdb_logo.svg",
      "access":"proxy",
      "url":"http://localhost:8086",
      "password":"",
      "user":"",
      "database":"telegraf",
      "basicAuth":false,
      "isDefault":false,
      "jsonData":{  

      }
   }
````

### ENTRY: Monitoring-Node-Install/datasource3.json

- bytes: 359
- crc32: `93a36454`
- decoded_as: `utf-8`

````json

   {  
      "name":"Teamwork Cloud",
      "type":"influxdb",
      "typeLogoUrl":"public/app/plugins/datasource/influxdb/img/influxdb_logo.svg",
      "access":"proxy",
      "url":"http://localhost:8086",
      "password":"",
      "user":"",
      "database":"twcloud",
      "basicAuth":false,
      "isDefault":false,
      "jsonData":{  

      }
   }
````

### ENTRY: Monitoring-Node-Install/datasource4.json

- bytes: 352
- crc32: `a1cfb65a`
- decoded_as: `utf-8`

````json
   {  
      "name":"Webapp",
      "type":"influxdb",
      "typeLogoUrl":"public/app/plugins/datasource/influxdb/img/influxdb_logo.svg",
      "access":"proxy",
      "url":"http://localhost:8086",
      "password":"",
      "user":"",
      "database":"webapp",
      "basicAuth":false,
      "isDefault":false,
      "jsonData":{  

      }
   }



````

### ENTRY: Monitoring-Node-Install/influxdb.conf

- bytes: 15952
- crc32: `933d8708`
- decoded_as: `utf-8`

````text
### Welcome to the InfluxDB configuration file.

# The values in this file override the default values used by the system if
# a config option is not specified. The commented out lines are the configuration
# field and the default value used. Uncommenting a line and changing the value
# will change the value used at runtime when the process is restarted.

# Once every 24 hours InfluxDB will report usage data to usage.influxdata.com
# The data includes a random ID, os, arch, version, the number of series and other
# usage data. No data from user databases is ever transmitted.
# Change this option to true to disable reporting.
reporting-disabled = true

# Bind address to use for the RPC service for backup and restore.
# bind-address = "127.0.0.1:8088"

###
### [meta]
###
### Controls the parameters for the Raft consensus group that stores metadata
### about the InfluxDB cluster.
###

[meta]
  # Where the metadata/raft database is stored
  dir = "/var/lib/influxdb/meta"

  # Automatically create a default retention policy when creating a database.
  # retention-autocreate = true

  # If log messages are printed for the meta service
  # logging-enabled = true

###
### [data]
###
### Controls where the actual shard data for InfluxDB lives and how it is
### flushed from the WAL. "dir" may need to be changed to a suitable place
### for your system, but the WAL settings are an advanced configuration. The
### defaults should work for most systems.
###

[data]
  # The directory where the TSM storage engine stores TSM files.
  dir = "/var/lib/influxdb/data"

  # The directory where the TSM storage engine stores WAL files.
  wal-dir = "/var/lib/influxdb/wal"

  # The amount of time that a write will wait before fsyncing.  A duration
  # greater than 0 can be used to batch up multiple fsync calls.  This is useful for slower
  # disks or when WAL write contention is seen.  A value of 0s fsyncs every write to the WAL.
  # Values in the range of 0-100ms are recommended for non-SSD disks.
  # wal-fsync-delay = "0s"


  # The type of shard index to use for new shards.  The default is an in-memory index that is
  # recreated at startup.  A value of "tsi1" will use a disk based index that supports higher
  # cardinality datasets.
  # index-version = "inmem"

  # Trace logging provides more verbose output around the tsm engine. Turning
  # this on can provide more useful output for debugging tsm engine issues.
  # trace-logging-enabled = false

  # Whether queries should be logged before execution. Very useful for troubleshooting, but will
  # log any sensitive data contained within a query.
   query-log-enabled = false

  # Settings for the TSM engine

  # CacheMaxMemorySize is the maximum size a shard's cache can
  # reach before it starts rejecting writes.
  # Valid size suffixes are k, m, or g (case insensitive, 1024 = 1k).
  # Vaues without a size suffix are in bytes.
  # cache-max-memory-size = "1g"

  # CacheSnapshotMemorySize is the size at which the engine will
  # snapshot the cache and write it to a TSM file, freeing up memory
  # Valid size suffixes are k, m, or g (case insensitive, 1024 = 1k).
  # Values without a size suffix are in bytes.
  # cache-snapshot-memory-size = "25m"

  # CacheSnapshotWriteColdDuration is the length of time at
  # which the engine will snapshot the cache and write it to
  # a new TSM file if the shard hasn't received writes or deletes
  # cache-snapshot-write-cold-duration = "10m"

  # CompactFullWriteColdDuration is the duration at which the engine
  # will compact all TSM files in a shard if it hasn't received a
  # write or delete
  # compact-full-write-cold-duration = "4h"

  # The maximum number of concurrent full and level compactions that can run at one time.  A
  # value of 0 results in 50% of runtime.GOMAXPROCS(0) used at runtime.  Any number greater
  # than 0 limits compactions to that value.  This setting does not apply
  # to cache snapshotting.
  # max-concurrent-compactions = 0

  # The maximum series allowed per database before writes are dropped.  This limit can prevent
  # high cardinality issues at the database level.  This limit can be disabled by setting it to
  # 0.
  # max-series-per-database = 1000000

  # The maximum number of tag values per tag that are allowed before writes are dropped.  This limit
  # can prevent high cardinality tag values from being written to a measurement.  This limit can be
  # disabled by setting it to 0.
  # max-values-per-tag = 100000

###
### [coordinator]
###
### Controls the clustering service configuration.
###

[coordinator]
  # The default time a write request will wait until a "timeout" error is returned to the caller.
  # write-timeout = "10s"

  # The maximum number of concurrent queries allowed to be executing at one time.  If a query is
  # executed and exceeds this limit, an error is returned to the caller.  This limit can be disabled
  # by setting it to 0.
  # max-concurrent-queries = 0

  # The maximum time a query will is allowed to execute before being killed by the system.  This limit
  # can help prevent run away queries.  Setting the value to 0 disables the limit.
  # query-timeout = "0s"

  # The time threshold when a query will be logged as a slow query.  This limit can be set to help
  # discover slow or resource intensive queries.  Setting the value to 0 disables the slow query logging.
  # log-queries-after = "0s"

  # The maximum number of points a SELECT can process.  A value of 0 will make
  # the maximum point count unlimited.  This will only be checked every second so queries will not
  # be aborted immediately when hitting the limit.
  # max-select-point = 0

  # The maximum number of series a SELECT can run.  A value of 0 will make the maximum series
  # count unlimited.
  # max-select-series = 0

  # The maxium number of group by time bucket a SELECT can create.  A value of zero will max the maximum
  # number of buckets unlimited.
  # max-select-buckets = 0

###
### [retention]
###
### Controls the enforcement of retention policies for evicting old data.
###

[retention]
  # Determines whether retention policy enforcement enabled.
  # enabled = true

  # The interval of time when retention policy enforcement checks run.
  # check-interval = "30m"

###
### [shard-precreation]
###
### Controls the precreation of shards, so they are available before data arrives.
### Only shards that, after creation, will have both a start- and end-time in the
### future, will ever be created. Shards are never precreated that would be wholly
### or partially in the past.

[shard-precreation]
  # Determines whether shard pre-creation service is enabled.
  # enabled = true

  # The interval of time when the check to pre-create new shards runs.
  # check-interval = "10m"

  # The default period ahead of the endtime of a shard group that its successor
  # group is created.
  # advance-period = "30m"

###
### Controls the system self-monitoring, statistics and diagnostics.
###
### The internal database for monitoring data is created automatically if
### if it does not already exist. The target retention within this database
### is called 'monitor' and is also created with a retention period of 7 days
### and a replication factor of 1, if it does not exist. In all cases the
### this retention policy is configured as the default for the database.

[monitor]
  # Whether to record statistics internally.
  # store-enabled = true

  # The destination database for recorded statistics
  # store-database = "_internal"

  # The interval at which to record statistics
  # store-interval = "10s"

###
### [http]
###
### Controls how the HTTP endpoints are configured. These are the primary
### mechanism for getting data into and out of InfluxDB.
###

[http]
  # Determines whether HTTP endpoint is enabled.
  # enabled = true

  # The bind address used by the HTTP service.
  # bind-address = ":8086"

  # Determines whether user authentication is enabled over HTTP/HTTPS.
  # auth-enabled = false

  # The default realm sent back when issuing a basic auth challenge.
  # realm = "InfluxDB"

  # Determines whether HTTP request logging is enabled.
   log-enabled = false

  # Determines whether detailed write logging is enabled.
  # write-tracing = false

  # Determines whether the pprof endpoint is enabled.  This endpoint is used for
  # troubleshooting and monitoring.
  # pprof-enabled = true

  # Determines whether HTTPS is enabled.
  # https-enabled = false

  # The SSL certificate to use when HTTPS is enabled.
  # https-certificate = "/etc/ssl/influxdb.pem"

  # Use a separate private key location.
  # https-private-key = ""

  # The JWT auth shared secret to validate requests using JSON web tokens.
  # shared-secret = ""

  # The default chunk size for result sets that should be chunked.
  # max-row-limit = 0

  # The maximum number of HTTP connections that may be open at once.  New connections that
  # would exceed this limit are dropped.  Setting this value to 0 disables the limit.
  # max-connection-limit = 0

  # Enable http service over unix domain socket
  # unix-socket-enabled = false

  # The path of the unix domain socket.
  # bind-socket = "/var/run/influxdb.sock"

  # The maximum size of a client request body, in bytes. Setting this value to 0 disables the limit.
  # max-body-size = 25000000


###
### [ifql]
###
### Configures the ifql RPC API.
###

[ifql]
  # Determines whether the RPC service is enabled.
  # enabled = true

  # Determines whether additional logging is enabled.
   log-enabled = false

  # The bind address used by the ifql RPC service.
  # bind-address = ":8082"


###
### [subscriber]
###
### Controls the subscriptions, which can be used to fork a copy of all data
### received by the InfluxDB host.
###

[subscriber]
  # Determines whether the subscriber service is enabled.
  # enabled = true

  # The default timeout for HTTP writes to subscribers.
  # http-timeout = "30s"

  # Allows insecure HTTPS connections to subscribers.  This is useful when testing with self-
  # signed certificates.
  # insecure-skip-verify = false

  # The path to the PEM encoded CA certs file. If the empty string, the default system certs will be used
  # ca-certs = ""

  # The number of writer goroutines processing the write channel.
  # write-concurrency = 40

  # The number of in-flight writes buffered in the write channel.
  # write-buffer-size = 1000


###
### [[graphite]]
###
### Controls one or many listeners for Graphite data.
###

[[graphite]]
  # Determines whether the graphite endpoint is enabled.
   enabled = true
   database = "graphite"
   retention-policy = ""
   bind-address = ":2003"
   protocol = "tcp"
  # consistency-level = "one"

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Batching
  # will buffer points in memory if you have many coming in.

  # Flush if this many points get buffered
  # batch-size = 5000

  # number of batches that may be pending in memory
  # batch-pending = 10

  # Flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "1s"

  # UDP Read buffer size, 0 means OS default. UDP listener will fail if set above OS max.
  # udp-read-buffer = 0

  ### This string joins multiple matching 'measurement' values providing more control over the final measurement name.
  # separator = "."

  ### Default tags that will be added to all metrics.  These can be overridden at the template level
  ### or by tags extracted from metric
  # tags = ["region=us-east", "zone=1c"]

  ### Each template line requires a template pattern.  It can have an optional
  ### filter before the template and separated by spaces.  It can also have optional extra
  ### tags following the template.  Multiple tags should be separated by commas and no spaces
  ### similar to the line protocol format.  There can be only one default template.
  # templates = [
  #   "*.app env.service.resource.measurement",
  #   # Default template
  #   "server.*",
  # ]

  templates = [
      "*.org.apache.* host.measurement*" ,
      "*.*.org.apache.* host.host.measurement*" ,
      "*.*.*.org.apache.* host.host.host.measurement*" ,
      "*.*.*.*.org.apache.* host.host.host.host.measurement*" ,
      "*.jvm.*  host.measurement*",
      "*.*.jvm.*  host.host.measurement*",
      "*.*.*.jvm.*  host.host.host.measurement*",
      "*.*.*.*.jvm.*  host.host.host.host.measurement*",
	]


###
### [collectd]
###
### Controls one or many listeners for collectd data.
###

[[collectd]]
  # enabled = false
  # bind-address = ":25826"
  # database = "collectd"
  # retention-policy = ""
  #
  # The collectd service supports either scanning a directory for multiple types
  # db files, or specifying a single db file.
  # typesdb = "/usr/local/share/collectd"
  #
  # security-level = "none"
  # auth-file = "/etc/collectd/auth_file"

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Batching
  # will buffer points in memory if you have many coming in.

  # Flush if this many points get buffered
  # batch-size = 5000

  # Number of batches that may be pending in memory
  # batch-pending = 10

  # Flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "10s"

  # UDP Read buffer size, 0 means OS default. UDP listener will fail if set above OS max.
  # read-buffer = 0

  # Multi-value plugins can be handled two ways.
  # "split" will parse and store the multi-value plugin data into separate measurements
  # "join" will parse and store the multi-value plugin as a single multi-value measurement.
  # "split" is the default behavior for backward compatability with previous versions of influxdb.
  # parse-multivalue-plugin = "split"
###
### [opentsdb]
###
### Controls one or many listeners for OpenTSDB data.
###

[[opentsdb]]
  # enabled = false
  # bind-address = ":4242"
  # database = "opentsdb"
  # retention-policy = ""
  # consistency-level = "one"
  # tls-enabled = false
  # certificate= "/etc/ssl/influxdb.pem"

  # Log an error for every malformed point.
  # log-point-errors = true

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Only points
  # metrics received over the telnet protocol undergo batching.

  # Flush if this many points get buffered
  # batch-size = 1000

  # Number of batches that may be pending in memory
  # batch-pending = 5

  # Flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "1s"

###
### [[udp]]
###
### Controls the listeners for InfluxDB line protocol data via UDP.
###

[[udp]]
  # enabled = false
  # bind-address = ":8089"
  # database = "udp"
  # retention-policy = ""

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Batching
  # will buffer points in memory if you have many coming in.

  # Flush if this many points get buffered
  # batch-size = 5000

  # Number of batches that may be pending in memory
  # batch-pending = 10

  # Will flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "1s"

  # UDP Read buffer size, 0 means OS default. UDP listener will fail if set above OS max.
  # read-buffer = 0

###
### [continuous_queries]
###
### Controls how continuous queries are run within InfluxDB.
###

[continuous_queries]
  # Determines whether the continuous query service is enabled.
  # enabled = true

  # Controls whether queries are logged when executed by the CQ service.
   log-enabled = false

  # Controls whether queries are logged to the self-monitoring data store.
  # query-stats-enabled = false

  # interval for how often continuous queries will be checked if they need to run
  # run-interval = "1s"

````

### ENTRY: Monitoring-Node-Install/install_monitoring_node.sh

- bytes: 6197
- crc32: `3008fb63`
- decoded_as: `utf-8`

````text
#!/bin/bash
GRAFANA_VER=9.2.10
GRAFANA_URL=https://dl.grafana.com/oss/release/grafana-$GRAFANA_VER-1.x86_64.rpm
JMXTRANS_RPM=jmxtrans-272.rpm
JMXTRANS_URL=https://repo1.maven.org/maven2/org/jmxtrans/jmxtrans/272/$JMXTRANS_RPM

required_files="twcloud.json.template influxdb.conf createguest.json datasource1.json datasource2.json datasource3.json datasource4.json"

function add_influxdb_repo {
    cat <<EOF > /etc/yum.repos.d/influxdata.repo
[influxdata]
name = InfluxData Repository - Stable
baseurl = https://repos.influxdata.com/stable/\$basearch/main
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdata-archive_compat.key
EOF
    sleep 5
}

function create_jmxtrans_service {
    cat <<EOF > /etc/systemd/system/jmxtrans.service
[Unit]
Description=JMX Transformer - more than meets the eye
After=syslog.target network.target

[Service]
Type=forking
User=jmxtrans
Group=jmxtrans
# Run ExecStartPre with root-permissions
PermissionsStartOnly=true
ExecStartPre=-/usr/bin/mkdir /run/jmxtrans/
ExecStartPre=/usr/bin/chown -R jmxtrans:jmxtrans /run/jmxtrans/
PIDFile=/var/run/jmxtrans/jmxtrans.pid
ExecStart=/usr/share/jmxtrans/bin/jmxtrans start

[Install]
WantedBy=multi-user.target
EOF
    sleep 5
}

# Preliminary checks
if [ "$EUID" -ne 0 ]; then
	echo "Please run as root or sudo."
	exit 1
fi
for curr_file in $required_files
do
    if ! [ -f $curr_file ]; then
        echo "Installation terminated. Could not find $curr_file in current installation path."
        exit 1
    fi
done
if command -v hostname &> /dev/null; then
	TNODE_HOSTNAME=$(hostname)
	TNODE_ADDRESS=$(hostname -f)
    MONITORNODE_ADDRESS=$(hostname -f)
else
    TNODE_HOSTNAME=localhost
	TNODE_ADDRESS=127.0.0.1
    MONITORNODE_ADDRESS=127.0.0.1
fi

echo "====================================="
echo "Installing Monitoring Node Components"
echo "====================================="
echo ""
# Specify remote telemtry node. Go with default if telemetry is local. 
echo "Provide the hostname of a telemetry node (press enter to use local hostname found)."
read -e -p "($TNODE_HOSTNAME): "  -i ""  host_entered
TNODE_HOSTNAME=${host_entered:-$TNODE_HOSTNAME}
echo "" 
echo "Provide the IP address or FQDN for $TNODE_HOSTNAME telemetry node (press enter to use the local address found)."
read -e -p "($TNODE_ADDRESS): "  -i ""  address_entered
TNODE_ADDRESS=${address_entered:-$TNODE_ADDRESS}
echo "" 
FWZONE=$(firewall-cmd --get-default-zone)
echo "==================="
echo "Installing InfluxDB"
echo "==================="
echo "Adding InfluxDB yum repo..."
add_influxdb_repo
yum -yq install influxdb
echo "Creating firewall service for InfluxDB"
cat <<EOF > /etc/firewalld/services/influxdb.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>influxdb</short>
    <description>InfluxDB</description>
    <port port="8086" protocol="tcp"/>
    <port port="2003" protocol="tcp"/>
</service>
EOF
sleep 10
firewall-cmd --permanent --zone=$FWZONE --add-service=influxdb

echo "=================="
echo "Installing Grafana"
echo "=================="
yum install -yq $GRAFANA_URL 
echo "Creating firewall service for Grafana"
cat <<EOF > /etc/firewalld/services/grafana.xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
    <short>grafana</short>
    <description>Grafana</description>
    <port port="3000" protocol="tcp"/>
</service>
EOF
sleep 5
echo ""
firewall-cmd --permanent --zone=$FWZONE --add-service=grafana
systemctl enable grafana-server.service

echo "==================="
echo "Installing jmxtrans"
echo "==================="
yum -yq install $JMXTRANS_URL
if type -p chkconfig > /dev/null; then chkconfig --del jmxtrans; fi
# Edit jmxtrans configuration with telemetry node address and hostname.
JMXFILE=twcloud-$TNODE_HOSTNAME.json
sed -e "s/HOST_NAME/$TNODE_HOSTNAME/g" twcloud.json.template > $JMXFILE
sed -i "s/IP_ADDRESS/$TNODE_ADDRESS/g" $JMXFILE
chmod 755 $JMXFILE
\cp -fR $JMXFILE /var/lib/jmxtrans/
sed -i '/wrapper.app.parameter.3/a wrapper.app.parameter.4=-s\nwrapper.app.parameter.5=30\n' /etc/jmxtrans/wrapper.conf
echo "Creating jmxtrans service file..."
create_jmxtrans_service
echo ""
systemctl daemon-reload
echo "Starting InfluxDB Server"
\cp -fR influxdb.conf /etc/influxdb/influxdb.conf
systemctl enable influxdb
systemctl start influxdb
echo "Starting Grafana Server"
systemctl enable grafana-server
systemctl start grafana-server
echo "Starting jmxtrans"
systemctl enable jmxtrans
systemctl start jmxtrans
if systemctl is-active -q firewalld; then
    echo "Reloading firewall rules"
    firewall-cmd --reload
    sleep 5
fi

echo "====================================================="
echo "Initializing InfluxDB databases with 35-day retention"
echo "====================================================="
influx -execute "CREATE DATABASE graphite with duration 35d"
influx -execute "CREATE DATABASE telegraf with duration 35d"
influx -execute "CREATE DATABASE twcloud with duration 35d"  
influx -execute "CREATE DATABASE webapp with duration 35d"  

echo "============================"
echo "Creating Grafana Datasources"
echo "============================"
if ! type curl > /dev/null; then yum install -yq curl; fi
curl -X POST -H "Content-Type: application/json" -d @datasource1.json http://admin:admin@localhost:3000/api/datasources
curl -X POST -H "Content-Type: application/json" -d @datasource2.json http://admin:admin@localhost:3000/api/datasources
curl -X POST -H "Content-Type: application/json" -d @datasource3.json http://admin:admin@localhost:3000/api/datasources 
curl -X POST -H "Content-Type: application/json" -d @datasource4.json http://admin:admin@localhost:3000/api/datasources 
echo ""
echo "==========================="
echo "Creating Grafana Guest User" 
echo "==========================="
curl -X POST -H "Content-Type: application/json" -d @createguest.json http://admin:admin@localhost:3000/api/admin/users/
echo ""
echo ""
echo "Monitoring node installation completed and configured with telemetry node $TNODE_HOSTNAME."
echo ""
echo "Access and set up Grafana dashboard: http://$MONITORNODE_ADDRESS:3000"
echo ""
echo "Run add_twc_monitor.sh to connect to additional telemetry nodes."
echo ""

````

### ENTRY: Monitoring-Node-Install/twcloud.json.template

- bytes: 8760
- crc32: `26a33a51`
- decoded_as: `utf-8`

````text
{
   "servers":[
      {
         "port":"2468",
         "host":"IP_ADDRESS",
         "queries":[
            {
               "obj":"java.lang:type=Memory",
               "attr":[
                  "HeapMemoryUsage",
                  "NonHeapMemoryUsage"
               ],
               "resultAlias":"jvmMemory",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]
            },
            {
               "obj":"java.lang:type=GarbageCollector,*",
               "attr":[
                  "CollectionCount",
                  "CollectionTime"
               ],
               "resultAlias":"jvmGC",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]
            },
            {
               "obj":"TWCloud:type=Internal,item1=Metrics,item2=Actors,*",
               "attr":[
                  "Count",
                  "Value",
                  "50thPercentile",
                  "99thPercentile"
               ],
               "resultAlias":"twc",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]
            },
            {
               "obj":"TWCloud:type=Metrics,item1=Client,*",
               "attr":[
                  "Count",
                  "Value",
                  "50thPercentile",
                  "99thPercentile"
               ],
               "resultAlias":"twc",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]
            },
            {
               "obj":"TWCloud:type=Metrics,item1=Persistence,*",
               "attr":[
                  "Count",
                  "Value",
                  "50thPercentile",
                  "99thPercentile"
               ],
               "resultAlias":"twc",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]       
            },
            {
               "obj":"TWCloud:type=Metrics,item1=ThreadPools,*",  
               "attr":[
                  "Count",
                  "Value",
                  "50thPercentile",
                  "99thPercentile"
               ],
               "resultAlias":"twc",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]
            },
            {
               "obj":"TWCloud:type=Metrics,item1=Cache,*,item4=Hit",
               "attr":[
                  "Count",
                  "Value"
               ],
               "resultAlias":"twcCacheInt",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]       
            },
            {
               "obj":"TWCloud:type=Metrics,item1=Cache,*,item4=MaxEntries",
               "attr":[
                  "Count",
                  "Value"
               ],
               "resultAlias":"twcCacheInt",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]       
            },
            {
               "obj":"TWCloud:type=Metrics,item1=Cache,*,item4=Miss",
               "attr":[
                  "Count",
                  "Value"
               ],
               "resultAlias":"twcCacheInt",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]       
            },
            {
               "obj":"TWCloud:type=Metrics,item1=Cache,*,item4=NumberOfEntries",
               "attr":[
                  "Count",
                  "Value"
               ],
               "resultAlias":"twcCacheInt",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]       
            },
            {
               "obj":"TWCloud:type=Cluster,item1=Hosts,*,item3=ConnectedClients",
               "attr":[
                  "NumberOfClients"
               ],
               "resultAlias":"twc",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]       
            },
            {
               "obj":"TWCloud:type=Cluster,item1=Hosts,*,item3=ActiveClientsIDCount",
               "attr":[
                  "ActiveClients"
               ],
               "resultAlias":"twc",
               "outputWriters":[
                  {
                     "@class":"com.googlecode.jmxtrans.model.output.InfluxDbWriterFactory",
                     "url":"http://127.0.0.1:8086/",
                     "username":"admin",
                     "password":"admin",
                     "database":"twcloud",
                     "tags":{
                        "host":"HOST_NAME"
                     }
                  }
               ]       
            }
            
            
         ]
      }
   ]
}
````

### ENTRY: Telemetry-Node-Install/install_telemetry_node.sh

- bytes: 3564
- crc32: `1f179068`
- decoded_as: `utf-8`

````text
#!/bin/bash
C8_CONF=/etc/cassandra/default.conf
C8_LIB=/usr/share/cassandra/lib/
GRAPHITE_TEMPLATE=metrics-reporter-graphite.yaml.template
TELEGRAF_TEMPLATE=telegraf.conf.template
GRAPHITE_REPO=repo1.maven.org/maven2/io/dropwizard/metrics/metrics-graphite
GRAPHITE_VER=3.1.5

required_files="$GRAPHITE_TEMPLATE $TELEGRAF_TEMPLATE"

function add_influxdb_repo {
    cat <<EOF > /etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - Stable
baseurl = https://repos.influxdata.com/stable/\$basearch/main
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdata-archive_compat.key
EOF
    sleep 5
}

# Preliminary checks
if [ "$EUID" -ne 0 ]; then
	echo "Please run as root or sudo."
	exit 1
fi
for curr_file in $required_files
do
    if ! [ -f $curr_file ]; then
        echo "Installation terminated. Could not find $curr_file in current installation path."
        exit 1
    fi
done

# Obtain node address information
if command -v hostname &> /dev/null; then
	TNODE_HOSTNAME=$(hostname)
	MONITORNODE_ADDRESS=$(hostname -f)
else
	echo "Unable to obtain machine hostname."
	read -p "Enter this machine's hostname: " TNODE_HOSTNAME
	MONITORNODE_ADDRESS=localhost
fi
echo "========================="
echo "Installing Telemetry Node"
echo "========================="
echo ""
# If monitoring stack is remote, specify remote address. Local hostname is obtained automatically.
echo "Provide the full address of the monitoring node (press enter to use the local address found)."
read -e -p "($MONITORNODE_ADDRESS): "  -i "" address_entered
MONITORNODE_ADDRESS=${address_entered:-$MONITORNODE_ADDRESS}
echo ""

echo "==================="
echo "Installing Telegraf"
echo "==================="
echo "Adding yum repo for Telegraf installation..."
add_influxdb_repo
yum -yq install telegraf
# Edit telegraf.conf with monitoring node address.
sed -e "s/HOST_NAME/$MONITORNODE_ADDRESS/g" $TELEGRAF_TEMPLATE > telegraf.conf
\cp -fR telegraf.conf /etc/telegraf/telegraf.conf

# Install Graphite metrics reporter if Cassandra is found
if [ -d $C8_CONF ]; then
	GRAPHITE_JAR=metrics-graphite-$GRAPHITE_VER.jar
	GRAPHITE_YAML=$(basename -s .template $GRAPHITE_TEMPLATE)
	echo "============================================================"
	echo "Setting up metrics-graphite-$GRAPHITE_VER for Cassandra monitoring"
	echo "============================================================"
	wget -c https://$GRAPHITE_REPO/$GRAPHITE_VER/$GRAPHITE_JAR
	if [ -f $GRAPHITE_JAR ]; then
		\cp -fR $GRAPHITE_JAR $C8_LIB/
	else
		echo "Installation terminated. Could not retrieve $GRAPHITE_JAR." && exit 1
	fi
	\cp -fR $C8_CONF/cassandra-env.sh $C8_CONF/cassandra-env.sh.backup
	#Enable Graphite metrics reporter for Cassandra
	cat <<EOF >> $C8_CONF/cassandra-env.sh

# Enable metrics reporting to InfluxDB using the yammer library
METRICS_REPORTER_CFG="$GRAPHITE_YAML"
JVM_OPTS="\$JVM_OPTS -Dcassandra.metricsReporterConfigFile=\$METRICS_REPORTER_CFG"

EOF
	#Update yaml configuration with local hostname and monitoring stack node address. 
	sed -e "s/HOST_NAME/$TNODE_HOSTNAME/g" $GRAPHITE_TEMPLATE > $GRAPHITE_YAML
	sed -i "s/IP/$MONITORNODE_ADDRESS/g" $GRAPHITE_YAML
	\cp -fR $GRAPHITE_YAML $C8_CONF/
	chmod 755 $C8_CONF/$GRAPHITE_YAML
else
	echo "Cassandra not found. Skipping Graphite metrics installation."
fi

yum -yq install net-tools
echo "Starting Telegraf Service"
systemctl start telegraf
echo ""
echo "Telemetry node installation complete for $TNODE_HOSTNAME."
echo "Cassandra must be restarted for telemetry to be sent to the monitoring node"
echo ""

````

### ENTRY: Telemetry-Node-Install/metrics-reporter-graphite.yaml.template

- bytes: 1228
- crc32: `de8f2dec`
- decoded_as: `utf-8`

````text
# For details see:
# * http://wiki.apache.org/cassandra/Metrics
# * https://github.com/addthis/metrics-reporter-config

# This is an example file for configuring which metrics should go
# where.  The sample sends everything to a flat file for humans to
# poke at.  metrics-ganglia or metrics-graphite are more likely to
# operationally useful.

# Some metrics are global for a node (KeyCache capacity) while others
# are broken down by column family or even IP.  The sample list
# includes all of the global metrics via a while list.  To include
# metrics for the system column family for example add
# "^org.apache.cassandra.metrics.ColumnFamily.system.+".


# Start Cassandra with
# -Dcassandra.metricsReporterConfigFile=metrics-reporter-config.yaml
# for this file to be used.  If you are using metrics-ganglia,
# metrics-graphite, or a custom reporter you will also have to add those
# jars to the lib directory.  Nothing in this file can affect
# jmx metrics.


graphite:
  -
    period: 30
    timeunit: 'SECONDS'
    prefix: 'HOST_NAME'
    hosts:
     - host: 'IP'
       port: 2003
    predicate:
      color: 'white'
      useQualifiedName: true
      patterns:
        - '^org.apache.cassandra.+'
        - '^jvm.+'


````

### ENTRY: Telemetry-Node-Install/telegraf.conf.template

- bytes: 95659
- crc32: `3c9f46ee`
- decoded_as: `utf-8`

````text
# Telegraf Configuration
#
# Telegraf is entirely plugin driven. All metrics are gathered from the
# declared inputs, and sent to the declared outputs.
#
# Plugins must be declared in here to be active.
# To deactivate a plugin, comment out the name and any variables.
#
# Use 'telegraf -config telegraf.conf -test' to see what metrics a config
# file would generate.
#
# Environment variables can be used anywhere in this config file, simply prepend
# them with $. For strings the variable must be within quotes (ie, "$STR_VAR"),
# for numbers and booleans they should be plain (ie, $INT_VAR, $BOOL_VAR)


# Global tags can be specified here in key="value" format.
[global_tags]
  # dc = "us-east-1" # will tag all metrics with dc=us-east-1
  # rack = "1a"
  ## Environment variables can be used as tags, and throughout the config file
  # user = "$USER"


# Configuration for telegraf agent
[agent]
  ## Default data collection interval for all inputs
  interval = "10s"
  ## Rounds collection interval to 'interval'
  ## ie, if interval="10s" then always collect on :00, :10, :20, etc.
  round_interval = true

  ## Telegraf will send metrics to outputs in batches of at most
  ## metric_batch_size metrics.
  ## This controls the size of writes that Telegraf sends to output plugins.
  metric_batch_size = 1000

  ## For failed writes, telegraf will cache metric_buffer_limit metrics for each
  ## output, and will flush this buffer on a successful write. Oldest metrics
  ## are dropped first when this buffer fills.
  ## This buffer only fills when writes fail to output plugin(s).
  metric_buffer_limit = 10000

  ## Collection jitter is used to jitter the collection by a random amount.
  ## Each plugin will sleep for a random time within jitter before collecting.
  ## This can be used to avoid many plugins querying things like sysfs at the
  ## same time, which can have a measurable effect on the system.
  collection_jitter = "0s"

  ## Default flushing interval for all outputs. You shouldn't set this below
  ## interval. Maximum flush_interval will be flush_interval + flush_jitter
  flush_interval = "10s"
  ## Jitter the flush interval by a random amount. This is primarily to avoid
  ## large write spikes for users running a large number of telegraf instances.
  ## ie, a jitter of 5s and interval 10s means flushes will happen every 10-15s
  flush_jitter = "0s"

  ## By default or when set to "0s", precision will be set to the same
  ## timestamp order as the collection interval, with the maximum being 1s.
  ##   ie, when interval = "10s", precision will be "1s"
  ##       when interval = "250ms", precision will be "1ms"
  ## Precision will NOT be used for service inputs. It is up to each individual
  ## service input to set the timestamp at the appropriate precision.
  ## Valid time units are "ns", "us" (or "µs"), "ms", "s".
  precision = ""

  ## Logging configuration:
  ## Run telegraf with debug log messages.
  debug = false
  ## Run telegraf in quiet mode (error log messages only).
  quiet = false
  ## Specify the log file name. The empty string means to log to stderr.
  logfile = ""

  ## Override default hostname, if empty use os.Hostname()
  hostname = ""
  ## If set to true, do no set the "host" tag in the telegraf agent.
  omit_hostname = false


###############################################################################
#                            OUTPUT PLUGINS                                   #
###############################################################################

# Configuration for influxdb server to send metrics to
[[outputs.influxdb]]
  ## The HTTP or UDP URL for your InfluxDB instance.  Each item should be
  ## of the form:
  ##   scheme "://" host [ ":" port]
  ##
  ## Multiple urls can be specified as part of the same cluster,
  ## this means that only ONE of the urls will be written to each interval.
  # urls = ["udp://localhost:8089"] # UDP endpoint example
  urls = ["http://HOST_NAME:8086"] # required
  ## The target database for metrics (telegraf will create it if not exists).
  database = "telegraf" # required

  ## Name of existing retention policy to write to.  Empty string writes to
  ## the default retention policy.
  retention_policy = ""
  ## Write consistency (clusters only), can be: "any", "one", "quorum", "all"
  write_consistency = "any"

  ## Write timeout (for the InfluxDB client), formatted as a string.
  ## If not provided, will default to 5s. 0s means no timeout (not recommended).
  timeout = "5s"
  # username = "telegraf"
  # password = "metricsmetricsmetricsmetrics"
  ## Set the user agent for HTTP POSTs (can be useful for log differentiation)
  # user_agent = "telegraf"
  ## Set UDP payload size, defaults to InfluxDB UDP Client default (512 bytes)
  # udp_payload = 512

  ## Optional SSL Config
  # ssl_ca = "/etc/telegraf/ca.pem"
  # ssl_cert = "/etc/telegraf/cert.pem"
  # ssl_key = "/etc/telegraf/key.pem"
  ## Use SSL but skip chain & host verification
  # insecure_skip_verify = false

  ## HTTP Proxy Config
  # http_proxy = "http://corporate.proxy:3128"

  ## Compress each HTTP request payload using GZIP.
  # content_encoding = "gzip"


# # Configuration for Amon Server to send metrics to.
# [[outputs.amon]]
#   ## Amon Server Key
#   server_key = "my-server-key" # required.
#
#   ## Amon Instance URL
#   amon_instance = "https://youramoninstance" # required
#
#   ## Connection timeout.
#   # timeout = "5s"


# # Configuration for the AMQP server to send metrics to
# [[outputs.amqp]]
#   ## AMQP url
#   url = "amqp://localhost:5672/influxdb"
#   ## AMQP exchange
#   exchange = "telegraf"
#   ## Auth method. PLAIN and EXTERNAL are supported
#   ## Using EXTERNAL requires enabling the rabbitmq_auth_mechanism_ssl plugin as
#   ## described here: https://www.rabbitmq.com/plugins.html
#   # auth_method = "PLAIN"
#   ## Telegraf tag to use as a routing key
#   ##  ie, if this tag exists, its value will be used as the routing key
#   routing_tag = "host"
#
#   ## InfluxDB retention policy
#   # retention_policy = "default"
#   ## InfluxDB database
#   # database = "telegraf"
#
#   ## Write timeout, formatted as a string.  If not provided, will default
#   ## to 5s. 0s means no timeout (not recommended).
#   # timeout = "5s"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"


# # Configuration for AWS CloudWatch output.
# [[outputs.cloudwatch]]
#   ## Amazon REGION
#   region = "us-east-1"
#
#   ## Amazon Credentials
#   ## Credentials are loaded in the following order
#   ## 1) Assumed credentials via STS if role_arn is specified
#   ## 2) explicit credentials from 'access_key' and 'secret_key'
#   ## 3) shared profile from 'profile'
#   ## 4) environment variables
#   ## 5) shared credentials file
#   ## 6) EC2 Instance Profile
#   #access_key = ""
#   #secret_key = ""
#   #token = ""
#   #role_arn = ""
#   #profile = ""
#   #shared_credential_file = ""
#
#   ## Namespace for the CloudWatch MetricDatums
#   namespace = "InfluxData/Telegraf"


# # Configuration for DataDog API to send metrics to.
# [[outputs.datadog]]
#   ## Datadog API key
#   apikey = "my-secret-key" # required.
#
#   ## Connection timeout.
#   # timeout = "5s"


# # Send metrics to nowhere at all
# [[outputs.discard]]
#   # no configuration


# # Configuration for Elasticsearch to send metrics to.
# [[outputs.elasticsearch]]
#   ## The full HTTP endpoint URL for your Elasticsearch instance
#   ## Multiple urls can be specified as part of the same cluster,
#   ## this means that only ONE of the urls will be written to each interval.
#   urls = [ "http://node1.es.example.com:9200" ] # required.
#   ## Elasticsearch client timeout, defaults to "5s" if not set.
#   timeout = "5s"
#   ## Set to true to ask Elasticsearch a list of all cluster nodes,
#   ## thus it is not necessary to list all nodes in the urls config option.
#   enable_sniffer = false
#   ## Set the interval to check if the Elasticsearch nodes are available
#   ## Setting to "0s" will disable the health check (not recommended in production)
#   health_check_interval = "10s"
#   ## HTTP basic authentication details (eg. when using Shield)
#   # username = "telegraf"
#   # password = "mypassword"
#
#   ## Index Config
#   ## The target index for metrics (Elasticsearch will create if it not exists).
#   ## You can use the date specifiers below to create indexes per time frame.
#   ## The metric timestamp will be used to decide the destination index name
#   # %Y - year (2016)
#   # %y - last two digits of year (00..99)
#   # %m - month (01..12)
#   # %d - day of month (e.g., 01)
#   # %H - hour (00..23)
#   index_name = "telegraf-%Y.%m.%d" # required.
#
#   ## Template Config
#   ## Set to true if you want telegraf to manage its index template.
#   ## If enabled it will create a recommended index template for telegraf indexes
#   manage_template = true
#   ## The template name used for telegraf indexes
#   template_name = "telegraf"
#   ## Set to true if you want telegraf to overwrite an existing template
#   overwrite_template = false


# # Send telegraf metrics to file(s)
# [[outputs.file]]
#   ## Files to write to, "stdout" is a specially handled file.
#   files = ["stdout", "/tmp/metrics.out"]
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"


# # Configuration for Graphite server to send metrics to
# [[outputs.graphite]]
#   ## TCP endpoint for your graphite instance.
#   ## If multiple endpoints are configured, output will be load balanced.
#   ## Only one of the endpoints will be written to with each iteration.
#   servers = ["localhost:2003"]
#   ## Prefix metrics name
#   prefix = ""
#   ## Graphite output template
#   ## see https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   template = "host.tags.measurement.field"
#   ## timeout in seconds for the write connection to graphite
#   timeout = 2
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Send telegraf metrics to graylog(s)
# [[outputs.graylog]]
#   ## UDP endpoint for your graylog instance.
#   servers = ["127.0.0.1:12201", "192.168.1.1:12201"]


# # Configuration for sending metrics to an Instrumental project
# [[outputs.instrumental]]
#   ## Project API Token (required)
#   api_token = "API Token" # required
#   ## Prefix the metrics with a given name
#   prefix = ""
#   ## Stats output template (Graphite formatting)
#   ## see https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md#graphite
#   template = "host.tags.measurement.field"
#   ## Timeout in seconds to connect
#   timeout = "2s"
#   ## Display Communcation to Instrumental
#   debug = false


# # Configuration for the Kafka server to send metrics to
# [[outputs.kafka]]
#   ## URLs of kafka brokers
#   brokers = ["localhost:9092"]
#   ## Kafka topic for producer messages
#   topic = "telegraf"
#   ## Telegraf tag to use as a routing key
#   ##  ie, if this tag exists, its value will be used as the routing key
#   routing_tag = "host"
#
#   ## CompressionCodec represents the various compression codecs recognized by
#   ## Kafka in messages.
#   ##  0 : No compression
#   ##  1 : Gzip compression
#   ##  2 : Snappy compression
#   compression_codec = 0
#
#   ##  RequiredAcks is used in Produce Requests to tell the broker how many
#   ##  replica acknowledgements it must see before responding
#   ##   0 : the producer never waits for an acknowledgement from the broker.
#   ##       This option provides the lowest latency but the weakest durability
#   ##       guarantees (some data will be lost when a server fails).
#   ##   1 : the producer gets an acknowledgement after the leader replica has
#   ##       received the data. This option provides better durability as the
#   ##       client waits until the server acknowledges the request as successful
#   ##       (only messages that were written to the now-dead leader but not yet
#   ##       replicated will be lost).
#   ##   -1: the producer gets an acknowledgement after all in-sync replicas have
#   ##       received the data. This option provides the best durability, we
#   ##       guarantee that no messages will be lost as long as at least one in
#   ##       sync replica remains.
#   required_acks = -1
#
#   ##  The total number of times to retry sending a message
#   max_retry = 3
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Optional SASL Config
#   # sasl_username = "kafka"
#   # sasl_password = "secret"
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"


# # Configuration for the AWS Kinesis output.
# [[outputs.kinesis]]
#   ## Amazon REGION of kinesis endpoint.
#   region = "ap-southeast-2"
#
#   ## Amazon Credentials
#   ## Credentials are loaded in the following order
#   ## 1) Assumed credentials via STS if role_arn is specified
#   ## 2) explicit credentials from 'access_key' and 'secret_key'
#   ## 3) shared profile from 'profile'
#   ## 4) environment variables
#   ## 5) shared credentials file
#   ## 6) EC2 Instance Profile
#   #access_key = ""
#   #secret_key = ""
#   #token = ""
#   #role_arn = ""
#   #profile = ""
#   #shared_credential_file = ""
#
#   ## Kinesis StreamName must exist prior to starting telegraf.
#   streamname = "StreamName"
#   ## PartitionKey as used for sharding data.
#   partitionkey = "PartitionKey"
#   ## If set the paritionKey will be a random UUID on every put.
#   ## This allows for scaling across multiple shards in a stream.
#   ## This will cause issues with ordering.
#   use_random_partitionkey = false
#
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"
#
#   ## debug will show upstream aws messages.
#   debug = false


# # Configuration for Librato API to send metrics to.
# [[outputs.librato]]
#   ## Librator API Docs
#   ## http://dev.librato.com/v1/metrics-authentication
#   ## Librato API user
#   api_user = "telegraf@influxdb.com" # required.
#   ## Librato API token
#   api_token = "my-secret-token" # required.
#   ## Debug
#   # debug = false
#   ## Connection timeout.
#   # timeout = "5s"
#   ## Output source Template (same as graphite buckets)
#   ## see https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md#graphite
#   ## This template is used in librato's source (not metric's name)
#   template = "host"
#


# # Configuration for MQTT server to send metrics to
# [[outputs.mqtt]]
#   servers = ["localhost:1883"] # required.
#
#   ## MQTT outputs send metrics to this topic format
#   ##    "<topic_prefix>/<hostname>/<pluginname>/"
#   ##   ex: prefix/web01.example.com/mem
#   topic_prefix = "telegraf"
#
#   ## username and password to connect MQTT server.
#   # username = "telegraf"
#   # password = "metricsmetricsmetricsmetrics"
#
#   ## client ID, if not set a random ID is generated
#   # client_id = ""
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"


# # Send telegraf measurements to NATS
# [[outputs.nats]]
#   ## URLs of NATS servers
#   servers = ["nats://localhost:4222"]
#   ## Optional credentials
#   # username = ""
#   # password = ""
#   ## NATS subject for producer messages
#   subject = "telegraf"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"


# # Send telegraf measurements to NSQD
# [[outputs.nsq]]
#   ## Location of nsqd instance listening on TCP
#   server = "localhost:4150"
#   ## NSQ topic for producer messages
#   topic = "telegraf"
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"


# # Configuration for OpenTSDB server to send metrics to
# [[outputs.opentsdb]]
#   ## prefix for metrics keys
#   prefix = "my.specific.prefix."
#
#   ## DNS name of the OpenTSDB server
#   ## Using "opentsdb.example.com" or "tcp://opentsdb.example.com" will use the
#   ## telnet API. "http://opentsdb.example.com" will use the Http API.
#   host = "opentsdb.example.com"
#
#   ## Port of the OpenTSDB server
#   port = 4242
#
#   ## Number of data points to send to OpenTSDB in Http requests.
#   ## Not used with telnet API.
#   httpBatchSize = 50
#
#   ## Debug true - Prints OpenTSDB communication
#   debug = false


# # Configuration for the Prometheus client to spawn
# [[outputs.prometheus_client]]
#   ## Address to listen on
#   # listen = ":9273"
#
#   ## Interval to expire metrics and not deliver to prometheus, 0 == no expiration
#   # expiration_interval = "60s"


# # Configuration for the Riemann server to send metrics to
# [[outputs.riemann]]
#   ## The full TCP or UDP URL of the Riemann server
#   url = "tcp://localhost:5555"
#
#   ## Riemann event TTL, floating-point time in seconds.
#   ## Defines how long that an event is considered valid for in Riemann
#   # ttl = 30.0
#
#   ## Separator to use between measurement and field name in Riemann service name
#   ## This does not have any effect if 'measurement_as_attribute' is set to 'true'
#   separator = "/"
#
#   ## Set measurement name as Riemann attribute 'measurement', instead of prepending it to the Riemann service name
#   # measurement_as_attribute = false
#
#   ## Send string metrics as Riemann event states.
#   ## Unless enabled all string metrics will be ignored
#   # string_as_state = false
#
#   ## A list of tag keys whose values get sent as Riemann tags.
#   ## If empty, all Telegraf tag values will be sent as tags
#   # tag_keys = ["telegraf","custom_tag"]
#
#   ## Additional Riemann tags to send.
#   # tags = ["telegraf-output"]
#
#   ## Description for Riemann event
#   # description_text = "metrics collected from telegraf"
#
#   ## Riemann client write timeout, defaults to "5s" if not set.
#   # timeout = "5s"


# # Configuration for the Riemann server to send metrics to
# [[outputs.riemann_legacy]]
#   ## URL of server
#   url = "localhost:5555"
#   ## transport protocol to use either tcp or udp
#   transport = "tcp"
#   ## separator to use between input name and field name in Riemann service name
#   separator = " "


# # Generic socket writer capable of handling multiple socket types.
# [[outputs.socket_writer]]
#   ## URL to connect to
#   # address = "tcp://127.0.0.1:8094"
#   # address = "tcp://example.com:http"
#   # address = "tcp4://127.0.0.1:8094"
#   # address = "tcp6://127.0.0.1:8094"
#   # address = "tcp6://[2001:db8::1]:8094"
#   # address = "udp://127.0.0.1:8094"
#   # address = "udp4://127.0.0.1:8094"
#   # address = "udp6://127.0.0.1:8094"
#   # address = "unix:///tmp/telegraf.sock"
#   # address = "unixgram:///tmp/telegraf.sock"
#
#   ## Period between keep alive probes.
#   ## Only applies to TCP sockets.
#   ## 0 disables keep alive probes.
#   ## Defaults to the OS configuration.
#   # keep_alive_period = "5m"
#
#   ## Data format to generate.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   # data_format = "influx"



###############################################################################
#                            PROCESSOR PLUGINS                                #
###############################################################################

# # Print all metrics that pass through this filter.
# [[processors.printer]]



###############################################################################
#                            AGGREGATOR PLUGINS                               #
###############################################################################

# # Create aggregate histograms.
# [[aggregators.histogram]]
#   ## The period in which to flush the aggregator.
#   period = "30s"
#
#   ## If true, the original metric will be dropped by the
#   ## aggregator and will not get sent to the output plugins.
#   drop_original = false
#
#   ## Example config that aggregates all fields of the metric.
#   # [[aggregators.histogram.config]]
#   #   ## The set of buckets.
#   #   buckets = [0.0, 15.6, 34.5, 49.1, 71.5, 80.5, 94.5, 100.0]
#   #   ## The name of metric.
#   #   measurement_name = "cpu"
#
#   ## Example config that aggregates only specific fields of the metric.
#   # [[aggregators.histogram.config]]
#   #   ## The set of buckets.
#   #   buckets = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
#   #   ## The name of metric.
#   #   measurement_name = "diskio"
#   #   ## The concrete fields of metric
#   #   fields = ["io_time", "read_time", "write_time"]


# # Keep the aggregate min/max of each metric passing through.
# [[aggregators.minmax]]
#   ## General Aggregator Arguments:
#   ## The period on which to flush & clear the aggregator.
#   period = "30s"
#   ## If true, the original metric will be dropped by the
#   ## aggregator and will not get sent to the output plugins.
#   drop_original = false



###############################################################################
#                            INPUT PLUGINS                                    #
###############################################################################

# Read metrics about cpu usage
[[inputs.cpu]]
  ## Whether to report per-cpu stats or not
  percpu = true
  ## Whether to report total system cpu stats or not
  totalcpu = true
  ## If true, collect raw CPU time metrics.
  collect_cpu_time = false
  ## If true, compute and report the sum of all non-idle CPU states.
  report_active = false


# Read metrics about disk usage by mount point
[[inputs.disk]]
  ## By default, telegraf gather stats for all mountpoints.
  ## Setting mountpoints will restrict the stats to the specified mountpoints.
  # mount_points = ["/"]

  ## Ignore some mountpoints by filesystem type. For example (dev)tmpfs (usually
  ## present on /run, /var/run, /dev/shm or /dev).
  ignore_fs = ["tmpfs", "devtmpfs", "devfs"]


# Read metrics about disk IO by device
[[inputs.diskio]]
  ## By default, telegraf will gather stats for all devices including
  ## disk partitions.
  ## Setting devices will restrict the stats to the specified devices.
  # devices = ["sda", "sdb"]
  ## Uncomment the following line if you need disk serial numbers.
  # skip_serial_number = false
  #
  ## On systems which support it, device metadata can be added in the form of
  ## tags.
  ## Currently only Linux is supported via udev properties. You can view
  ## available properties for a device by running:
  ## 'udevadm info -q property -n /dev/sda'
  # device_tags = ["ID_FS_TYPE", "ID_FS_USAGE"]
  #
  ## Using the same metadata source as device_tags, you can also customize the
  ## name of the device via templates.
  ## The 'name_templates' parameter is a list of templates to try and apply to
  ## the device. The template may contain variables in the form of '$PROPERTY' or
  ## '${PROPERTY}'. The first template which does not contain any variables not
  ## present for the device is used as the device name tag.
  ## The typical use case is for LVM volumes, to get the VG/LV name instead of
  ## the near-meaningless DM-0 name.
  # name_templates = ["$ID_FS_LABEL","$DM_VG_NAME/$DM_LV_NAME"]


# Get kernel statistics from /proc/stat
[[inputs.kernel]]
  # no configuration


# Read metrics about memory usage
[[inputs.mem]]
  # no configuration


# Get the number of processes and group them by status
[[inputs.processes]]
  # no configuration


# Read metrics about swap memory usage
[[inputs.swap]]
  # no configuration


# Read metrics about system load & uptime
[[inputs.system]]
  # no configuration


# # Read stats from aerospike server(s)
# [[inputs.aerospike]]
#   ## Aerospike servers to connect to (with port)
#   ## This plugin will query all namespaces the aerospike
#   ## server has configured and get stats for them.
#   servers = ["localhost:3000"]


# # Read Apache status information (mod_status)
# [[inputs.apache]]
#   ## An array of URLs to gather from, must be directed at the machine
#   ## readable version of the mod_status page including the auto query string.
#   ## Default is "http://localhost/server-status?auto".
#   urls = ["http://localhost/server-status?auto"]
#
#   ## Credentials for basic HTTP authentication.
#   # username = "myuser"
#   # password = "mypassword"
#
#   ## Maximum time to receive response.
#   # response_timeout = "5s"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Read metrics of bcache from stats_total and dirty_data
# [[inputs.bcache]]
#   ## Bcache sets path
#   ## If not specified, then default is:
#   bcachePath = "/sys/fs/bcache"
#
#   ## By default, telegraf gather stats for all bcache devices
#   ## Setting devices will restrict the stats to the specified
#   ## bcache devices.
#   bcacheDevs = ["bcache0"]


# # Read Cassandra metrics through Jolokia
# [[inputs.cassandra]]
#   # This is the context root used to compose the jolokia url
#   context = "/jolokia/read"
#   ## List of cassandra servers exposing jolokia read service
#   servers = ["myuser:mypassword@10.10.10.1:8778","10.10.10.2:8778",":8778"]
#   ## List of metrics collected on above servers
#   ## Each metric consists of a jmx path.
#   ## This will collect all heap memory usage metrics from the jvm and
#   ## ReadLatency metrics for all keyspaces and tables.
#   ## "type=Table" in the query works with Cassandra3.0. Older versions might
#   ## need to use "type=ColumnFamily"
#   metrics  = [
#     "/java.lang:type=Memory/HeapMemoryUsage",
#     "/org.apache.cassandra.metrics:type=Table,keyspace=*,scope=*,name=ReadLatency"
#   ]


# # Collects performance metrics from the MON and OSD nodes in a Ceph storage cluster.
# [[inputs.ceph]]
#   ## This is the recommended interval to poll.  Too frequent and you will lose
#   ## data points due to timeouts during rebalancing and recovery
#   interval = '1m'
#
#   ## All configuration values are optional, defaults are shown below
#
#   ## location of ceph binary
#   ceph_binary = "/usr/bin/ceph"
#
#   ## directory in which to look for socket files
#   socket_dir = "/var/run/ceph"
#
#   ## prefix of MON and OSD socket files, used to determine socket type
#   mon_prefix = "ceph-mon"
#   osd_prefix = "ceph-osd"
#
#   ## suffix used to identify socket files
#   socket_suffix = "asok"
#
#   ## Ceph user to authenticate as
#   ceph_user = "client.admin"
#
#   ## Ceph configuration to use to locate the cluster
#   ceph_config = "/etc/ceph/ceph.conf"
#
#   ## Whether to gather statistics via the admin socket
#   gather_admin_socket_stats = true
#
#   ## Whether to gather statistics via ceph commands
#   gather_cluster_stats = false


# # Read specific statistics per cgroup
# [[inputs.cgroup]]
#   ## Directories in which to look for files, globs are supported.
#   ## Consider restricting paths to the set of cgroups you really
#   ## want to monitor if you have a large number of cgroups, to avoid
#   ## any cardinality issues.
#   # paths = [
#   #   "/cgroup/memory",
#   #   "/cgroup/memory/child1",
#   #   "/cgroup/memory/child2/*",
#   # ]
#   ## cgroup stat fields, as file names, globs are supported.
#   ## these file names are appended to each path from above.
#   # files = ["memory.*usage*", "memory.limit_in_bytes"]


# # Get standard chrony metrics, requires chronyc executable.
# [[inputs.chrony]]
#   ## If true, chronyc tries to perform a DNS lookup for the time server.
#   # dns_lookup = false


# # Pull Metric Statistics from Amazon CloudWatch
# [[inputs.cloudwatch]]
#   ## Amazon Region
#   region = "us-east-1"
#
#   ## Amazon Credentials
#   ## Credentials are loaded in the following order
#   ## 1) Assumed credentials via STS if role_arn is specified
#   ## 2) explicit credentials from 'access_key' and 'secret_key'
#   ## 3) shared profile from 'profile'
#   ## 4) environment variables
#   ## 5) shared credentials file
#   ## 6) EC2 Instance Profile
#   #access_key = ""
#   #secret_key = ""
#   #token = ""
#   #role_arn = ""
#   #profile = ""
#   #shared_credential_file = ""
#
#   # The minimum period for Cloudwatch metrics is 1 minute (60s). However not all
#   # metrics are made available to the 1 minute period. Some are collected at
#   # 3 minute, 5 minute, or larger intervals. See https://aws.amazon.com/cloudwatch/faqs/#monitoring.
#   # Note that if a period is configured that is smaller than the minimum for a
#   # particular metric, that metric will not be returned by the Cloudwatch API
#   # and will not be collected by Telegraf.
#   #
#   ## Requested CloudWatch aggregation Period (required - must be a multiple of 60s)
#   period = "5m"
#
#   ## Collection Delay (required - must account for metrics availability via CloudWatch API)
#   delay = "5m"
#
#   ## Recomended: use metric 'interval' that is a multiple of 'period' to avoid
#   ## gaps or overlap in pulled data
#   interval = "5m"
#
#   ## Configure the TTL for the internal cache of metrics.
#   ## Defaults to 1 hr if not specified
#   #cache_ttl = "10m"
#
#   ## Metric Statistic Namespace (required)
#   namespace = "AWS/ELB"
#
#   ## Maximum requests per second. Note that the global default AWS rate limit is
#   ## 400 reqs/sec, so if you define multiple namespaces, these should add up to a
#   ## maximum of 400. Optional - default value is 200.
#   ## See http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html
#   ratelimit = 200
#
#   ## Metrics to Pull (optional)
#   ## Defaults to all Metrics in Namespace if nothing is provided
#   ## Refreshes Namespace available metrics every 1h
#   #[[inputs.cloudwatch.metrics]]
#   #  names = ["Latency", "RequestCount"]
#   #
#   #  ## Dimension filters for Metric (optional)
#   #  [[inputs.cloudwatch.metrics.dimensions]]
#   #    name = "LoadBalancerName"
#   #    value = "p-example"


# # Collects conntrack stats from the configured directories and files.
# [[inputs.conntrack]]
#    ## The following defaults would work with multiple versions of conntrack.
#    ## Note the nf_ and ip_ filename prefixes are mutually exclusive across
#    ## kernel versions, as are the directory locations.
#
#    ## Superset of filenames to look for within the conntrack dirs.
#    ## Missing files will be ignored.
#    files = ["ip_conntrack_count","ip_conntrack_max",
#             "nf_conntrack_count","nf_conntrack_max"]
#
#    ## Directories to search within for the conntrack files above.
#    ## Missing directrories will be ignored.
#    dirs = ["/proc/sys/net/ipv4/netfilter","/proc/sys/net/netfilter"]


# # Gather health check statuses from services registered in Consul
# [[inputs.consul]]
#   ## Most of these values defaults to the one configured on a Consul's agent level.
#   ## Optional Consul server address (default: "localhost")
#   # address = "localhost"
#   ## Optional URI scheme for the Consul server (default: "http")
#   # scheme = "http"
#   ## Optional ACL token used in every request (default: "")
#   # token = ""
#   ## Optional username used for request HTTP Basic Authentication (default: "")
#   # username = ""
#   ## Optional password used for HTTP Basic Authentication (default: "")
#   # password = ""
#   ## Optional data centre to query the health checks from (default: "")
#   # datacentre = ""


# # Read metrics from one or many couchbase clusters
# [[inputs.couchbase]]
#   ## specify servers via a url matching:
#   ##  [protocol://][:password]@address[:port]
#   ##  e.g.
#   ##    http://couchbase-0.example.com/
#   ##    http://admin:secret@couchbase-0.example.com:8091/
#   ##
#   ## If no servers are specified, then localhost is used as the host.
#   ## If no protocol is specifed, HTTP is used.
#   ## If no port is specified, 8091 is used.
#   servers = ["http://localhost:8091"]


# # Read CouchDB Stats from one or more servers
# [[inputs.couchdb]]
#   ## Works with CouchDB stats endpoints out of the box
#   ## Multiple HOSTs from which to read CouchDB stats:
#   hosts = ["http://localhost:8086/_stats"]


# # Read metrics from one or many disque servers
# [[inputs.disque]]
#   ## An array of URI to gather stats about. Specify an ip or hostname
#   ## with optional port and password.
#   ## ie disque://localhost, disque://10.10.3.33:18832, 10.0.0.1:10000, etc.
#   ## If no servers are specified, then localhost is used as the host.
#   servers = ["localhost"]


# # Provide a native collection for dmsetup based statistics for dm-cache
# [[inputs.dmcache]]
#   ## Whether to report per-device stats or not
#   per_device = true


# # Query given DNS server and gives statistics
# [[inputs.dns_query]]
#   ## servers to query
#   servers = ["8.8.8.8"]
#
#   ## Network is the network protocol name.
#   # network = "udp"
#
#   ## Domains or subdomains to query.
#   # domains = ["."]
#
#   ## Query record type.
#   ## Posible values: A, AAAA, CNAME, MX, NS, PTR, TXT, SOA, SPF, SRV.
#   # record_type = "A"
#
#   ## Dns server port.
#   # port = 53
#
#   ## Query timeout in seconds.
#   # timeout = 2


# # Read metrics about docker containers
# [[inputs.docker]]
#   ## Docker Endpoint
#   ##   To use TCP, set endpoint = "tcp://[ip]:[port]"
#   ##   To use environment variables (ie, docker-machine), set endpoint = "ENV"
#   endpoint = "unix:///var/run/docker.sock"
#
#   ## Only collect metrics for these containers, collect all if empty
#   container_names = []
#
#   ## Containers to include and exclude. Globs accepted.
#   ## Note that an empty array for both will include all containers
#   container_name_include = []
#   container_name_exclude = []
#
#   ## Timeout for docker list, info, and stats commands
#   timeout = "5s"
#
#   ## Whether to report for each container per-device blkio (8:0, 8:1...) and
#   ## network (eth0, eth1, ...) stats or not
#   perdevice = true
#   ## Whether to report for each container total blkio and network stats or not
#   total = false
#   ## Which environment variables should we use as a tag
#   ##tag_env = ["JAVA_HOME", "HEAP_SIZE"]
#
#   ## docker labels to include and exclude as tags.  Globs accepted.
#   ## Note that an empty array for both will include all labels as tags
#   docker_label_include = []
#   docker_label_exclude = []
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Read statistics from one or many dovecot servers
# [[inputs.dovecot]]
#   ## specify dovecot servers via an address:port list
#   ##  e.g.
#   ##    localhost:24242
#   ##
#   ## If no servers are specified, then localhost is used as the host.
#   servers = ["localhost:24242"]
#   ## Type is one of "user", "domain", "ip", or "global"
#   type = "global"
#   ## Wildcard matches like "*.com". An empty string "" is same as "*"
#   ## If type = "ip" filters should be <IP/network>
#   filters = [""]


# # Read stats from one or more Elasticsearch servers or clusters
# [[inputs.elasticsearch]]
#   ## specify a list of one or more Elasticsearch servers
#   # you can add username and password to your url to use basic authentication:
#   # servers = ["http://user:pass@localhost:9200"]
#   servers = ["http://localhost:9200"]
#
#   ## Timeout for HTTP requests to the elastic search server(s)
#   http_timeout = "5s"
#
#   ## When local is true (the default), the node will read only its own stats.
#   ## Set local to false when you want to read the node stats from all nodes
#   ## of the cluster.
#   local = true
#
#   ## Set cluster_health to true when you want to also obtain cluster health stats
#   cluster_health = false
#
#   ## Set cluster_stats to true when you want to also obtain cluster stats from the
#   ## Master node.
#   cluster_stats = false
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Read metrics from one or more commands that can output to stdout
# [[inputs.exec]]
#   ## Commands array
#   commands = [
#     "/tmp/test.sh",
#     "/usr/bin/mycollector --foo=bar",
#     "/tmp/collect_*.sh"
#   ]
#
#   ## Timeout for each command to complete.
#   timeout = "5s"
#
#   ## measurement name suffix (for separating different commands)
#   name_suffix = "_mycollector"
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   data_format = "influx"


# # Read metrics from fail2ban.
# [[inputs.fail2ban]]
#   ## fail2ban-client require root access.
#   ## Setting 'use_sudo' to true will make use of sudo to run fail2ban-client.
#   ## Users must configure sudo to allow telegraf user to run fail2ban-client with no password.
#   ## This plugin run only "fail2ban-client status".
#   use_sudo = false


# # Read stats about given file(s)
# [[inputs.filestat]]
#   ## Files to gather stats about.
#   ## These accept standard unix glob matching rules, but with the addition of
#   ## ** as a "super asterisk". ie:
#   ##   "/var/log/**.log"  -> recursively find all .log files in /var/log
#   ##   "/var/log/*/*.log" -> find all .log files with a parent dir in /var/log
#   ##   "/var/log/apache.log" -> just tail the apache log file
#   ##
#   ## See https://github.com/gobwas/glob for more examples
#   ##
#   files = ["/var/log/**.log"]
#   ## If true, read the entire file and calculate an md5 checksum.
#   md5 = false


# # Read metrics exposed by fluentd in_monitor plugin
# [[inputs.fluentd]]
#   ## This plugin reads information exposed by fluentd (using /api/plugins.json endpoint).
#   ##
#   ## Endpoint:
#   ## - only one URI is allowed
#   ## - https is not supported
#   endpoint = "http://localhost:24220/api/plugins.json"
#   	
#   ## Define which plugins have to be excluded (based on "type" field - e.g. monitor_agent)
#   exclude = [
# 	  "monitor_agent",
# 	  "dummy",
#   ]


# # Read flattened metrics from one or more GrayLog HTTP endpoints
# [[inputs.graylog]]
#   ## API endpoint, currently supported API:
#   ##
#   ##   - multiple  (Ex http://<host>:12900/system/metrics/multiple)
#   ##   - namespace (Ex http://<host>:12900/system/metrics/namespace/{namespace})
#   ##
#   ## For namespace endpoint, the metrics array will be ignored for that call.
#   ## Endpoint can contain namespace and multiple type calls.
#   ##
#   ## Please check http://[graylog-server-ip]:12900/api-browser for full list
#   ## of endpoints
#   servers = [
#     "http://[graylog-server-ip]:12900/system/metrics/multiple",
#   ]
#
#   ## Metrics list
#   ## List of metrics can be found on Graylog webservice documentation.
#   ## Or by hitting the the web service api at:
#   ##   http://[graylog-host]:12900/system/metrics
#   metrics = [
#     "jvm.cl.loaded",
#     "jvm.memory.pools.Metaspace.committed"
#   ]
#
#   ## Username and password
#   username = ""
#   password = ""
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Read metrics of haproxy, via socket or csv stats page
# [[inputs.haproxy]]
#   ## An array of address to gather stats about. Specify an ip on hostname
#   ## with optional port. ie localhost, 10.10.3.33:1936, etc.
#   ## Make sure you specify the complete path to the stats endpoint
#   ## including the protocol, ie http://10.10.3.33:1936/haproxy?stats
#
#   ## If no servers are specified, then default to 127.0.0.1:1936/haproxy?stats
#   servers = ["http://myhaproxy.com:1936/haproxy?stats"]
#
#   ## You can also use local socket with standard wildcard globbing.
#   ## Server address not starting with 'http' will be treated as a possible
#   ## socket, so both examples below are valid.
#   # servers = ["socket:/run/haproxy/admin.sock", "/run/haproxy/*.sock"]
#
#   ## By default, some of the fields are renamed from what haproxy calls them.
#   ## Setting this option to true results in the plugin keeping the original
#   ## field names.
#   # keep_field_names = true
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Monitor disks' temperatures using hddtemp
# [[inputs.hddtemp]]
#   ## By default, telegraf gathers temps data from all disks detected by the
#   ## hddtemp.
#   ##
#   ## Only collect temps from the selected disks.
#   ##
#   ## A * as the device name will return the temperature values of all disks.
#   ##
#   # address = "127.0.0.1:7634"
#   # devices = ["sda", "*"]


# # HTTP/HTTPS request given an address a method and a timeout
# [[inputs.http_response]]
#   ## Server address (default http://localhost)
#   # address = "http://localhost"
#
#   ## Set response_timeout (default 5 seconds)
#   # response_timeout = "5s"
#
#   ## HTTP Request Method
#   # method = "GET"
#
#   ## Whether to follow redirects from the server (defaults to false)
#   # follow_redirects = false
#
#   ## Optional HTTP Request Body
#   # body = '''
#   # {'fake':'data'}
#   # '''
#
#   ## Optional substring or regex match in body of the response
#   # response_string_match = "\"service_status\": \"up\""
#   # response_string_match = "ok"
#   # response_string_match = "\".*_status\".?:.?\"up\""
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## HTTP Request Headers (all values must be strings)
#   # [inputs.http_response.headers]
#   #   Host = "github.com"


# # Read flattened metrics from one or more JSON HTTP endpoints
# [[inputs.httpjson]]
#   ## NOTE This plugin only reads numerical measurements, strings and booleans
#   ## will be ignored.
#
#   ## Name for the service being polled.  Will be appended to the name of the
#   ## measurement e.g. httpjson_webserver_stats
#   ##
#   ## Deprecated (1.3.0): Use name_override, name_suffix, name_prefix instead.
#   name = "webserver_stats"
#
#   ## URL of each server in the service's cluster
#   servers = [
#     "http://localhost:9999/stats/",
#     "http://localhost:9998/stats/",
#   ]
#   ## Set response_timeout (default 5 seconds)
#   response_timeout = "5s"
#
#   ## HTTP method to use: GET or POST (case-sensitive)
#   method = "GET"
#
#   ## List of tag names to extract from top-level of JSON server response
#   # tag_keys = [
#   #   "my_tag_1",
#   #   "my_tag_2"
#   # ]
#
#   ## HTTP parameters (all values must be strings).  For "GET" requests, data
#   ## will be included in the query.  For "POST" requests, data will be included
#   ## in the request body as "x-www-form-urlencoded".
#   # [inputs.httpjson.parameters]
#   #   event_type = "cpu_spike"
#   #   threshold = "0.75"
#
#   ## HTTP Headers (all values must be strings)
#   # [inputs.httpjson.headers]
#   #   X-Auth-Token = "my-xauth-token"
#   #   apiVersion = "v1"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Read InfluxDB-formatted JSON metrics from one or more HTTP endpoints
# [[inputs.influxdb]]
#   ## Works with InfluxDB debug endpoints out of the box,
#   ## but other services can use this format too.
#   ## See the influxdb plugin's README for more details.
#
#   ## Multiple URLs from which to read InfluxDB-formatted JSON
#   ## Default is "http://localhost:8086/debug/vars".
#   urls = [
#     "http://localhost:8086/debug/vars"
#   ]
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## http request & header timeout
#   timeout = "5s"


# # Collect statistics about itself
# [[inputs.internal]]
#   ## If true, collect telegraf memory stats.
#   # collect_memstats = true


# # This plugin gathers interrupts data from /proc/interrupts and /proc/softirqs.
# [[inputs.interrupts]]
#   ## To filter which IRQs to collect, make use of tagpass / tagdrop, i.e.
#   # [inputs.interrupts.tagdrop]
#     # irq = [ "NET_RX", "TASKLET" ]


# # Read metrics from the bare metal servers via IPMI
# [[inputs.ipmi_sensor]]
#   ## optionally specify the path to the ipmitool executable
#   # path = "/usr/bin/ipmitool"
#   #
#   ## optionally specify one or more servers via a url matching
#   ##  [username[:password]@][protocol[(address)]]
#   ##  e.g.
#   ##    root:passwd@lan(127.0.0.1)
#   ##
#   ## if no servers are specified, local machine sensor stats will be queried
#   ##
#   # servers = ["USERID:PASSW0RD@lan(192.168.1.1)"]
#
#   ## Recomended: use metric 'interval' that is a multiple of 'timeout' to avoid
#   ## gaps or overlap in pulled data
#   interval = "30s"
#
#   ## Timeout for the ipmitool command to complete
#   timeout = "20s"


# # Gather packets and bytes throughput from iptables
# [[inputs.iptables]]
#   ## iptables require root access on most systems.
#   ## Setting 'use_sudo' to true will make use of sudo to run iptables.
#   ## Users must configure sudo to allow telegraf user to run iptables with no password.
#   ## iptables can be restricted to only list command "iptables -nvL".
#   use_sudo = false
#   ## Setting 'use_lock' to true runs iptables with the "-w" option.
#   ## Adjust your sudo settings appropriately if using this option ("iptables -wnvl")
#   use_lock = false
#   ## defines the table to monitor:
#   table = "filter"
#   ## defines the chains to monitor.
#   ## NOTE: iptables rules without a comment will not be monitored.
#   ## Read the plugin documentation for more information.
#   chains = [ "INPUT" ]


# # Read JMX metrics through Jolokia
# [[inputs.jolokia]]
#   ## This is the context root used to compose the jolokia url
#   ## NOTE that Jolokia requires a trailing slash at the end of the context root
#   ## NOTE that your jolokia security policy must allow for POST requests.
#   context = "/jolokia/"
#
#   ## This specifies the mode used
#   # mode = "proxy"
#   #
#   ## When in proxy mode this section is used to specify further
#   ## proxy address configurations.
#   ## Remember to change host address to fit your environment.
#   # [inputs.jolokia.proxy]
#   #   host = "127.0.0.1"
#   #   port = "8080"
#
#   ## Optional http timeouts
#   ##
#   ## response_header_timeout, if non-zero, specifies the amount of time to wait
#   ## for a server's response headers after fully writing the request.
#   # response_header_timeout = "3s"
#   ##
#   ## client_timeout specifies a time limit for requests made by this client.
#   ## Includes connection time, any redirects, and reading the response body.
#   # client_timeout = "4s"
#
#   ## Attribute delimiter
#   ##
#   ## When multiple attributes are returned for a single
#   ## [inputs.jolokia.metrics], the field name is a concatenation of the metric
#   ## name, and the attribute name, separated by the given delimiter.
#   # delimiter = "_"
#
#   ## List of servers exposing jolokia read service
#   [[inputs.jolokia.servers]]
#     name = "as-server-01"
#     host = "127.0.0.1"
#     port = "8080"
#     # username = "myuser"
#     # password = "mypassword"
#
#   ## List of metrics collected on above servers
#   ## Each metric consists in a name, a jmx path and either
#   ## a pass or drop slice attribute.
#   ## This collect all heap memory usage metrics.
#   [[inputs.jolokia.metrics]]
#     name = "heap_memory_usage"
#     mbean  = "java.lang:type=Memory"
#     attribute = "HeapMemoryUsage"
#
#   ## This collect thread counts metrics.
#   [[inputs.jolokia.metrics]]
#     name = "thread_count"
#     mbean  = "java.lang:type=Threading"
#     attribute = "TotalStartedThreadCount,ThreadCount,DaemonThreadCount,PeakThreadCount"
#
#   ## This collect number of class loaded/unloaded counts metrics.
#   [[inputs.jolokia.metrics]]
#     name = "class_count"
#     mbean  = "java.lang:type=ClassLoading"
#     attribute = "LoadedClassCount,UnloadedClassCount,TotalLoadedClassCount"


# # Read Kapacitor-formatted JSON metrics from one or more HTTP endpoints
# [[inputs.kapacitor]]
#   ## Multiple URLs from which to read Kapacitor-formatted JSON
#   ## Default is "http://localhost:9092/kapacitor/v1/debug/vars".
#   urls = [
#     "http://localhost:9092/kapacitor/v1/debug/vars"
#   ]
#
#   ## Time limit for http requests
#   timeout = "5s"


# # Get kernel statistics from /proc/vmstat
# [[inputs.kernel_vmstat]]
#   # no configuration


# # Read metrics from the kubernetes kubelet api
# [[inputs.kubernetes]]
#   ## URL for the kubelet
#   url = "http://1.1.1.1:10255"
#
#   ## Use bearer token for authorization
#   # bearer_token = /path/to/bearer/token
#
#   ## Optional SSL Config
#   # ssl_ca = /path/to/cafile
#   # ssl_cert = /path/to/certfile
#   # ssl_key = /path/to/keyfile
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Read metrics from a LeoFS Server via SNMP
# [[inputs.leofs]]
#   ## An array of URLs of the form:
#   ##   "udp://" host [ ":" port]
#   servers = ["udp://127.0.0.1:4020"]


# # Provides Linux sysctl fs metrics
# [[inputs.linux_sysctl_fs]]
#   # no configuration


# # Read metrics from local Lustre service on OST, MDS
# [[inputs.lustre2]]
#   ## An array of /proc globs to search for Lustre stats
#   ## If not specified, the default will work on Lustre 2.5.x
#   ##
#   # ost_procfiles = [
#   #   "/proc/fs/lustre/obdfilter/*/stats",
#   #   "/proc/fs/lustre/osd-ldiskfs/*/stats",
#   #   "/proc/fs/lustre/obdfilter/*/job_stats",
#   # ]
#   # mds_procfiles = [
#   #   "/proc/fs/lustre/mdt/*/md_stats",
#   #   "/proc/fs/lustre/mdt/*/job_stats",
#   # ]


# # Gathers metrics from the /3.0/reports MailChimp API
# [[inputs.mailchimp]]
#   ## MailChimp API key
#   ## get from https://admin.mailchimp.com/account/api/
#   api_key = "" # required
#   ## Reports for campaigns sent more than days_old ago will not be collected.
#   ## 0 means collect all.
#   days_old = 0
#   ## Campaign ID to get, if empty gets all campaigns, this option overrides days_old
#   # campaign_id = ""


# # Read metrics from one or many memcached servers
# [[inputs.memcached]]
#   ## An array of address to gather stats about. Specify an ip on hostname
#   ## with optional port. ie localhost, 10.0.0.1:11211, etc.
#   servers = ["localhost:11211"]
#   # unix_sockets = ["/var/run/memcached.sock"]


# # Telegraf plugin for gathering metrics from N Mesos masters
# [[inputs.mesos]]
#   ## Timeout, in ms.
#   timeout = 100
#   ## A list of Mesos masters.
#   masters = ["localhost:5050"]
#   ## Master metrics groups to be collected, by default, all enabled.
#   master_collections = [
#     "resources",
#     "master",
#     "system",
#     "agents",
#     "frameworks",
#     "tasks",
#     "messages",
#     "evqueue",
#     "registrar",
#   ]
#   ## A list of Mesos slaves, default is []
#   # slaves = []
#   ## Slave metrics groups to be collected, by default, all enabled.
#   # slave_collections = [
#   #   "resources",
#   #   "agent",
#   #   "system",
#   #   "executors",
#   #   "tasks",
#   #   "messages",
#   # ]


# # Collects scores from a minecraft server's scoreboard using the RCON protocol
# [[inputs.minecraft]]
#   ## server address for minecraft
#   # server = "localhost"
#   ## port for RCON
#   # port = "25575"
#   ## password RCON for mincraft server
#   # password = ""


# # Read metrics from one or many MongoDB servers
# [[inputs.mongodb]]
#   ## An array of URLs of the form:
#   ##   "mongodb://" [user ":" pass "@"] host [ ":" port]
#   ## For example:
#   ##   mongodb://user:auth_key@10.10.3.30:27017,
#   ##   mongodb://10.10.3.33:18832,
#   servers = ["mongodb://127.0.0.1:27017"]
#   gather_perdb_stats = false
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Read metrics from one or many mysql servers
# [[inputs.mysql]]
#   ## specify servers via a url matching:
#   ##  [username[:password]@][protocol[(address)]]/[?tls=[true|false|skip-verify|custom]]
#   ##  see https://github.com/go-sql-driver/mysql#dsn-data-source-name
#   ##  e.g.
#   ##    servers = ["user:passwd@tcp(127.0.0.1:3306)/?tls=false"]
#   ##    servers = ["user@tcp(127.0.0.1:3306)/?tls=false"]
#   #
#   ## If no servers are specified, then localhost is used as the host.
#   servers = ["tcp(127.0.0.1:3306)/"]
#   ## the limits for metrics form perf_events_statements
#   perf_events_statements_digest_text_limit  = 120
#   perf_events_statements_limit              = 250
#   perf_events_statements_time_limit         = 86400
#   #
#   ## if the list is empty, then metrics are gathered from all databasee tables
#   table_schema_databases                    = []
#   #
#   ## gather metrics from INFORMATION_SCHEMA.TABLES for databases provided above list
#   gather_table_schema                       = false
#   #
#   ## gather thread state counts from INFORMATION_SCHEMA.PROCESSLIST
#   gather_process_list                       = true
#   #
#   ## gather thread state counts from INFORMATION_SCHEMA.USER_STATISTICS
#   gather_user_statistics                    = true
#   #
#   ## gather auto_increment columns and max values from information schema
#   gather_info_schema_auto_inc               = true
#   #
#   ## gather metrics from INFORMATION_SCHEMA.INNODB_METRICS
#   gather_innodb_metrics                     = true
#   #
#   ## gather metrics from SHOW SLAVE STATUS command output
#   gather_slave_status                       = true
#   #
#   ## gather metrics from SHOW BINARY LOGS command output
#   gather_binary_logs                        = false
#   #
#   ## gather metrics from PERFORMANCE_SCHEMA.TABLE_IO_WAITS_SUMMARY_BY_TABLE
#   gather_table_io_waits                     = false
#   #
#   ## gather metrics from PERFORMANCE_SCHEMA.TABLE_LOCK_WAITS
#   gather_table_lock_waits                   = false
#   #
#   ## gather metrics from PERFORMANCE_SCHEMA.TABLE_IO_WAITS_SUMMARY_BY_INDEX_USAGE
#   gather_index_io_waits                     = false
#   #
#   ## gather metrics from PERFORMANCE_SCHEMA.EVENT_WAITS
#   gather_event_waits                        = false
#   #
#   ## gather metrics from PERFORMANCE_SCHEMA.FILE_SUMMARY_BY_EVENT_NAME
#   gather_file_events_stats                  = false
#   #
#   ## gather metrics from PERFORMANCE_SCHEMA.EVENTS_STATEMENTS_SUMMARY_BY_DIGEST
#   gather_perf_events_statements             = false
#   #
#   ## Some queries we may want to run less often (such as SHOW GLOBAL VARIABLES)
#   interval_slow                   = "30m"
#
#   ## Optional SSL Config (will be used if tls=custom parameter specified in server uri)
#   ssl_ca = "/etc/telegraf/ca.pem"
#   ssl_cert = "/etc/telegraf/cert.pem"
#   ssl_key = "/etc/telegraf/key.pem"


# # Read metrics about network interface usage
[[inputs.net]]
#   ## By default, telegraf gathers stats from any up interface (excluding loopback)
#   ## Setting interfaces will tell it to gather these explicit interfaces,
#   ## regardless of status.
#   ##
#   # interfaces = ["eth0"]


# # TCP or UDP 'ping' given url and collect response time in seconds
# [[inputs.net_response]]
#   ## Protocol, must be "tcp" or "udp"
#   ## NOTE: because the "udp" protocol does not respond to requests, it requires
#   ## a send/expect string pair (see below).
#   protocol = "tcp"
#   ## Server address (default localhost)
#   address = "localhost:80"
#   ## Set timeout
#   timeout = "1s"
#
#   ## Set read timeout (only used if expecting a response)
#   read_timeout = "1s"
#
#   ## The following options are required for UDP checks. For TCP, they are
#   ## optional. The plugin will send the given string to the server and then
#   ## expect to receive the given 'expect' string back.
#   ## string sent to the server
#   # send = "ssh"
#   ## expected string in answer
#   # expect = "ssh"


# # Read TCP metrics such as established, time wait and sockets counts.
[[inputs.netstat]]
#   # no configuration


# # Read Nginx's basic status information (ngx_http_stub_status_module)
# [[inputs.nginx]]
#   # An array of Nginx stub_status URI to gather stats.
#   urls = ["http://localhost/server_status"]
#
#   # TLS/SSL configuration
#   ssl_ca = "/etc/telegraf/ca.pem"
#   ssl_cert = "/etc/telegraf/cert.cer"
#   ssl_key = "/etc/telegraf/key.key"
#   insecure_skip_verify = false
#
#   # HTTP response timeout (default: 5s)
#   response_timeout = "5s"


# # Read NSQ topic and channel statistics.
# [[inputs.nsq]]
#   ## An array of NSQD HTTP API endpoints
#   endpoints = ["http://localhost:4151"]


# # Collect kernel snmp counters and network interface statistics
# [[inputs.nstat]]
#   ## file paths for proc files. If empty default paths will be used:
#   ##    /proc/net/netstat, /proc/net/snmp, /proc/net/snmp6
#   ## These can also be overridden with env variables, see README.
#   proc_net_netstat = "/proc/net/netstat"
#   proc_net_snmp = "/proc/net/snmp"
#   proc_net_snmp6 = "/proc/net/snmp6"
#   ## dump metrics with 0 values too
#   dump_zeros       = true


# # Get standard NTP query metrics, requires ntpq executable.
# [[inputs.ntpq]]
#   ## If false, set the -n ntpq flag. Can reduce metric gather time.
#   dns_lookup = true


# # OpenLDAP cn=Monitor plugin
# [[inputs.openldap]]
#   host = "localhost"
#   port = 389
#
#   # ldaps, starttls, or no encryption. default is an empty string, disabling all encryption.
#   # note that port will likely need to be changed to 636 for ldaps
#   # valid options: "" | "starttls" | "ldaps"
#   ssl = ""
#
#   # skip peer certificate verification. Default is false.
#   insecure_skip_verify = false
#
#   # Path to PEM-encoded Root certificate to use to verify server certificate
#   ssl_ca = "/etc/ssl/certs.pem"
#
#   # dn/password to bind with. If bind_dn is empty, an anonymous bind is performed.
#   bind_dn = ""
#   bind_password = ""


# # Read metrics of passenger using passenger-status
# [[inputs.passenger]]
#   ## Path of passenger-status.
#   ##
#   ## Plugin gather metric via parsing XML output of passenger-status
#   ## More information about the tool:
#   ##   https://www.phusionpassenger.com/library/admin/apache/overall_status_report.html
#   ##
#   ## If no path is specified, then the plugin simply execute passenger-status
#   ## hopefully it can be found in your PATH
#   command = "passenger-status -v --show=xml"


# # Read metrics of phpfpm, via HTTP status page or socket
# [[inputs.phpfpm]]
#   ## An array of addresses to gather stats about. Specify an ip or hostname
#   ## with optional port and path
#   ##
#   ## Plugin can be configured in three modes (either can be used):
#   ##   - http: the URL must start with http:// or https://, ie:
#   ##       "http://localhost/status"
#   ##       "http://192.168.130.1/status?full"
#   ##
#   ##   - unixsocket: path to fpm socket, ie:
#   ##       "/var/run/php5-fpm.sock"
#   ##      or using a custom fpm status path:
#   ##       "/var/run/php5-fpm.sock:fpm-custom-status-path"
#   ##
#   ##   - fcgi: the URL must start with fcgi:// or cgi://, and port must be present, ie:
#   ##       "fcgi://10.0.0.12:9000/status"
#   ##       "cgi://10.0.10.12:9001/status"
#   ##
#   ## Example of multiple gathering from local socket and remove host
#   ## urls = ["http://192.168.1.20/status", "/tmp/fpm.sock"]
#   urls = ["http://localhost/status"]


# # Ping given url(s) and return statistics
# [[inputs.ping]]
#   ## NOTE: this plugin forks the ping command. You may need to set capabilities
#   ## via setcap cap_net_raw+p /bin/ping
#   #
#   ## List of urls to ping
#   urls = ["www.google.com"] # required
#   ## number of pings to send per collection (ping -c <COUNT>)
#   # count = 1
#   ## interval, in s, at which to ping. 0 == default (ping -i <PING_INTERVAL>)
#   # ping_interval = 1.0
#   ## per-ping timeout, in s. 0 == no timeout (ping -W <TIMEOUT>)
#   # timeout = 1.0
#   ## interface to send ping from (ping -I <INTERFACE>)
#   # interface = ""


# # Read metrics from one or many postgresql servers
# [[inputs.postgresql]]
#   ## specify address via a url matching:
#   ##   postgres://[pqgotest[:password]]@localhost[/dbname]\
#   ##       ?sslmode=[disable|verify-ca|verify-full]
#   ## or a simple string:
#   ##   host=localhost user=pqotest password=... sslmode=... dbname=app_production
#   ##
#   ## All connection parameters are optional.
#   ##
#   ## Without the dbname parameter, the driver will default to a database
#   ## with the same name as the user. This dbname is just for instantiating a
#   ## connection with the server and doesn't restrict the databases we are trying
#   ## to grab metrics for.
#   ##
#   address = "host=localhost user=postgres sslmode=disable"
#
#   ## A  list of databases to explicitly ignore.  If not specified, metrics for all
#   ## databases are gathered.  Do NOT use with the 'databases' option.
#   # ignored_databases = ["postgres", "template0", "template1"]
#
#   ## A list of databases to pull metrics about. If not specified, metrics for all
#   ## databases are gathered.  Do NOT use with the 'ignored_databases' option.
#   # databases = ["app_production", "testing"]


# # Read metrics from one or many postgresql servers
# [[inputs.postgresql_extensible]]
#   ## specify address via a url matching:
#   ##   postgres://[pqgotest[:password]]@localhost[/dbname]\
#   ##       ?sslmode=[disable|verify-ca|verify-full]
#   ## or a simple string:
#   ##   host=localhost user=pqotest password=... sslmode=... dbname=app_production
#   #
#   ## All connection parameters are optional.  #
#   ## Without the dbname parameter, the driver will default to a database
#   ## with the same name as the user. This dbname is just for instantiating a
#   ## connection with the server and doesn't restrict the databases we are trying
#   ## to grab metrics for.
#   #
#   address = "host=localhost user=postgres sslmode=disable"
#   ## A list of databases to pull metrics about. If not specified, metrics for all
#   ## databases are gathered.
#   ## databases = ["app_production", "testing"]
#   #
#   # outputaddress = "db01"
#   ## A custom name for the database that will be used as the "server" tag in the
#   ## measurement output. If not specified, a default one generated from
#   ## the connection address is used.
#   #
#   ## Define the toml config where the sql queries are stored
#   ## New queries can be added, if the withdbname is set to true and there is no
#   ## databases defined in the 'databases field', the sql query is ended by a
#   ## 'is not null' in order to make the query succeed.
#   ## Example :
#   ## The sqlquery : "SELECT * FROM pg_stat_database where datname" become
#   ## "SELECT * FROM pg_stat_database where datname IN ('postgres', 'pgbench')"
#   ## because the databases variable was set to ['postgres', 'pgbench' ] and the
#   ## withdbname was true. Be careful that if the withdbname is set to false you
#   ## don't have to define the where clause (aka with the dbname) the tagvalue
#   ## field is used to define custom tags (separated by commas)
#   ## The optional "measurement" value can be used to override the default
#   ## output measurement name ("postgresql").
#   #
#   ## Structure :
#   ## [[inputs.postgresql_extensible.query]]
#   ##   sqlquery string
#   ##   version string
#   ##   withdbname boolean
#   ##   tagvalue string (comma separated)
#   ##   measurement string
#   [[inputs.postgresql_extensible.query]]
#     sqlquery="SELECT * FROM pg_stat_database"
#     version=901
#     withdbname=false
#     tagvalue=""
#     measurement=""
#   [[inputs.postgresql_extensible.query]]
#     sqlquery="SELECT * FROM pg_stat_bgwriter"
#     version=901
#     withdbname=false
#     tagvalue="postgresql.stats"


# # Read metrics from one or many PowerDNS servers
# [[inputs.powerdns]]
#   ## An array of sockets to gather stats about.
#   ## Specify a path to unix socket.
#   unix_sockets = ["/var/run/pdns.controlsocket"]


# # Monitor process cpu and memory usage
# [[inputs.procstat]]
#   ## Must specify one of: pid_file, exe, or pattern
#   ## PID file to monitor process
#   pid_file = "/var/run/nginx.pid"
#   ## executable name (ie, pgrep <exe>)
#   # exe = "nginx"
#   ## pattern as argument for pgrep (ie, pgrep -f <pattern>)
#   # pattern = "nginx"
#   ## user as argument for pgrep (ie, pgrep -u <user>)
#   # user = "nginx"
#
#   ## override for process_name
#   ## This is optional; default is sourced from /proc/<pid>/status
#   # process_name = "bar"
#   ## Field name prefix
#   prefix = ""
#   ## comment this out if you want raw cpu_time stats
#   fielddrop = ["cpu_time_*"]
#   ## This is optional; moves pid into a tag instead of a field
#   pid_tag = false


# # Read metrics from one or many prometheus clients
# [[inputs.prometheus]]
#   ## An array of urls to scrape metrics from.
#   urls = ["http://localhost:9100/metrics"]
#
#   ## Use bearer token for authorization
#   # bearer_token = /path/to/bearer/token
#
#   ## Specify timeout duration for slower prometheus clients (default is 3s)
#   # response_timeout = "3s"
#
#   ## Optional SSL Config
#   # ssl_ca = /path/to/cafile
#   # ssl_cert = /path/to/certfile
#   # ssl_key = /path/to/keyfile
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Reads last_run_summary.yaml file and converts to measurments
# [[inputs.puppetagent]]
#   ## Location of puppet last run summary file
#   location = "/var/lib/puppet/state/last_run_summary.yaml"


# # Reads metrics from RabbitMQ servers via the Management Plugin
# [[inputs.rabbitmq]]
#   ## Management Plugin url. (default: http://localhost:15672)
#   # url = "http://localhost:15672"
#   ## Tag added to rabbitmq_overview series; deprecated: use tags
#   # name = "rmq-server-1"
#   ## Credentials
#   # username = "guest"
#   # password = "guest"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Optional request timeouts
#   ##
#   ## ResponseHeaderTimeout, if non-zero, specifies the amount of time to wait
#   ## for a server's response headers after fully writing the request.
#   # header_timeout = "3s"
#   ##
#   ## client_timeout specifies a time limit for requests made by this client.
#   ## Includes connection time, any redirects, and reading the response body.
#   # client_timeout = "4s"
#
#   ## A list of nodes to gather as the rabbitmq_node measurement. If not
#   ## specified, metrics for all nodes are gathered.
#   # nodes = ["rabbit@node1", "rabbit@node2"]
#
#   ## A list of queues to gather as the rabbitmq_queue measurement. If not
#   ## specified, metrics for all queues are gathered.
#   # queues = ["telegraf"]


# # Read raindrops stats (raindrops - real-time stats for preforking Rack servers)
# [[inputs.raindrops]]
#   ## An array of raindrops middleware URI to gather stats.
#   urls = ["http://localhost:8080/_raindrops"]


# # Read metrics from one or many redis servers
# [[inputs.redis]]
#   ## specify servers via a url matching:
#   ##  [protocol://][:password]@address[:port]
#   ##  e.g.
#   ##    tcp://localhost:6379
#   ##    tcp://:password@192.168.99.100
#   ##    unix:///var/run/redis.sock
#   ##
#   ## If no servers are specified, then localhost is used as the host.
#   ## If no port is specified, 6379 is used
#   servers = ["tcp://localhost:6379"]


# # Read metrics from one or many RethinkDB servers
# [[inputs.rethinkdb]]
#   ## An array of URI to gather stats about. Specify an ip or hostname
#   ## with optional port add password. ie,
#   ##   rethinkdb://user:auth_key@10.10.3.30:28105,
#   ##   rethinkdb://10.10.3.33:18832,
#   ##   10.0.0.1:10000, etc.
#   servers = ["127.0.0.1:28015"]
#   ##
#   ## If you use actual rethinkdb of > 2.3.0 with username/password authorization,
#   ## protocol have to be named "rethinkdb2" - it will use 1_0 H.
#   # servers = ["rethinkdb2://username:password@127.0.0.1:28015"]
#   ##
#   ## If you use older versions of rethinkdb (<2.2) with auth_key, protocol
#   ## have to be named "rethinkdb".
#   # servers = ["rethinkdb://username:auth_key@127.0.0.1:28015"]


# # Read metrics one or many Riak servers
# [[inputs.riak]]
#   # Specify a list of one or more riak http servers
#   servers = ["http://localhost:8098"]


# # Read API usage and limits for a Salesforce organisation
# [[inputs.salesforce]]
#   ## specify your credentials
#   ##
#   username = "your_username"
#   password = "your_password"
#   ##
#   ## (optional) security token
#   # security_token = "your_security_token"
#   ##
#   ## (optional) environment type (sandbox or production)
#   ## default is: production
#   ##
#   # environment = "production"
#   ##
#   ## (optional) API version (default: "39.0")
#   ##
#   # version = "39.0"


# # Monitor sensors, requires lm-sensors package
# [[inputs.sensors]]
#   ## Remove numbers from field names.
#   ## If true, a field name like 'temp1_input' will be changed to 'temp_input'.
#   # remove_numbers = true


# # Retrieves SNMP values from remote agents
# [[inputs.snmp]]
#   agents = [ "127.0.0.1:161" ]
#   ## Timeout for each SNMP query.
#   timeout = "5s"
#   ## Number of retries to attempt within timeout.
#   retries = 3
#   ## SNMP version, values can be 1, 2, or 3
#   version = 2
#
#   ## SNMP community string.
#   community = "public"
#
#   ## The GETBULK max-repetitions parameter
#   max_repetitions = 10
#
#   ## SNMPv3 auth parameters
#   #sec_name = "myuser"
#   #auth_protocol = "md5"      # Values: "MD5", "SHA", ""
#   #auth_password = "pass"
#   #sec_level = "authNoPriv"   # Values: "noAuthNoPriv", "authNoPriv", "authPriv"
#   #context_name = ""
#   #priv_protocol = ""         # Values: "DES", "AES", ""
#   #priv_password = ""
#
#   ## measurement name
#   name = "system"
#   [[inputs.snmp.field]]
#     name = "hostname"
#     oid = ".1.0.0.1.1"
#   [[inputs.snmp.field]]
#     name = "uptime"
#     oid = ".1.0.0.1.2"
#   [[inputs.snmp.field]]
#     name = "load"
#     oid = ".1.0.0.1.3"
#   [[inputs.snmp.field]]
#     oid = "HOST-RESOURCES-MIB::hrMemorySize"
#
#   [[inputs.snmp.table]]
#     ## measurement name
#     name = "remote_servers"
#     inherit_tags = [ "hostname" ]
#     [[inputs.snmp.table.field]]
#       name = "server"
#       oid = ".1.0.0.0.1.0"
#       is_tag = true
#     [[inputs.snmp.table.field]]
#       name = "connections"
#       oid = ".1.0.0.0.1.1"
#     [[inputs.snmp.table.field]]
#       name = "latency"
#       oid = ".1.0.0.0.1.2"
#
#   [[inputs.snmp.table]]
#     ## auto populate table's fields using the MIB
#     oid = "HOST-RESOURCES-MIB::hrNetworkTable"


# # DEPRECATED! PLEASE USE inputs.snmp INSTEAD.
# [[inputs.snmp_legacy]]
#   ## Use 'oids.txt' file to translate oids to names
#   ## To generate 'oids.txt' you need to run:
#   ##   snmptranslate -m all -Tz -On | sed -e 's/"//g' > /tmp/oids.txt
#   ## Or if you have an other MIB folder with custom MIBs
#   ##   snmptranslate -M /mycustommibfolder -Tz -On -m all | sed -e 's/"//g' > oids.txt
#   snmptranslate_file = "/tmp/oids.txt"
#   [[inputs.snmp.host]]
#     address = "192.168.2.2:161"
#     # SNMP community
#     community = "public" # default public
#     # SNMP version (1, 2 or 3)
#     # Version 3 not supported yet
#     version = 2 # default 2
#     # SNMP response timeout
#     timeout = 2.0 # default 2.0
#     # SNMP request retries
#     retries = 2 # default 2
#     # Which get/bulk do you want to collect for this host
#     collect = ["mybulk", "sysservices", "sysdescr"]
#     # Simple list of OIDs to get, in addition to "collect"
#     get_oids = []
#
#   [[inputs.snmp.host]]
#     address = "192.168.2.3:161"
#     community = "public"
#     version = 2
#     timeout = 2.0
#     retries = 2
#     collect = ["mybulk"]
#     get_oids = [
#         "ifNumber",
#         ".1.3.6.1.2.1.1.3.0",
#     ]
#
#   [[inputs.snmp.get]]
#     name = "ifnumber"
#     oid = "ifNumber"
#
#   [[inputs.snmp.get]]
#     name = "interface_speed"
#     oid = "ifSpeed"
#     instance = "0"
#
#   [[inputs.snmp.get]]
#     name = "sysuptime"
#     oid = ".1.3.6.1.2.1.1.3.0"
#     unit = "second"
#
#   [[inputs.snmp.bulk]]
#     name = "mybulk"
#     max_repetition = 127
#     oid = ".1.3.6.1.2.1.1"
#
#   [[inputs.snmp.bulk]]
#     name = "ifoutoctets"
#     max_repetition = 127
#     oid = "ifOutOctets"
#
#   [[inputs.snmp.host]]
#     address = "192.168.2.13:161"
#     #address = "127.0.0.1:161"
#     community = "public"
#     version = 2
#     timeout = 2.0
#     retries = 2
#     #collect = ["mybulk", "sysservices", "sysdescr", "systype"]
#     collect = ["sysuptime" ]
#     [[inputs.snmp.host.table]]
#       name = "iftable3"
#       include_instances = ["enp5s0", "eth1"]
#
#   # SNMP TABLEs
#   # table without mapping neither subtables
#   [[inputs.snmp.table]]
#     name = "iftable1"
#     oid = ".1.3.6.1.2.1.31.1.1.1"
#
#   # table without mapping but with subtables
#   [[inputs.snmp.table]]
#     name = "iftable2"
#     oid = ".1.3.6.1.2.1.31.1.1.1"
#     sub_tables = [".1.3.6.1.2.1.2.2.1.13"]
#
#   # table with mapping but without subtables
#   [[inputs.snmp.table]]
#     name = "iftable3"
#     oid = ".1.3.6.1.2.1.31.1.1.1"
#     # if empty. get all instances
#     mapping_table = ".1.3.6.1.2.1.31.1.1.1.1"
#     # if empty, get all subtables
#
#   # table with both mapping and subtables
#   [[inputs.snmp.table]]
#     name = "iftable4"
#     oid = ".1.3.6.1.2.1.31.1.1.1"
#     # if empty get all instances
#     mapping_table = ".1.3.6.1.2.1.31.1.1.1.1"
#     # if empty get all subtables
#     # sub_tables could be not "real subtables"
#     sub_tables=[".1.3.6.1.2.1.2.2.1.13", "bytes_recv", "bytes_send"]


# # Read metrics from Microsoft SQL Server
# [[inputs.sqlserver]]
#   ## Specify instances to monitor with a list of connection strings.
#   ## All connection parameters are optional.
#   ## By default, the host is localhost, listening on default port, TCP 1433.
#   ##   for Windows, the user is the currently running AD user (SSO).
#   ##   See https://github.com/denisenkom/go-mssqldb for detailed connection
#   ##   parameters.
#   # servers = [
#   #  "Server=192.168.1.10;Port=1433;User Id=<user>;Password=<pw>;app name=telegraf;log=1;",
#   # ]


# # Sysstat metrics collector
# [[inputs.sysstat]]
#   ## Path to the sadc command.
#   #
#   ## Common Defaults:
#   ##   Debian/Ubuntu: /usr/lib/sysstat/sadc
#   ##   Arch:          /usr/lib/sa/sadc
#   ##   RHEL/CentOS:   /usr/lib64/sa/sadc
#   sadc_path = "/usr/lib/sa/sadc" # required
#   #
#   #
#   ## Path to the sadf command, if it is not in PATH
#   # sadf_path = "/usr/bin/sadf"
#   #
#   #
#   ## Activities is a list of activities, that are passed as argument to the
#   ## sadc collector utility (e.g: DISK, SNMP etc...)
#   ## The more activities that are added, the more data is collected.
#   # activities = ["DISK"]
#   #
#   #
#   ## Group metrics to measurements.
#   ##
#   ## If group is false each metric will be prefixed with a description
#   ## and represents itself a measurement.
#   ##
#   ## If Group is true, corresponding metrics are grouped to a single measurement.
#   # group = true
#   #
#   #
#   ## Options for the sadf command. The values on the left represent the sadf
#   ## options and the values on the right their description (wich are used for
#   ## grouping and prefixing metrics).
#   ##
#   ## Run 'sar -h' or 'man sar' to find out the supported options for your
#   ## sysstat version.
#   [inputs.sysstat.options]
#     -C = "cpu"
#     -B = "paging"
#     -b = "io"
#     -d = "disk"             # requires DISK activity
#     "-n ALL" = "network"
#     "-P ALL" = "per_cpu"
#     -q = "queue"
#     -R = "mem"
#     -r = "mem_util"
#     -S = "swap_util"
#     -u = "cpu_util"
#     -v = "inode"
#     -W = "swap"
#     -w = "task"
#   #  -H = "hugepages"        # only available for newer linux distributions
#   #  "-I ALL" = "interrupts" # requires INT activity
#   #
#   #
#   ## Device tags can be used to add additional tags for devices.
#   ## For example the configuration below adds a tag vg with value rootvg for
#   ## all metrics with sda devices.
#   # [[inputs.sysstat.device_tags.sda]]
#   #  vg = "rootvg"


# # Gather metrics from the Tomcat server status page.
# [[inputs.tomcat]]
#   ## URL of the Tomcat server status
#   # url = "http://127.0.0.1:8080/manager/status/all?XML=true"
#
#   ## HTTP Basic Auth Credentials
#   # username = "tomcat"
#   # password = "s3cret"
#
#   ## Request timeout
#   # timeout = "5s"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false


# # Inserts sine and cosine waves for demonstration purposes
# [[inputs.trig]]
#   ## Set the amplitude
#   amplitude = 10.0


# # Read Twemproxy stats data
# [[inputs.twemproxy]]
#   ## Twemproxy stats address and port (no scheme)
#   addr = "localhost:22222"
#   ## Monitor pool name
#   pools = ["redis_pool", "mc_pool"]


# # A plugin to collect stats from Varnish HTTP Cache
# [[inputs.varnish]]
#   ## If running as a restricted user you can prepend sudo for additional access:
#   #use_sudo = false
#
#   ## The default location of the varnishstat binary can be overridden with:
#   binary = "/usr/bin/varnishstat"
#
#   ## By default, telegraf gather stats for 3 metric points.
#   ## Setting stats will override the defaults shown below.
#   ## Glob matching can be used, ie, stats = ["MAIN.*"]
#   ## stats may also be set to ["*"], which will collect all stats
#   stats = ["MAIN.cache_hit", "MAIN.cache_miss", "MAIN.uptime"]


# # Read metrics of ZFS from arcstats, zfetchstats, vdev_cache_stats, and pools
# [[inputs.zfs]]
#   ## ZFS kstat path. Ignored on FreeBSD
#   ## If not specified, then default is:
#   # kstatPath = "/proc/spl/kstat/zfs"
#
#   ## By default, telegraf gather all zfs stats
#   ## If not specified, then default is:
#   # kstatMetrics = ["arcstats", "zfetchstats", "vdev_cache_stats"]
#
#   ## By default, don't gather zpool stats
#   # poolMetrics = false


# # Reads 'mntr' stats from one or many zookeeper servers
# [[inputs.zookeeper]]
#   ## An array of address to gather stats about. Specify an ip or hostname
#   ## with port. ie localhost:2181, 10.0.0.1:2181, etc.
#
#   ## If no servers are specified, then localhost is used as the host.
#   ## If no port is specified, 2181 is used
#   servers = [":2181"]



###############################################################################
#                            SERVICE INPUT PLUGINS                            #
###############################################################################

# # AMQP consumer plugin
# [[inputs.amqp_consumer]]
#   ## AMQP url
#   url = "amqp://localhost:5672/influxdb"
#   ## AMQP exchange
#   exchange = "telegraf"
#   ## AMQP queue name
#   queue = "telegraf"
#   ## Binding Key
#   binding_key = "#"
#
#   ## Maximum number of messages server should give to the worker.
#   prefetch_count = 50
#
#   ## Auth method. PLAIN and EXTERNAL are supported
#   ## Using EXTERNAL requires enabling the rabbitmq_auth_mechanism_ssl plugin as
#   ## described here: https://www.rabbitmq.com/plugins.html
#   # auth_method = "PLAIN"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Data format to output.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_OUTPUT.md
#   data_format = "influx"


# # Influx HTTP write listener
# [[inputs.http_listener]]
#   ## Address and port to host HTTP listener on
#   service_address = ":8186"
#
#   ## maximum duration before timing out read of the request
#   read_timeout = "10s"
#   ## maximum duration before timing out write of the response
#   write_timeout = "10s"
#
#   ## Maximum allowed http request body size in bytes.
#   ## 0 means to use the default of 536,870,912 bytes (500 mebibytes)
#   max_body_size = 0
#
#   ## Maximum line size allowed to be sent in bytes.
#   ## 0 means to use the default of 65536 bytes (64 kibibytes)
#   max_line_size = 0


# # Read metrics from Kafka topic(s)
# [[inputs.kafka_consumer]]
#   ## kafka servers
#   brokers = ["localhost:9092"]
#   ## topic(s) to consume
#   topics = ["telegraf"]
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Optional SASL Config
#   # sasl_username = "kafka"
#   # sasl_password = "secret"
#
#   ## the name of the consumer group
#   consumer_group = "telegraf_metrics_consumers"
#   ## Offset (must be either "oldest" or "newest")
#   offset = "oldest"
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   data_format = "influx"
#
#   ## Maximum length of a message to consume, in bytes (default 0/unlimited);
#   ## larger messages are dropped
#   max_message_len = 65536


# # Read metrics from Kafka topic(s)
# [[inputs.kafka_consumer_legacy]]
#   ## topic(s) to consume
#   topics = ["telegraf"]
#   ## an array of Zookeeper connection strings
#   zookeeper_peers = ["localhost:2181"]
#   ## Zookeeper Chroot
#   zookeeper_chroot = ""
#   ## the name of the consumer group
#   consumer_group = "telegraf_metrics_consumers"
#   ## Offset (must be either "oldest" or "newest")
#   offset = "oldest"
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   data_format = "influx"
#
#   ## Maximum length of a message to consume, in bytes (default 0/unlimited);
#   ## larger messages are dropped
#   max_message_len = 65536


# # Stream and parse log file(s).
# [[inputs.logparser]]
#   ## Log files to parse.
#   ## These accept standard unix glob matching rules, but with the addition of
#   ## ** as a "super asterisk". ie:
#   ##   /var/log/**.log     -> recursively find all .log files in /var/log
#   ##   /var/log/*/*.log    -> find all .log files with a parent dir in /var/log
#   ##   /var/log/apache.log -> only tail the apache log file
#   files = ["/var/log/apache/access.log"]
#
#   ## Read files that currently exist from the beginning. Files that are created
#   ## while telegraf is running (and that match the "files" globs) will always
#   ## be read from the beginning.
#   from_beginning = false
#
#   ## Parse logstash-style "grok" patterns:
#   ##   Telegraf built-in parsing patterns: https://goo.gl/dkay10
#   [inputs.logparser.grok]
#     ## This is a list of patterns to check the given log file(s) for.
#     ## Note that adding patterns here increases processing time. The most
#     ## efficient configuration is to have one pattern per logparser.
#     ## Other common built-in patterns are:
#     ##   %{COMMON_LOG_FORMAT}   (plain apache & nginx access logs)
#     ##   %{COMBINED_LOG_FORMAT} (access logs + referrer & agent)
#     patterns = ["%{COMBINED_LOG_FORMAT}"]
#
#     ## Name of the outputted measurement name.
#     measurement = "apache_access_log"
#
#     ## Full path(s) to custom pattern files.
#     custom_pattern_files = []
#
#     ## Custom patterns can also be defined here. Put one pattern per line.
#     custom_patterns = '''
#
#     ## Timezone allows you to provide an override for timestamps that
#     ## don't already include an offset
#     ## e.g. 04/06/2016 12:41:45 data one two 5.43µs
#     ##
#     ## Default: "" which renders UTC
#     ## Options are as follows:
#     ##   1. Local             -- interpret based on machine localtime
#     ##   2. "Canada/Eastern"  -- Unix TZ values like those found in https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
#     ##   3. UTC               -- or blank/unspecified, will return timestamp in UTC
#     timezone = "Canada/Eastern"
#     '''


# # Read metrics from MQTT topic(s)
# [[inputs.mqtt_consumer]]
#   servers = ["localhost:1883"]
#   ## MQTT QoS, must be 0, 1, or 2
#   qos = 0
#
#   ## Topics to subscribe to
#   topics = [
#     "telegraf/host01/cpu",
#     "telegraf/+/mem",
#     "sensors/#",
#   ]
#
#   # if true, messages that can't be delivered while the subscriber is offline
#   # will be delivered when it comes back (such as on service restart).
#   # NOTE: if true, client_id MUST be set
#   persistent_session = false
#   # If empty, a random client ID will be generated.
#   client_id = ""
#
#   ## username and password to connect MQTT server.
#   # username = "telegraf"
#   # password = "metricsmetricsmetricsmetrics"
#
#   ## Optional SSL Config
#   # ssl_ca = "/etc/telegraf/ca.pem"
#   # ssl_cert = "/etc/telegraf/cert.pem"
#   # ssl_key = "/etc/telegraf/key.pem"
#   ## Use SSL but skip chain & host verification
#   # insecure_skip_verify = false
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   data_format = "influx"


# # Read metrics from NATS subject(s)
# [[inputs.nats_consumer]]
#   ## urls of NATS servers
#   # servers = ["nats://localhost:4222"]
#   ## Use Transport Layer Security
#   # secure = false
#   ## subject(s) to consume
#   # subjects = ["telegraf"]
#   ## name a queue group
#   # queue_group = "telegraf_consumers"
#
#   ## Sets the limits for pending msgs and bytes for each subscription
#   ## These shouldn't need to be adjusted except in very high throughput scenarios
#   # pending_message_limit = 65536
#   # pending_bytes_limit = 67108864
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   data_format = "influx"


# # Read NSQ topic for metrics.
# [[inputs.nsq_consumer]]
#   ## An string representing the NSQD TCP Endpoint
#   server = "localhost:4150"
#   topic = "telegraf"
#   channel = "consumer"
#   max_in_flight = 100
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   data_format = "influx"


# # Generic socket listener capable of handling multiple socket types.
# [[inputs.socket_listener]]
#   ## URL to listen on
#   # service_address = "tcp://:8094"
#   # service_address = "tcp://127.0.0.1:http"
#   # service_address = "tcp4://:8094"
#   # service_address = "tcp6://:8094"
#   # service_address = "tcp6://[2001:db8::1]:8094"
#   # service_address = "udp://:8094"
#   # service_address = "udp4://:8094"
#   # service_address = "udp6://:8094"
#   # service_address = "unix:///tmp/telegraf.sock"
#   # service_address = "unixgram:///tmp/telegraf.sock"
#
#   ## Maximum number of concurrent connections.
#   ## Only applies to stream sockets (e.g. TCP).
#   ## 0 (default) is unlimited.
#   # max_connections = 1024
#
#   ## Read timeout.
#   ## Only applies to stream sockets (e.g. TCP).
#   ## 0 (default) is unlimited.
#   # read_timeout = "30s"
#
#   ## Maximum socket buffer size in bytes.
#   ## For stream sockets, once the buffer fills up, the sender will start backing up.
#   ## For datagram sockets, once the buffer fills up, metrics will start dropping.
#   ## Defaults to the OS default.
#   # read_buffer_size = 65535
#
#   ## Period between keep alive probes.
#   ## Only applies to TCP sockets.
#   ## 0 disables keep alive probes.
#   ## Defaults to the OS configuration.
#   # keep_alive_period = "5m"
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   # data_format = "influx"


# # Statsd UDP/TCP Server
# [[inputs.statsd]]
#   ## Protocol, must be "tcp" or "udp" (default=udp)
#   protocol = "udp"
#
#   ## MaxTCPConnection - applicable when protocol is set to tcp (default=250)
#   max_tcp_connections = 250
#
#   ## Address and port to host UDP listener on
#   service_address = ":8125"
#
#   ## The following configuration options control when telegraf clears it's cache
#   ## of previous values. If set to false, then telegraf will only clear it's
#   ## cache when the daemon is restarted.
#   ## Reset gauges every interval (default=true)
#   delete_gauges = true
#   ## Reset counters every interval (default=true)
#   delete_counters = true
#   ## Reset sets every interval (default=true)
#   delete_sets = true
#   ## Reset timings & histograms every interval (default=true)
#   delete_timings = true
#
#   ## Percentiles to calculate for timing & histogram stats
#   percentiles = [90]
#
#   ## separator to use between elements of a statsd metric
#   metric_separator = "_"
#
#   ## Parses tags in the datadog statsd format
#   ## http://docs.datadoghq.com/guides/dogstatsd/
#   parse_data_dog_tags = false
#
#   ## Statsd data translation templates, more info can be read here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md#graphite
#   # templates = [
#   #     "cpu.* measurement*"
#   # ]
#
#   ## Number of UDP messages allowed to queue up, once filled,
#   ## the statsd server will start dropping packets
#   allowed_pending_messages = 10000
#
#   ## Number of timing/histogram values to track per-measurement in the
#   ## calculation of percentiles. Raising this limit increases the accuracy
#   ## of percentiles but also increases the memory usage and cpu time.
#   percentile_limit = 1000


# # Stream a log file, like the tail -f command
# [[inputs.tail]]
#   ## files to tail.
#   ## These accept standard unix glob matching rules, but with the addition of
#   ## ** as a "super asterisk". ie:
#   ##   "/var/log/**.log"  -> recursively find all .log files in /var/log
#   ##   "/var/log/*/*.log" -> find all .log files with a parent dir in /var/log
#   ##   "/var/log/apache.log" -> just tail the apache log file
#   ##
#   ## See https://github.com/gobwas/glob for more examples
#   ##
#   files = ["/var/mymetrics.out"]
#   ## Read file from beginning.
#   from_beginning = false
#   ## Whether file is a named pipe
#   pipe = false
#
#   ## Data format to consume.
#   ## Each data format has its own unique set of configuration options, read
#   ## more about them here:
#   ## https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
#   data_format = "influx"


# # Generic TCP listener
# [[inputs.tcp_listener]]
#   # DEPRECATED: the TCP listener plugin has been deprecated in favor of the
#   # socket_listener plugin
#   # see https://github.com/influxdata/telegraf/tree/master/plugins/inputs/socket_listener


# # Generic UDP listener
# [[inputs.udp_listener]]
#   # DEPRECATED: the TCP listener plugin has been deprecated in favor of the
#   # socket_listener plugin
#   # see https://github.com/influxdata/telegraf/tree/master/plugins/inputs/socket_listener


# # A Webhooks Event collector
# [[inputs.webhooks]]
#   ## Address and port to host Webhook listener on
#   service_address = ":1619"
#
#   [inputs.webhooks.filestack]
#     path = "/filestack"
#
#   [inputs.webhooks.github]
#     path = "/github"
#     # secret = ""
#
#   [inputs.webhooks.mandrill]
#     path = "/mandrill"
#
#   [inputs.webhooks.rollbar]
#     path = "/rollbar"
#
#   [inputs.webhooks.papertrail]
#     path = "/papertrail"


# # This plugin implements the Zipkin http server to gather trace and timing data needed to troubleshoot latency problems in microservice architectures.
# [[inputs.zipkin]]
#   # path = "/api/v1/spans" # URL path for span data
#   # port = 9411            # Port on which Telegraf listens


````


## EXACT ATTACHMENT METADATA

````json
{
  "id": "218759800",
  "type": "attachment",
  "status": "current",
  "title": "monitoring-stack_2024xRefresh2.zip",
  "version": {
    "by": {
      "type": "known",
      "username": "agnpal",
      "userKey": "ff80808151426f0e0151af8b0d360002",
      "profilePicture": {
        "path": "/download/attachments/6598412/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Agne P.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151426f0e0151af8b0d360002"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2025-03-18T14:15:47.773+01:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/218759800/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/218759800"
    }
  },
  "position": -1,
  "container": {
    "id": "218759799",
    "type": "page",
    "status": "current",
    "title": "Installation using scripts",
    "position": 0,
    "extensions": {
      "position": 0
    },
    "_links": {
      "webui": "/spaces/MCS2024xR2/pages/218759799/Installation+using+scripts",
      "edit": "/pages/resumedraft.action?draftId=218759799",
      "tinyui": "/x/dwIKDQ",
      "self": "https://docs.nomagic.com/rest/api/content/218759799"
    },
    "_expandable": {
      "container": "/rest/api/space/MCS2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/218759799/child",
      "restrictions": "/rest/api/content/218759799/restriction/byOperation",
      "history": "/rest/api/content/218759799/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/218759799/descendant",
      "space": "/rest/api/space/MCS2024xR2",
      "relevantViewRestrictions": "/rest/api/content/218759799/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 55580,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/218759799/monitoring-stack_2024xRefresh2.zip?version=1&modificationDate=1742303747773&api=v2",
    "webui": "/spaces/MCS2024xR2/pages/218759799/Installation+using+scripts?preview=%2F218759799%2F218759800%2Fmonitoring-stack_2024xRefresh2.zip",
    "self": "https://docs.nomagic.com/rest/api/content/218759800"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/218759800/child",
    "restrictions": "/rest/api/content/218759800/restriction/byOperation",
    "history": "/rest/api/content/218759800/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/218759800/descendant",
    "space": "/rest/api/space/MCS2024xR2",
    "relevantViewRestrictions": "/rest/api/content/218759800/restriction/relevantViewRestrictions"
  }
}
````
