function createPropertiesFile(){
	str = 
@'{
	"port": 91193
}
';

	return str;
}

function initialiseServer(){
	fname = program_directory + "properties.json";

	if !file_exists(fname) {
		file = file_text_open_write(fname);
	
		file_text_write_string(file, createPropertiesFile());
	
		file_text_close(file);
	}

	file = file_text_open_read(fname);

	data = json_decode(file_text_read_string(file));

	file_text_close(file);
}
