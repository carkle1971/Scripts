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

def parse_pure_arraydetails(string_table):
	section = {}
	for row in string_table:
		(item, data_reduction, total_reduction, shared_space, thin_provisioning, snapshots, volumes)  = row

		
		try:
			data_reduction = (data_reduction)
		except ValueError:
			data_reduction = 0
		try:
			total_reduction = (total_reduction)
		except ValueError:
			total_reduction = 0		 
		try:
			shared_space = int(shared_space)
		except ValueError:
			shared_space = 0
		try:
			thin_provisioning = (thin_provisioning)
		except ValueError:
			thin_provisioning = 0
		try:
			snapshots = int(snapshots)
		except ValueError:
			snapshots = 0
		try:
			volumes = int(volumes)
		except ValueError:
			volumes = 0 

		section[item] = {
			'data_reduction': data_reduction,
			'total_reduction': total_reduction,
			'shared_space': shared_space,
			'thin_provisioning': thin_provisioning,
			'snapshots': snapshots,
			'volumes': volumes,
		}
	return section

register.agent_section(
	name="pure_arraydetails",
	parse_function=parse_pure_arraydetails,
)

def discovery_pure_arraydetails(section):
	for item in section.keys():
		yield Service(item=item)

def check_pure_arraydetails(item, section):
	failed = []

	if item not in section.keys():
		yield Result(
			state=State.UNKNOWN,
			summary=f"Item {item} not found",
		)

	data = section[item]
	dedup_ratio = (data['data_reduction'])
	perfdata = True
	if item in section.keys():
		yield Result(
			state=State.OK,
			summary=f"Data Reduction: {data['data_reduction']} to 1, Total reduction: {(data['total_reduction'])} to 1, Shared Space: {render.bytes(data['shared_space'])}, Thin Provisioned: {data['thin_provisioning']}, Snapshots: {render.bytes(data['snapshots'])}",
			details=f"Used after deduplication: {render.bytes(data['volumes'])}",
		)

# Metrics
	if perfdata == True:
		yield Metric("dedup_ratio", float(dedup_ratio))


register.check_plugin(
	name="pure_arraydetails",
	service_name="Filesystem %s Details",
	discovery_function=discovery_pure_arraydetails,
	check_function=check_pure_arraydetails,
)