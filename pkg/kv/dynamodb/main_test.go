package dynamodb_test

import (
	"encoding/json"
	"log"
	"os"
	"testing"

	nanoid "github.com/matoous/go-nanoid/v2"
	"github.com/treeverse/lakefs/pkg/kv/dynamodb"
)

const chars = "abcdef1234567890"

var (
	dsn string
)

func testUniqueTableName() string {
	return "kvstore_test_" + nanoid.MustGenerate(chars, 8)
}

func TestMain(m *testing.M) {
	//databaseURI, cleanpFunc, err := testutil.RunLocalDynamoDBInstance()
	//if err != nil {
	//	log.Fatalf("Could not connect to Docker: %s", err)
	//}

	testParams := &dynamodb.Params{
		TableName:          testUniqueTableName(),
		ReadCapacityUnits:  1000,
		WriteCapacityUnits: 1000,
		ScanLimit:          10,
		//Endpoint:           databaseURI,
		AwsRegion:          "us-east-1",
		AwsAccessKeyID:     "fakeMyKeyId",
		AwsSecretAccessKey: "fakeSecretAccessKey",
	}

	dsnBytes, err := json.Marshal(testParams)
	if err != nil {
		log.Fatalf("Failed to initalize tests params :%s", err)
	}

	dsn = string(dsnBytes)

	code := m.Run()
	//cleanpFunc()
	os.Exit(code)
}
