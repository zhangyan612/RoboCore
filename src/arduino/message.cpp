// Example 5 - Receive with start- and end-markers combined with parsing

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing

// variables to hold the parsed data
char messageFromPC[numChars] = {0};
int command1 = 0;
int command2 = 0;
int command3 = 0;
int command4 = 0;
int command5 = 0;
int command6 = 0;

// float floatFromPC = 0.0;

boolean newData = false;

//============

void setup() {
    Serial.begin(9600);
    Serial.println("This demo expects 3 pieces of data - text, an integer and a floating point value");
    Serial.println("Enter data in this style <Servo, 12, 22, 55, 77, 66, 33>  ");
}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        showParsedData();
        newData = false;
    }
}

//============

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

//============

void parseData() {      // split the data into its parts

    char * strtokIndx; // this is used by strtok() as an index

    strtokIndx = strtok(tempChars,","); // get the first part - the string
    strcpy(messageFromPC, strtokIndx); // copy it to messageFromPC
 
    strtokIndx = strtok(NULL, ",");  // this continues where the previous call left off
    command1 = atoi(strtokIndx);     // convert this part to an integer
    
    strtokIndx = strtok(NULL, ",");
    command2 = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    command3 = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    command4 = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    command5 = atoi(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    command6 = atoi(strtokIndx);

    // strtokIndx = strtok(NULL, ",");
    // floatFromPC = atof(strtokIndx);     // convert this part to a float

}

//============

void showParsedData() {
    Serial.print("Text ");
    Serial.println(messageFromPC);
    Serial.print("Move Commands: ");
    Serial.println(command1);
    Serial.println(command2);
    Serial.println(command3);
    Serial.println(command4);
    Serial.println(command5);
    Serial.println(command6);

    // Serial.print("Float ");
    // Serial.println(floatFromPC);
}
