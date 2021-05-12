/*
 * lakeFS API
 * lakeFS HTTP API
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package io.lakefs.clients.api;

import io.lakefs.clients.api.ApiException;
import io.lakefs.clients.api.model.ActionRun;
import io.lakefs.clients.api.model.ActionRunList;
import io.lakefs.clients.api.model.Error;
import java.io.File;
import io.lakefs.clients.api.model.HookRunList;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ActionsApi
 */
@Ignore
public class ActionsApiTest {

    private final ActionsApi api = new ActionsApi();

    
    /**
     * get a run
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunTest() throws ApiException {
        String repository = null;
        String runId = null;
        ActionRun response = api.getRun(repository, runId);

        // TODO: test validations
    }
    
    /**
     * get run hook output
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRunHookOutputTest() throws ApiException {
        String repository = null;
        String runId = null;
        String hookRunId = null;
        File response = api.getRunHookOutput(repository, runId, hookRunId);

        // TODO: test validations
    }
    
    /**
     * list runs
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listRepositoryRunsTest() throws ApiException {
        String repository = null;
        String after = null;
        Integer amount = null;
        String branch = null;
        String commit = null;
        ActionRunList response = api.listRepositoryRuns(repository, after, amount, branch, commit);

        // TODO: test validations
    }
    
    /**
     * list run hooks
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listRunHooksTest() throws ApiException {
        String repository = null;
        String runId = null;
        String after = null;
        Integer amount = null;
        HookRunList response = api.listRunHooks(repository, runId, after, amount);

        // TODO: test validations
    }
    
}