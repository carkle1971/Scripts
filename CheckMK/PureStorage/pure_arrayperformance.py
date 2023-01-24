# 2021 created by Sven Rueß, sritd.de
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based
#bytes_per_mirrored_write (int) – The average I/O size per mirrored write. Measured in bytes.
#bytes_per_op (int) – The average I/O size for both read and write (all) operations.
#bytes_per_read (int) – The average I/O size per read. Measured in bytes.
#bytes_per_write (int) – The average I/O size per write. Measured in bytes.
#mirrored_write_bytes_per_sec (int) – The number of mirrored bytes written per second.
#mirrored_writes_per_sec (int) – The number of mirrored writes per second.
#qos_rate_limit_usec_per_mirrored_write_op (int) – The average time it takes the array to process a mirrored I/O write request. Measured in microseconds.
#qos_rate_limit_usec_per_read_op (int) – The average time spent waiting due to QoS rate limiting for a read request. Measured in microseconds.
#qos_rate_limit_usec_per_write_op (int) – The average time that a write I/O request spends waiting as a result of the volume reaching its QoS bandwidth limit. Measured in microseconds.
#queue_usec_per_mirrored_write_op (int) – The average time that a mirrored write I/O request spends in the array waiting to be served. Measured in microseconds.
#queue_usec_per_read_op (int) – The average time that a read I/O request spends in the array waiting to be served. Measured in microseconds.
#queue_usec_per_write_op (int) – The average time that a write I/O request spends in the array waiting to be served. Measured in microseconds.
#read_bytes_per_sec (int) – The number of bytes read per second.
#reads_per_sec (int) – The number of read requests processed per second.
#san_usec_per_mirrored_write_op (int) – The average time required to transfer data from the initiator to the array for a mirrored write request. Measured in microseconds.
#san_usec_per_read_op (int) – The average time required to transfer data from the array to the initiator for a read request. Measured in microseconds.
#san_usec_per_write_op (int) – The average time required to transfer data from the initiator to the array for a write request. Measured in microseconds.
#service_usec_per_mirrored_write_op (int) – The average time required for the array to service a mirrored write request. Measured in microseconds.
#service_usec_per_read_op (int) – The average time required for the array to service a read request. Measured in microseconds.
#service_usec_per_write_op (int) – The average time required for the array to service a write request. Measured in microseconds.
#time (int) – The time when the sample performance data was taken. Measured in milliseconds since the UNIX epoch.
#usec_per_mirrored_write_op (int) – The average time it takes the array to process a mirrored I/O write request. Measured in microseconds. The average time does not include SAN time, queue time, or QoS rate limit time.
#usec_per_read_op (int) – The average time it takes the array to process an I/O read request. Measured in microseconds. The average time does not include SAN time, queue time, or QoS rate limit time.
#usec_per_write_op (int) – The average time it takes the array to process an I/O write request. Measured in microseconds. The average time does not include SAN time, queue time, or QoS rate limit time.
#write_bytes_per_sec (int) – The number of bytes written per second.
#writes_per_sec (int) – The number of write requests processed per second.
#service_usec_per_read_op_cache_reduction (float) – The percentage reduction in service_usec_per_read_op due to data cache hits. For example, a value of 0.25 indicates that the value of service_usec_per_read_op is 25&#37; #lower than it would have been without any data cache hits.
#id (str) – A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
#name (str) – A locally unique, system-generated name. The name cannot be modified.
#queue_depth (int) – Deprecated. The number displayed here may not be accurate and in later versions of the product this field will always display null. Instead, use queue_usec_per_mirrored_write_op, queue_usec_per_read_op, #and queue_usec_per_write_op fields to measure IO queuing.
#local_queue_usec_per_op (int) – Average local queue time for both read and write operations, measured in microseconds.
#usec_per_other_op (int) – The average time it takes the array to process an I/O other request, measured in microseconds. The average time does not include SAN time, queue time, or QoS rate limit time.
#others_per_sec (int) – The number of other requests processed per second.

from .agent_based_api.v1 import (
	register,
	Service,
	Result,
	State,
	Metric,
	render,
)

def parse_pure_arrayperformance(string_table):
	section = {}
	for row in string_table:
		(item, reads_per_sec, writes_per_sec, output_per_sec, input_per_sec, usec_per_read_op, usec_per_write_op)  = row

		section[item] = {
			'reads_per_sec': reads_per_sec,
			'writes_per_sec': writes_per_sec,
			'output_per_sec': output_per_sec,
			'input_per_sec': input_per_sec,
			'usec_per_read_op': usec_per_read_op,
			'usec_per_write_op': usec_per_write_op,        
		}
	return section

register.agent_section(
	name="pure_arrayperformance",
	parse_function=parse_pure_arrayperformance,
)

def discovery_pure_arrayperformance(section):
	for item in section.keys():
		yield Service(item=item)

def check_pure_arrayperformance(item, section):
	failed = []

	if item not in section.keys():
		yield Result(
			state=State.UNKNOWN,
			summary=f"Item {item} not found",
		)

	data = section[item]
	disk_read_ios = (data['reads_per_sec'])
	disk_write_ios = (data['writes_per_sec'])
	disk_read_throughput = (data['output_per_sec'])
	disk_write_throughput = (data['input_per_sec'])
	disk_read_responsetime = (data['usec_per_read_op'])
	disk_write_responsetime = (data['usec_per_write_op'])
	perfdata = True

	if item in section.keys():
		yield Result(state=State.OK, notice = f"Read latency: {data['reads_per_sec']}\n \
			Write latency: {data['writes_per_sec']}\n \
			Flash Volume: Yes")

# Metrics
	if perfdata == True:
		yield Metric("disk_read_ios", int(disk_read_ios))
		yield Metric("disk_write_ios", int(disk_write_ios))
		yield Metric("disk_read_throughput", int(disk_read_throughput))
		yield Metric("disk_write_throughput", int(disk_write_throughput))
		yield Metric("read_latency", int(disk_read_responsetime))
		yield Metric("write_latency", int(disk_write_responsetime))
		state = State.OK
		message = f"Read: {render.bytes(data['output_per_sec'])}, Write: {render.bytes(data['input_per_sec'])}, Read operations: {data['reads_per_sec']}/s, Write operations: {data['writes_per_sec']}/s"
		yield Result(state=State(state), summary=message)


register.check_plugin(
	name="pure_arrayperformance",
	service_name="Filesystem %s Performance",
	discovery_function=discovery_pure_arrayperformance,
	check_function=check_pure_arrayperformance,
)