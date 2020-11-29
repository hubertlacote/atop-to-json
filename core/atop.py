import re

# Valid for Atop 2.5.0 - see atop(1)
MAPPING = {

    "CPU": [
        "", "", "epoch", "", "", "interval",
        "ticks_per_second",
        "processor_count",
        "cpu_system_ticks",
        "cpu_user_ticks",
        "cpu_user_niced_ticks",
        "cpu_idle_ticks",
        "cpu_wait_ticks",
        "cpu_irq_ticks",
        "cpu_soft_irq_ticks",
        "cpu_steal_ticks",
        "cpu_guest_ticks",
        "frequency",
        "frequency_percentage",
        "instructions_executed",
        "cycles"
    ],

    "cpu": [
        "", "", "epoch", "", "", "interval",
        "ticks_per_second",
        "processor_id",
        "cpu_system_ticks",
        "cpu_user_ticks",
        "cpu_user_niced_ticks",
        "cpu_idle_ticks",
        "cpu_wait_ticks",
        "cpu_irq_ticks",
        "cpu_soft_irq_ticks",
        "cpu_steal_ticks",
        "cpu_guest_ticks",
        "frequency",
        "frequency_percentage",
        "instructions_executed",
        "cycles"
    ],

    "CPL": [
        "", "", "epoch", "", "", "interval",
        "processor_count",
        "load_average_last_1_min",
        "load_average_last_5_min",
        "load_average_last_15_min",
        "context_switches_count",
        "device_interrupts"
    ],

    "GPU": [
        "", "", "epoch", "", "", "interval",
        "gpu_number",
        "bus_id",
        "gpu_string",
        "gpu_busy_percentage_last_1_sec",
        "memory_busy_percentage_last_1_sec",
        "total_memory_kilo_bytes",
        "used_memory_kilo_bytes",
        "sample_count",
        "gpu_busy_percentage",
        "memory_busy_percentage",
        "memory_occupation"
    ],

    "MEM": [
        "", "", "epoch", "", "", "interval",
        "page_size_bytes",
        "physical_memory_pages",
        "free_memory_pages",
        "page_cache_pages",
        "buffer_cache_pages",
        "slab_pages",
        "dirty_pages",
        "slab_reclaimable_pages",
        "vmware_balloon_pages",
        "shared_memory_pages",
        "resident_memory_pages",
        "swapped_shared_memory_pages",
        "huge_page_size_bytes",
        "huge_pages_count",
        "free_huge_pages"
    ],

    "SWP": [
        "", "", "epoch", "", "", "interval",
        "page_size_bytes",
        "swap_size_pages",
        "free_swap_size_pages",
        "",
        "committed_space_pages",
        "committed_space_limit_pages"
    ],

    "PAG": [
        "", "", "epoch", "", "", "interval",
        "page_size_bytes",
        "page_scan_count",
        "allocstalls_count",
        "",
        "swapins",
        "swapouts"
    ],

    "PSI": [
        "", "", "epoch", "", "", "interval",
        "psi_statistics_available",
        "cpu_some_avg10",
        "cpu_some_avg60",
        "cpu_some_avg300",
        "cpu_some_micro_secs",
        "memory_some_avg10",
        "memory_some_avg60",
        "memory_some_avg300",
        "memory_some_micro_secs",
        "memory_full_avg10",
        "memory_full_avg60",
        "memory_full_avg300",
        "memory_full_micro_secs",
        "io_some_avg10",
        "io_some_avg60",
        "io_some_avg300",
        "io_some_micro_secs",
        "io_full_avg10",
        "io_full_avg60",
        "io_full_avg300",
        "io_full_micro_secs"
    ],

    "LVM": [
        "", "", "epoch", "", "", "interval",
        "name",
        "io_spent_ms",
        "reads_count",
        "sectors_read",
        "writes_count",
        "sectors_write"
    ],

    "MDD": [
        "", "", "epoch", "", "", "interval",
        "name",
        "io_spent_ms",
        "reads_count",
        "sectors_read",
        "writes_count",
        "sectors_write"
    ],

    "DSK": [
        "", "", "epoch", "", "", "interval",
        "name",
        "io_spent_ms",
        "reads_count",
        "sectors_read",
        "writes_count",
        "sectors_write"
    ],

    "NFM": [
        "", "", "epoch", "", "", "interval",
        "mounted_nfs_fs",
        "read_bytes",
        "written_bytes",
        "system_calls_bytes_read",
        "system_calls_bytes_written",
        "direct_io_bytes_read",
        "direct_io_bytes_written",
        "memory_mapped_io_pages_read",
        "memory_mapped_io_pages_written"
    ],

    "NFC": [
        "", "", "epoch", "", "", "interval",
        "transmitted_rpcs",
        "transmitted_read_rpcs",
        "transmitted_write_rpcs",
        "retransmitted_rpcs",
        "authorization_refreshes",
    ],

    "NFS": [
        "", "", "epoch", "", "", "interval",
        "handled_rpcs",
        "received_read_rpcs",
        "received_write_rpcs",
        "bytes_read_by_clients",
        "bytes_written_by_clients",
        "rpcs_with_bad_format",
        "rpcs_with_bad_authorization",
        "rpcs_from_bad_client",
        "handled_network_requests",
        "tcp_handled network requests",
        "udp_handled network requests",
        "tcp_connections",
        "reply_cache_hits",
        "reply_cache_misses",
        "uncached_requests"
    ],

    "NET-upper": [
        "", "", "epoch", "", "", "interval",
        "",
        "tcp_packets_received",
        "tcp_packets_sent",
        "udp_packets_received",
        "udp_packets_sent",
        "ip_packets_received",
        "ip_packets_sent",
        "ip_packets_delivered_to_higher_layers",
        "ip_packets_forwarded"
    ],

    "NET": [
        "", "", "epoch", "", "", "interval",
        "interface",
        "packets_received",
        "bytes_received",
        "packets_sent",
        "bytes_sent",
        "interface_speed",
        "duplex_mode"
    ],

    "IFB": [
        "", "", "epoch", "", "", "interval",
        "interface",
        "port_number",
        "lanes",
        "maximum_rate_mega_bps",
        "bytes_received",
        "bytes_sent",
        "packets_received",
        "packets_transmitted"
    ],

    "PRG": [
        "", "", "epoch", "", "", "interval",
        "pid",
        "name",
        "state",
        "real_uid",
        "real_gid",
        "tgid",
        "thread_count",
        "exit_code",
        "start_time_epoch",
        "command_line",
        "ppid",
        "running_threads",
        "interruptible_sleeping_threads",
        "uninterruptible_sleeping_threads",
        "effective_uid",
        "effective_gid",
        "saved_uid",
        "saved_gid",
        "filesystem_uid",
        "filesystem_gid",
        "elasped_time_hertz",
        "is_process",
        "openvz_vpid",
        "openvz_container_id",
        "docker_container_id"
    ],

    "PRC": [
        "", "", "epoch", "", "", "interval",
        "pid",
        "name",
        "state",
        "clock_ticks_per_second",
        "cpu_user",
        "cpu_system",
        "nice_value",
        "priority",
        "realtime_priority",
        "scheduling_policy",
        "current_cpu_id",
        "sleep_average",
        "tgid",
        "is_process"],

    "PRE": [
        "", "", "epoch", "", "", "interval",
        "pid",
        "name",
        "process_state",
        "gpu_state",
        "gpus_used",
        "used_gpus",
        "gpu_busy_percentage",
        "memory_occupation_kilo_bytes",
        "samples_taken"
    ],

    "PRM": [
        "", "", "epoch", "", "", "interval",
        "pid",
        "name",
        "state",
        "page_size_bytes",
        "virtual_memory_size_kilo_bytes",
        "resident_memory_size_kilo_bytes",
        "shared_text_memory_size_kilo_bytes",
        "virtual_memory_growth_kilo_bytes",
        "resident_memory_growth_kilo_bytes",
        "minor_page_faults",
        "major_page_faults",
        "virtual_library_exec_size_kilo_bytes",
        "virtual_data_size_kilo_bytes",
        "virtual_stack_size_kilo_bytes",
        "swap_space_used_kilo_bytes",
        "tgid",
        "is_process",
        "pss_kilo_bytes"
    ],

    "PRD": [
        "", "", "epoch", "", "", "interval",
        "pid",
        "name",
        "state",
        "obsoleted_kernel_patch",
        "standard_io_stats_used",
        "read_count",
        "read_sectors",
        "write_count",
        "written_sectors",
        "cancelled_written_sectors",
        "tgid",
        "is_process"
    ],

    "PRN": [
        "", "", "epoch", "", "", "interval",
        "pid",
        "name",
        "state",
        "kernel_module_loaded",
        "tcp_packets_sent",
        "tcp_packets_size_sent",
        "tcp_packets_received",
        "tcp_packets_size_received",
        "udp_packets_sent",
        "udp_packets_size_sent",
        "udp_packets_received",
        "udp_packets_size_received",
        "",
        "",
        "tgid",
        "is_process"
    ]
}

# The NET lines can convey two different types of information
# The interface field allows to distiguish between "upper" layer
# and other interfaces.
#
# See atop(1):
#
#     First one line is produced for the upper layers of the TCP/IP stack.
#     Next one line is shown for every interface.
#
NET_INTERFACE_FIELD = 6


def split_line(line):
    """
    >>> split_line(
    ... 'FOO host-name 2020/11/28 19:10:33 (Descriptive Name-1) 123 () 10 '
    ... '(Other name-2) 20 -')
    ['FOO', 'host-name', '2020/11/28', '19:10:33', '(Descriptive Name-1)', \
'123', '()', '10', '(Other name-2)', '20', '-']
    """
    # Fields are space separated and
    # process names / arguments are enclosed in brackets
    fields = re.findall(r"\([^\(]+\)|[^ ]+", line)
    return fields
