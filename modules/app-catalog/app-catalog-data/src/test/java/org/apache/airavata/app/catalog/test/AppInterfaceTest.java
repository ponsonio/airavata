/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

package org.apache.airavata.app.catalog.test;

import org.airavata.appcatalog.cpi.AppCatalog;
import org.airavata.appcatalog.cpi.AppCatalogException;
import org.airavata.appcatalog.cpi.ApplicationInterface;
import org.apache.aiaravata.application.catalog.data.impl.AppCatalogFactory;
import org.apache.airavata.app.catalog.test.util.Initialize;
import org.apache.airavata.common.utils.AiravataUtils;
import org.apache.airavata.model.appcatalog.appdeployment.ApplicationModule;
import org.apache.airavata.model.appcatalog.appinterface.ApplicationInterfaceDescription;
import org.apache.airavata.model.appcatalog.appinterface.DataType;
import org.apache.airavata.model.appcatalog.appinterface.InputDataObjectType;
import org.apache.airavata.model.appcatalog.appinterface.OutputDataObjectType;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertTrue;

public class AppInterfaceTest {
    private static Initialize initialize;
    private static AppCatalog appcatalog;

    @Before
    public void setUp() {
        try {
            AiravataUtils.setExecutionAsServer();
            initialize = new Initialize("appcatalog-derby.sql");
            initialize.initializeDB();
            appcatalog = AppCatalogFactory.getAppCatalog();
        } catch (AppCatalogException e) {
            e.printStackTrace();
        }
    }

    @AfterClass
    public static void tearDownAfterClass() throws Exception {
        initialize.stopDerbyServer();
    }

    @Test
    public void testAppInterface(){
        try {
            ApplicationInterface appInterface = appcatalog.getApplicationInterface();

            ApplicationInterfaceDescription description = new ApplicationInterfaceDescription();
            String wrfModuleId = addAppModule("WRF");
            String amberModuleId = addAppModule("AMBER");
            List<String> modules = new ArrayList<String>();
            modules.add(wrfModuleId);
            modules.add(amberModuleId);
            InputDataObjectType appInput1 = createAppInput("input1", "input1", DataType.STRING);
            InputDataObjectType appInput2 = createAppInput("input2", "input2", DataType.INTEGER);
            List<InputDataObjectType> inputs = new ArrayList<InputDataObjectType>();
            inputs.add(appInput1);
            inputs.add(appInput2);
            OutputDataObjectType output1 = createAppOutput("output1", "", DataType.STRING);
            OutputDataObjectType output2 = createAppOutput("output2", "", DataType.STRING);
            List<OutputDataObjectType> outputs = new ArrayList<OutputDataObjectType>();
            outputs.add(output1);
            outputs.add(output2);
            description.setApplicationName("testApplication");
            description.setApplicationModules(modules);
            description.setApplicationInputs(inputs);
            description.setApplicationOutputs(outputs);
            String appID = appInterface.addApplicationInterface(description);
            System.out.println("********** application id ************* : " + appID);
            ApplicationInterfaceDescription ainterface = null;
            if (appInterface.isApplicationInterfaceExists(appID)){
                ainterface = appInterface.getApplicationInterface(appID);
                System.out.println("********** application name ************* : " + ainterface.getApplicationName());
            }
            assertTrue("App interface saved successfully", ainterface != null);

        }catch (AppCatalogException e) {
            e.printStackTrace();
        }

    }

    public String addAppModule (String moduleName){
        try {
            ApplicationModule module = new ApplicationModule();
            module.setAppModuleName(moduleName);
            module.setAppModuleVersion("1.0.0");
            module.setAppModuleDescription("WeatherForcast");
            return appcatalog.getApplicationInterface().addApplicationModule(module);
        } catch (AppCatalogException e) {
            e.printStackTrace();
        }
        return null;
    }

    public InputDataObjectType createAppInput (String inputName, String value, DataType type ){
        InputDataObjectType input = new InputDataObjectType();
        input.setName(inputName);
        input.setValue(value);
        input.setType(type);
        input.setApplicationArguement("test arg");
        return input;
    }

    public OutputDataObjectType createAppOutput (String inputName, String value, DataType type ){
        OutputDataObjectType outputDataObjectType = new OutputDataObjectType();
        outputDataObjectType.setName(inputName);
        outputDataObjectType.setValue(value);
        outputDataObjectType.setType(type);
        return outputDataObjectType;
    }
}