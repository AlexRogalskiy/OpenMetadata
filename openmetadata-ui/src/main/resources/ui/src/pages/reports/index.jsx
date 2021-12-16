/*
 *  Copyright 2021 Collate
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *  http://www.apache.org/licenses/LICENSE-2.0
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

import React from 'react';
import PageContainer from '../../components/containers/PageContainer';
import ReportCard from '../../components/reports/ReportCard';
import { mockData } from './index.mock';

const ReportsPage = () => {
  return (
    <PageContainer>
      <div className="container-fluid">
        <div className="row">
          <div className="col-sm-12">
            {mockData.map((reportDetails) => {
              return (
                <ReportCard
                  key={reportDetails.dataId}
                  reportDetails={reportDetails}
                />
              );
            })}
          </div>
        </div>
      </div>
    </PageContainer>
  );
};

export default ReportsPage;