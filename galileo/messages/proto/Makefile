all:
	mkdir -p ./../java/src/main/java
	protoc $(wildcard *.proto) --python_out=./../py --cpp_out=./../c --java_out=./../java/src/main/java --proto_path=/apps/site-packages/control/messages/proto --proto_path=.
py:
	protoc $(wildcard *.proto) --python_out=./../py --proto_path=/apps/site-packages/control/messages/proto/ --proto_path=.
cc:
	protoc $(wildcard *.proto) --cpp_out=./../c --proto_path=/apps/site-packages/control/messages/proto/ --proto_path=.
java:
	mkdir -p ./../java/src/main/java
	protoc $(wildcard *.proto) --java_out=./../java/src/main/java --proto_path=/apps/site-packages/control/messages/proto/ --proto_path=.
