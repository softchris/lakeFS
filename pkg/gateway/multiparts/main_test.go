package multiparts_test

import (
	"encoding/json"
	"flag"
	"log"
	"os"
	"testing"

	"github.com/ory/dockertest/v3"
	"github.com/treeverse/lakefs/pkg/kv/dynamodb"
	_ "github.com/treeverse/lakefs/pkg/kv/mem"
	_ "github.com/treeverse/lakefs/pkg/kv/postgres"
	"github.com/treeverse/lakefs/pkg/logging"
	"github.com/treeverse/lakefs/pkg/testutil"
)

var (
	pool        *dockertest.Pool
	databaseURI string
	dynamoDSN   string
)

func TestMain(m *testing.M) {
	flag.Parse()
	if !testing.Verbose() {
		// keep the log level calm
		logging.SetLevel("panic")
	}

	// postgres container
	var err error
	pool, err = dockertest.NewPool("")
	if err != nil {
		log.Fatalf("Could not connect to Docker: %s", err)
	}
	var closer func()
	databaseURI, closer = testutil.GetDBInstance(pool)

	dynamoURI, cleanupFunc, err := testutil.GetDynamoDBInstance()
	if err != nil {
		log.Fatalf("Could not connect to Docker: %s", err)
	}
	defer cleanupFunc()

	testParams := &dynamodb.Params{
		TableName:          "tracker_kv_store",
		ReadCapacityUnits:  100,
		WriteCapacityUnits: 100,
		ScanLimit:          10,
		Endpoint:           dynamoURI,
		AwsRegion:          "us-east-1",
		AwsAccessKeyID:     "fakeMyKeyId",
		AwsSecretAccessKey: "fakeSecretAccessKey",
	}

	dsnBytes, err := json.Marshal(testParams)
	if err != nil {
		log.Fatalf("Failed to initalize tests params :%s", err)
	}
	dynamoDSN = string(dsnBytes)

	code := m.Run()
	closer() // cleanup
	os.Exit(code)
}
