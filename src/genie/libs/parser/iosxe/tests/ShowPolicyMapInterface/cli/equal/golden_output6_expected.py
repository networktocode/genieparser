expected_output = {
    "serial3/1": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "pol": {
                        "class_map": {
                            "silver": {
                                "match_evaluation": "match-all",
                                "packets": 366,
                                "bytes": 87840,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 15000,
                                    "drop_rate_bps": 300,
                                },
                                "match": ["ip precedence 1"],
                                "queueing": True,
                                "output_queue": "Conversation 266",
                                "bandwidth_percent": 10,
                                "pkts_matched": 363,
                                "bytes_matched": 87120,
                                "queue_depth": 147,
                                "total_drops": 38,
                                "no_buffer_drops": 0,
                                "random_detect": {
                                    "exponential_weight": "9",
                                    "mean_queue_depth": 25920,
                                    "class": {
                                        "0": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "20000",
                                            "maximum_thresh": "40000",
                                            "mark_prob": "1/10",
                                        },
                                        "1": {
                                            "transmitted": "328/78720",
                                            "random_drop": "38/9120",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "22000",
                                            "maximum_thresh": "40000",
                                            "mark_prob": "1/10",
                                        },
                                        "2": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "24000",
                                            "maximum_thresh": "40000",
                                            "mark_prob": "1/10",
                                        },
                                        "3": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "26000",
                                            "maximum_thresh": "40000",
                                            "mark_prob": "1/10",
                                        },
                                        "4": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "28000",
                                            "maximum_thresh": "40000",
                                            "mark_prob": "1/10",
                                        },
                                    },
                                },
                                "policy": {
                                    "wred-policy": {
                                        "class": {
                                            "prec2": {
                                                "bandwidth": 1000,
                                                "random_detect": {
                                                    "precedence": [2],
                                                    "bytes1": [100],
                                                    "bytes2": [200],
                                                    "bytes3": [10],
                                                },
                                            },
                                            "class-default": {
                                                "random_detect": {
                                                    "precedence": [4, 6],
                                                    "bytes1": [150, 200],
                                                    "bytes2": [300, 400],
                                                    "bytes3": [15, 5],
                                                }
                                            },
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            }
        }
    },
    "Ethernet0/0/1": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "wred-policy (1177)": {
                        "class_map": {
                            "prec2": {
                                "match_evaluation": "match-all 1178/10",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["ip precedence 2  (1179)"],
                                "queueing": True,
                                "queue_limit_bytes": 62500,
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_queued": 0,
                                "bytes_queued": 0,
                                "bandwidth_kbps": 1000,
                                "random_detect": {
                                    "exp_weight_constant": "9 (1/512)",
                                    "mean_queue_depth": 0,
                                    "class": {
                                        "0": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "15625",
                                            "maximum_thresh": "31250",
                                            "mark_prob": "1/10",
                                        },
                                        "1": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "17578",
                                            "maximum_thresh": "31250",
                                            "mark_prob": "1/10",
                                        },
                                        "2": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "100",
                                            "maximum_thresh": "200",
                                            "mark_prob": "1/10",
                                        },
                                        "3": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "21484",
                                            "maximum_thresh": "31250",
                                            "mark_prob": "1/10",
                                        },
                                        "4": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "23437",
                                            "maximum_thresh": "31250",
                                            "mark_prob": "1/10",
                                        },
                                        "5": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "25390",
                                            "maximum_thresh": "31250",
                                            "mark_prob": "1/10",
                                        },
                                        "6": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "27343",
                                            "maximum_thresh": "31250",
                                            "mark_prob": "1/10",
                                        },
                                        "7": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "29296",
                                            "maximum_thresh": "31250",
                                            "mark_prob": "1/10",
                                        },
                                    },
                                },
                            },
                            "class-default": {
                                "match_evaluation": "match-any 1182/0",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any  (1183)"],
                                "queue_limit_bytes": 562500,
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_queued": 0,
                                "bytes_queued": 0,
                                "random_detect": {
                                    "exp_weight_constant": "9 (1/512)",
                                    "mean_queue_depth": 0,
                                    "class": {
                                        "0": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "140625",
                                            "maximum_thresh": "281250",
                                            "mark_prob": "1/10",
                                        },
                                        "1": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "158203",
                                            "maximum_thresh": "281250",
                                            "mark_prob": "1/10",
                                        },
                                        "2": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "175781",
                                            "maximum_thresh": "281250",
                                            "mark_prob": "1/10",
                                        },
                                        "3": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "193359",
                                            "maximum_thresh": "281250",
                                            "mark_prob": "1/10",
                                        },
                                        "4": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "150",
                                            "maximum_thresh": "300",
                                            "mark_prob": "1/15",
                                        },
                                        "5": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "228515",
                                            "maximum_thresh": "281250",
                                            "mark_prob": "1/10",
                                        },
                                        "6": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "200",
                                            "maximum_thresh": "400",
                                            "mark_prob": "1/5",
                                        },
                                        "7": {
                                            "transmitted": "0/0",
                                            "random_drop": "0/0",
                                            "tail_drop": "0/0",
                                            "minimum_thresh": "263671",
                                            "maximum_thresh": "281250",
                                            "mark_prob": "1/10",
                                        },
                                    },
                                },
                            },
                        }
                    }
                }
            }
        }
    },
}
