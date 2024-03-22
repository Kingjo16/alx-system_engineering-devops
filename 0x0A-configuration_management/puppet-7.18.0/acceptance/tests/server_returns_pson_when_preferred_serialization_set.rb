test_name "C100532: Server returns expected format when --preferred_serialization_format is set" do

  tag 'risk:high',
      'audit:high',
      'audit:integration',
      'server'

  with_puppet_running_on(master, :main => {}) do
    formats = ['pson', 'json']
    formats.each do |expected_format|
      step "Server returns #{expected_format} catalog when --preferred_serialization_format=#{expected_format}" do
        agents.each do |agent|
          # We use :silent here to avoid raw http_debug bytes being printed to our CI logs
          on(agent, puppet('agent', '-t',
                           "--preferred_serialization_format #{expected_format}",
                           '--http_debug'),
                    :acceptable_exit_codes => [0,2], :silent => true) do |res|
            found_format = false
            started = false
            res.stderr.each_line do |line|
              # Expected content-type should be in the headers of the incomming
              # HTTP payload returned by the server between the outgoing POST
              # request for the catalog and the application of the returned catalog.
              started = true if line =~ /<- "POST \/puppet\/v[3-9]\/catalog/
              next unless started
              found_format = true if line =~ /-> "Content-Type: .*\/#{expected_format}/
              break if line =~ /Notice: Applied catalog in/
            end
            fail_test("Catalog was not returned in #{expected_format} format") unless found_format == true
          end
        end
      end
    end
  end

end
