# NI_LABVIEW_PROGRAMMING_REFERENCE

<!--SYSTEM_CORPUS id=NI_LABVIEW_PROGRAMMING_REFERENCE format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW Programming Reference Manual
- source: https://docs-be.ni.com/bundle/labview-api-ref/preprocessedpdf/enus
- source_sha256: 7a54c389b4f3d78e2215f55c9f156124d3668ce61d0d5018094e356004d895ac
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5501 ordinal=5501 -->
## Functions

Functions


 Palette            Description
 Object

 Message   Use the Message Queue VIs to launch and communicate with the top-level actor in your
 Queue      application.


 Init Actor   Provides access the To-Self and To-Caller message queues for an actor without
 Queues    launching the actor.
 FOR
 TESTING   Use this VI to test how an actor handles messages. Do not use this VI in code that you
 ONLY VI    deploy.


 Generate   Generates a DETT (Desktop Execution Trace Toolkit) User Generated Trace. The trace
 Custom    includes the source actor's ID (or debug alias, if available) and a custom message you
 Trace VI    define.


SendSend BatchBatch VIVI

(Filename: Actor Framework.lvlib:Batch Msg.lvclass:Send Batch.vi)

Sends multiple messages in a batch to an actor. All messages in the batch are given the
same priority. No additional messages of the same priority will be processed by the
actor in between the messages in the batch. However, messages with a higher priority
than the batch will be processed before the batch itself.


Inputs/Outputs

   •      Message Enqueuer —

    Message Enqueuer specifies the reference needed to send messages to the actor.

   •      Messages Array —


                                                    © National Instruments 5501

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5501 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5502 ordinal=5502 -->
## Functions

Functions


           Messages Array specifies the messages to send.

               •      Message Priority (Normal) —

           Message Priority specifies the placement of the messages in the message queue, which
            determines when the actor will process the messages.

           0 Low—Specifies that the batch will be processed after messages of all other priorities.
           Normal (Default)—Specifies that the batch will be processed after critical- and high-priority
           1            messages but before low-priority ones.
             High—Specifies that the batch will be processed first. High-priority messages can be
           2 superseded only by an Emergency Stop or Last Ack message, both of which have critical
                 priority.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Time-DelayedTime-Delayed SendSend MessageMessage VIVI

       Waits for the specified amount of time and then sends a message to an actor a
       specified number of times.


      Inputs/Outputs

               •      # Copies (0 = infinite repeat) —

           # Copies specifies the number of times this VI sends the Message. The default is 0, which


5502   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5502 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5503 ordinal=5503 -->
## Functions

Functions


  specifies to send the message an infinite number of times. Use the Delivery Notifier to stop
  sending the message.

•      Message Enqueuer —

  Message Enqueuer specifies the reference needed to send messages to the actor.

•      Message —

  Message specifies the message to send.

•       Milliseconds To Wait —

  Milliseconds To Wait specifies the time, in milliseconds, this VI waits before sending the
  Message.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      Message Priority (Normal) —

  Message Priority specifies the placement of the Message in the message queue. This placement
  determines when the actor will process the message.

   Low—Specifies that the message will be processed after messages of all other priorities.
  0    Multiple low-priority messages are processed in the order they are sent.
   Normal (Default)—Specifies that the message will be processed after critical- and high-priority
  1 messages but before low-priority ones. Multiple normal-priority messages are processed in the
   order they are sent.
   High—Specifies that the message will be processed first. Multiple high-priority messages are
  2 processed in the order they are sent. High-priority messages can be superseded only by an
   Emergency Stop or Last Ack message, both of which have critical priority.

•      Delivery Notifier —

  Delivery Notifier returns a notifier refnum you can use to preempt or reschedule the message
  delivery. This output also contains an enum of a typedef with valid values to send to the notifier.

  Use the Send Notification function to send the following values to this notifier:

      • Send next copy now


                                                   © National Instruments 5503

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5503 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5504 ordinal=5504 -->
## Functions

Functions

                     • Skip next scheduled copy
                     • Send next copy now and stop all further copies
                     • Stop all further copies
               •       error out —

             error out contains error information. This output provides standard error out functionality.


      AddressAddress MessageMessage VIVI

       (Filename: Actor Framework.lvlib:Self-Addressed Msg.lvclass:Address Message.vi)

       Creates a self-addressed message by storing an enqueuer inside a message. Later,
     when you send the message with the Send Self-Addressed Message method, the
      message will be sent to the actor that uses this enqueuer.


      Inputs/Outputs

               •      Destination —

            Destination specifies the enqueuer of the actor that will receive the self-addressed message.

               •      Message —

           Message specifies the message to send.

               •      Message Priority (Normal) —

           Message Priority specifies the placement of the Message in the message queue. This placement
            determines when the actor will process the message.

             Low—Specifies that the message will be processed after messages of all other priorities.
           0
              Multiple low-priority messages are processed in the order they are sent.
           Normal (Default)—Specifies that the message will be processed after critical- and high-priority
           1 messages but before low-priority ones. Multiple normal-priority messages are processed in the
             order they are sent.


5504   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5504 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5505 ordinal=5505 -->
## Functions

Functions


     High—Specifies that the message will be processed first. Multiple high-priority messages are
    2 processed in the order they are sent. High-priority messages can be superseded only by an
     Emergency Stop or Last Ack message, both of which have critical priority.

   •      Self-Addressed Message —

    Self-Addressed Message returns a message that consists of the Message, Destination, and
    Message Priority.


SendSend Self-AddressedSelf-Addressed MessageMessage VIVI

(Filename: Actor Framework.lvlib:Self-Addressed Msg.lvclass:Send Self-Addressed
Message.vi)

Sends a self-addressed message. You can send multiple copies to the same address by
calling this VI multiple times with the same message.

Use the Address Message method to create a self-addressed message.


Inputs/Outputs

   •      Self-Addressed Message in —

    Self-Addressed Message in specifies a self-addressed message.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Self-Addressed Message out —

    Self-Addressed Message out returns a duplicate of Self-Addressed Message in.

   •       error out —


                                                    © National Instruments 5505

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5505 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5506 ordinal=5506 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


       This VI returns error code 1556 if you attempt to send a self-addressed message that
      does not have a destination.

     SendSend MessageMessage AndAnd WaitWait ForFor ResponseResponse VIVI

       (Filename: Actor Framework.lvlib:Reply Msg.lvclass:Send Message And Wait For
       Response.vi)

      Sends a message to an actor and synchronously waits for a response from the actor.


      Inputs/Outputs

               •      Message Priority (Normal) —

           Message Priority specifies the placement of the Message in the message queue. This placement
            determines when the actor will process the message.

             Low—Specifies that the message will be processed after messages of all other priorities.           0              Multiple low-priority messages are processed in the order they are sent.
           Normal (Default)—Specifies that the message will be processed after critical- and high-priority
           1 messages but before low-priority ones. Multiple normal-priority messages are processed in the
             order they are sent.
             High—Specifies that the message will be processed first. Multiple high-priority messages are
           2 processed in the order they are sent. High-priority messages can be superseded only by an
            Emergency Stop or Last Ack message, both of which have critical priority.

               •      Message Enqueuer in —

           Message Enqueuer in specifies the reference needed to send a message to an actor.

               •       Original Message —


5506   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5506 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5507 ordinal=5507 -->
## Functions

Functions


    Original Message specifies the message this VI sends.

   •      timeout in ms (-1) —

    timeout in ms specifies the time, in milliseconds, this VI spends waiting for a reply. The default is
     -1, which specifies this VI waits indefinitely.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Message Enqueuer out —

    Message Enqueuer out returns the reference needed to send messages to the actor.

   •      Reply —

    Reply returns the message that the receiver sent in reply to Original Message.

   •      timed out? —

    timed out? returns TRUE if the timeout in ms elapsed before a reply was received.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SendSend LaunchLaunch NestedNested ActorActor MsgMsg VIVI

(Filename: Actor Framework.lvlib:Actor.lvclass:Send Launch Nested Actor Msg.vi)

This VI sends a message containing an actor to another actor. The actor receiving the
message will launch the payload actor as a nested actor. Use this VI only to send a
message from an actor to itself.

Ideally, this VI should have a scope such that an actor can only send this message to
itself. However, LabVIEW cannot specify a run-time dependent scope, so you must use
this VI only as specified.


                                                    © National Instruments 5507

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5507 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5508 ordinal=5508 -->
## Functions

Functions


      Inputs/Outputs

               •      Message Priority (Normal) —

           Message Priority specifies the placement of the messages in the message queue, which
            determines when the actor will process the messages.

           0 Low—Specifies that the batch will be processed after messages of all other priorities.
           Normal (Default)—Specifies that the batch will be processed after critical- and high-priority
           1            messages but before low-priority ones.
             High—Specifies that the batch will be processed first. High-priority messages can be
           2 superseded only by an Emergency Stop or Last Ack message, both of which have critical
                 priority.

               •       Self Enqueuer in —

             Self Enqueuer in is the reference the actor uses to send messages to itself.

               •      Nested Actor —

           Nested Actor is the initial state of the actor you want to launch.

               •      Auto-stop? (T) —

            Auto-stop determines whether Nested Actor stops when the calling actor stops. The default
            value is TRUE. If you set the value of this input to FALSE, you must manually override the Stop
           Core VI on the caller actor to specify stop behavior for Nested Actor.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     Open Actor Core front panel? (F) —

          Open Actor Core front panel? specifies whether, on launching the actor, the front panel of the
            Actor Core method opens. The default is FALSE. The TRUE setting causes this VI to return an


5508   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5508 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5509 ordinal=5509 -->
## Functions

Functions


     error in the run-time engine.

    Set Open Actor Core front panel? to TRUE during code development so you can access the
    Abort button for the VI, which helps if you forget to stop an actor. To open the Actor Core front
    panel of an actor for purposes other than debugging, use the Front Panel:Open method. You can
    also enable Show front panel when called on the Customize Window Appearance dialog box to
    configure this VI to open the Actor Core front panel when you call the actor.

   •       Self Enqueuer out —

     Self Enqueuer out returns the reference the actor uses to send messages to itself.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


It is generally problematic for any actor A to send a message telling another actor B to
launch a new nested actor C. Any message from A to B should tell B what to do, but not
how to do it. By including actor C in the message, A not only tells B to do a task, but
that B do the task by managing a nested actor. B may have a better way to accomplish
the task, and deciding how to respond to the message from A should be a part of the
internal details of B. If you violate this general rule, you create coupling between A and
B that may cause problems if you need to refactor B. Because A depends on B working
in a particular way, you may have to rewrite A in addition to rewriting B.

If you want to use this VI to launch a nested actor from one actor to another, create a
public VI in the calling actor class that includes the Send Launch Nested Actor Msg VI.

Refer to the Actor Framework template for more information about the Actor
Framework. To use the Actor Framework template, click Create Project from the
LabVIEW start screen and select Actor Framework.

MessageMessage QueueQueue

Use the Message Queue VIs to launch and communicate with the top-level actor in
your application.


                                                    © National Instruments 5509

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5509 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5510 ordinal=5510 -->
## Functions

Functions


         Palette                   Description
        Object

                   (Filename: Actor Framework.lvlib:Message Queue.lvclass:Obtain Message Queue.vi)        Obtain
        Message                   Obtains the reference to the message queue that the caller uses to communicate with
       Queue VI                   the top-level actor.


                   (Filename: Actor Framework.lvlib:Message Queue.lvclass:Read Enqueuer.vi)
       Read
        Enqueuer  Extracts the reference needed to send messages to the top-level actor.
          VI
                 Use the Obtain Message Queue method to obtain the Message Queue input.


                   (Filename: Actor Framework.lvlib:Message Queue.lvclass:Read Dequeuer.vi)
       Read
        Dequeuer  Extracts the reference needed to read messages from the top-level actor.
          VI
                 Use the Obtain Message Queue method to obtain the Message Queue input.


                   (Filename: Actor Framework.lvlib:Message Queue.lvclass:Release Message Queue.vi)
         Release
        Message   Releases the reference to a message queue.
       Queue VI
                 Use the Obtain Message Queue method to obtain the Message Queue input.


                   (Filename: Actor Framework.lvlib:Message Enqueuer.lvclass:Enqueue.vi)       Enqueue
          VI                 Sends a message.


                   (Filename: Actor Framework.lvlib:Message Dequeuer.lvclass:Dequeue.vi)       Dequeue
          VI                 Reads a message that a top-level actor sent to its caller. Use this VI to interact with non-


5510   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5510 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5511 ordinal=5511 -->
## Functions

Functions


 Palette           Description
 Object

            actor code, not in a VI that belongs to an actor.


           (Filename: Actor Framework.lvlib:Message Enqueuer.lvclass:Equals Not A Refnum.vi) Equals
 Not A          Checks whether a message enqueuer reference is equal to Not a Refnum. Unlike the Not
 Refnum          a Number/Path/Refnum? function, this function does not check whether a non-zero
 VI            reference still is valid. Refer to the detailed help for more information.


           (Filename: Actor Framework.lvlib:Message Dequeuer.lvclass:Equals Not A Refnum.vi) Equals
 Not A          Checks whether a message dequeuer reference is equal to Not a Refnum. Unlike the Not
 Refnum          a Number/Path/Refnum? function, this function does not check whether a non-zero
 VI            reference still is valid. Refer to the detailed help for more information.

ObtainObtain MessageMessage QueueQueue VIVI

(Filename: Actor Framework.lvlib:Message Queue.lvclass:Obtain Message Queue.vi)

Obtains the reference to the message queue that the caller uses to communicate with
the top-level actor.


Inputs/Outputs

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Message Queue —


                                                    © National Instruments 5511

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5511 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5512 ordinal=5512 -->
## Functions

Functions


           Message Queue returns the reference to the message queue.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   ReadRead EnqueuerEnqueuer VIVI

       (Filename: Actor Framework.lvlib:Message Queue.lvclass:Read Enqueuer.vi)

       Extracts the reference needed to send messages to the top-level actor.

      Use the Obtain Message Queue method to obtain the Message Queue input.


      Inputs/Outputs

               •      Message Queue —

           Message Queue specifies the reference to the message queue.

               •      Message Enqueuer —

           Message Enqueuer returns the reference needed to send messages to the top-level actor.

   ReadRead DequeuerDequeuer VIVI

       (Filename: Actor Framework.lvlib:Message Queue.lvclass:Read Dequeuer.vi)

       Extracts the reference needed to read messages from the top-level actor.

      Use the Obtain Message Queue method to obtain the Message Queue input.


5512   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5512 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5513 ordinal=5513 -->
## Functions

Functions


Inputs/Outputs

   •      Message Queue —

    Message Queue specifies the reference to the message queue.

   •      Message Dequeuer —

    Message Dequeuer returns the reference needed to read messages from the message queue.

ReleaseRelease MessageMessage QueueQueue VIVI

(Filename: Actor Framework.lvlib:Message Queue.lvclass:Release Message Queue.vi)

Releases the reference to a message queue.

Use the Obtain Message Queue method to obtain the Message Queue input.


Inputs/Outputs

   •      Message Queue —

    Message Queue specifies the reference to the message queue.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •      remaining elements —


                                                    © National Instruments 5513

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5513 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5514 ordinal=5514 -->
## Functions

Functions


           remaining elements returns any unread messages in the message queue.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   EnqueueEnqueue VIVI

       (Filename: Actor Framework.lvlib:Message Enqueuer.lvclass:Enqueue.vi)

      Sends a message.


      Inputs/Outputs

               •      Message Enqueuer in —

           Message Enqueuer in specifies the reference needed to send a message to an actor.

               •      Message —

           Message specifies the message to send.

               •      Message Priority (Normal) —

           Message Priority specifies the placement of the Message in the message queue. This placement
            determines when the actor will process the message.

             Low—Specifies that the message will be processed after messages of all other priorities.
           0
              Multiple low-priority messages are processed in the order they are sent.
           Normal (Default)—Specifies that the message will be processed after critical- and high-priority
           1 messages but before low-priority ones. Multiple normal-priority messages are processed in the
             order they are sent.
           2 High—Specifies that the message will be processed first. Multiple high-priority messages are


5514   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5514 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5515 ordinal=5515 -->
## Functions

Functions


     processed in the order they are sent. High-priority messages can be superseded only by an
     Emergency Stop or Last Ack message, both of which have critical priority.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Message Enqueuer out —

    Message Enqueuer out returns a duplicate of Message Enqueuer in.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

DequeueDequeue VIVI

(Filename: Actor Framework.lvlib:Message Dequeuer.lvclass:Dequeue.vi)

Reads a message that a top-level actor sent to its caller. Use this VI to interact with
non-actor code, not in a VI that belongs to an actor.


Inputs/Outputs

   •      Message Dequeuer in —

    Message Dequeuer in specifies the reference needed to read messages from a top-level actor.

   •      timeout in ms (-1) —

    timeout in ms specifies the time, in milliseconds, this VI has to read the message. The default is
     -1, which specifies no timeout.


                                                    © National Instruments 5515

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5515 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5516 ordinal=5516 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Message Dequeuer out —

           Message Dequeuer out returns a duplicate of Message Dequeuer in.

               •      Message —

           Message returns the message that was read from the queue. If timed out? returned TRUE,
           Message returns the default Message class.

               •      timed out? —

           timed out? returns TRUE if this VI was unable to read the message within the specified timeout
             in ms period. In this situation, message returns the default Message class.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •       priority —

              priority returns the priority level at which LabVIEW sent the message.

             Low—Specifies that the message was processed after messages of all other priorities. Multiple
           0               low-priority messages are processed in the order they are sent.
             Normal—Specifies that the message was processed after critical- and high-priority messages
           1 but before low-priority ones. Multiple normal-priority messages are processed in the order
             they are sent.
             High—Specifies that the message was processed first. Multiple high-priority messages are
           2 processed in the order they are sent. High-priority messages can be superseded only by an
            Emergency Stop or Last Ack message, both of which have critical priority.

   EqualsEquals NotNot AA RefnumRefnum VIVI

       (Filename: Actor Framework.lvlib:Message Enqueuer.lvclass:Equals Not A Refnum.vi)

      Checks whether a message enqueuer reference is equal to Not a Refnum. Unlike the

5516   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5516 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5517 ordinal=5517 -->
## Functions

Functions

Not a Number/Path/Refnum? function, this function does not check whether a non-
zero reference still is valid. Refer to the detailed help for more information.


Inputs/Outputs

   •      Message Enqueuer —

    Message Enqueuer specifies a message enqueuer to check.

   •      Not a refnum? —

    Not a refnum? returns TRUE if Message Enqueuer is equal to Not a Refnum, in which case you
    should not attempt to use this reference to send a message.

    This output returns FALSE in all other situations, including when Message Enqueuer is a non-
    zero refnum that has been released already. In these situations, send the message and then
    check for an error on that operation.


This function only checks whether Message Enqueuer is equal to Not a Refnum. It
does not check whether Message Enqueuer still is valid because doing so can
introduce a race condition into the application. It is possible for a refnum to become
invalid afterbeing declared valid but beforea message is sent to it.
EqualsEquals NotNot AA RefnumRefnum VIVI

(Filename: Actor Framework.lvlib:Message Dequeuer.lvclass:Equals Not A Refnum.vi)

Checks whether a message dequeuer reference is equal to Not a Refnum. Unlike the
Not a Number/Path/Refnum? function, this function does not check whether a non-
zero reference still is valid. Refer to the detailed help for more information.


                                                    © National Instruments 5517

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5517 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5518 ordinal=5518 -->
## Functions

Functions

      Inputs/Outputs

               •      Message Dequeuer —

           Message Dequeuer specifies a message dequeuer to check.

               •      Not a refnum? —

           Not a refnum? returns TRUE if Message Dequeuer is equal to Not a Refnum, in which case you
            should not attempt to use this reference to read a message.

             This output returns FALSE in all other situations, including when Message Dequeuer is a non-
            zero refnum that has been released already. In these situations, send the message and then
           check for an error on that operation.


       This function only checks whether Message Dequeuer is equal to Not a Refnum. It
      does not check whether Message Dequeuer still is valid because doing so can
       introduce a race condition into the application. It is possible for a refnum to become
        invalid afterbeing declared valid but beforea message is read from it.

        InitInit ActorActor QueuesQueues FORFOR TESTINGTESTING ONLYONLY VIVI

       Provides access the To-Self and To-Caller message queues for an actor without
       launching the actor.

      Use this VI to test how an actor handles messages. Do not use this VI in code that you
       deploy.


      Inputs/Outputs

               •      Actor in —

            Actor in specifies the actor.

               •       Actor-To-Caller Enqueuer —


5518   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5518 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5519 ordinal=5519 -->
## Functions

Functions


    Actor-To-Caller Enqueuer specifies the queue the actor uses to send messages to its caller.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Actor out —

    Actor out returns a duplicate of Actor in.

   •       Actor-To-Self Enqueuer —

    Actor-To-Self Enqueuer returns the reference to the queue the actor needs to send messages to
      itself.

   •       Actor-To-Self Dequeuer —

    Actor-To-Self Dequeuer returns the reference to the queue the actor needs to read its messages.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


This VI allows the Do method of a message to set the queues of an actor without
launching it. This VI returns the message enqueuer and dequeuer of an actor to the
caller, breaking the encapsulation around an actor. This action is useful for writing test
harnesses that dequeue the message from an actor instead of the normal procedure in
which the Actor Core method of an actor processes the message. This kind of test
harness is useful if you want to verify that the messages the actor sends to itself are
being generated properly when other methods are called.

To prevent abuse, this VI returns an error if the actor already has a queue set into it, if
the queue has been released, or if the refnum is not Not A Refnum. This VI sets the
actor-to-caller enqueuer that is passed in and creates the internal actor-to-self queue.
You cannot release this actor-to-self queue except by halting the caller.

GenerateGenerate CustomCustom TraceTrace VIVI

Generates a DETT (Desktop Execution Trace Toolkit) User Generated Trace. The trace

                                                    © National Instruments 5519

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5519 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5520 ordinal=5520 -->
## Functions

Functions

       includes the source actor's ID (or debug alias, if available) and a custom message you
       define.


      Inputs/Outputs

               •     Custom Action —

          Custom Action specifies the custom message you want to add to the trace.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

    CommonlyCommonly OverriddenOverridden MethodsMethods (Actor(Actor Framework)Framework)

      The following are Actor Framework class methods that you commonly override in
      descendant classes.

       Actor:ActorActor:Actor CoreCore [Protected][Protected]

       (Filename: Actor Framework.lvlib:Actor.lvclass:Actor Core.vi)

       Receives messages to the actor, reacts to them, and initiates any error handling that
     may shut the actor down.

      Descendant classes may override this VI to append parallel tasks for the actor to
      complete while it handles messages. Overrides use the Call Parent Class Method node.


      Inputs/Outputs

               •      Actor in —

5520   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5520 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5521 ordinal=5521 -->
## Functions

Functions


    Actor in specifies the state of the actor after it has launched.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Actor out —

    Actor out returns the state of the actor after it has shut down.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Message:DoMessage:Do

(Filename: Actor Framework.lvlib:Message.lvclass:Do.vi)

Defines what a message does when it is received by an actor. Generally, a message
instructs an actor to invoke one of its methods. By default, this method does nothing. A
child class must override it to define behavior.


Inputs/Outputs

   •      Message —

    Message specifies the message the actor received.

   •      Actor in —

    Actor in specifies the actor.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 5521

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5521 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5522 ordinal=5522 -->
## Functions

Functions


            standard error in functionality.

               •      Actor out —

            Actor out returns the actor.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use error out to control the actor's behavior after processing the message:

            • To continue running the actor, return no error.
            • To shut the actor down normally, return error code 43. The actor will shut down
          but will not report an error to its caller. Descendants of the Actor class can override
          the Handle Error method to change this behavior.
            • To shut the actor down and report an error to its caller, return any error code other
          than 43.

      ReplyReply Msg:DoMsg:Do CoreCore [Protected][Protected]

       (Filename: Actor Framework.lvlib:Reply Msg.lvclass:Do Core.vi)

       Defines what an actor does when it receives Reply Message. This method also defines
       the Reply that is returned to the actor that sent Reply Message.

      By default, this method does nothing, and Reply is the ancestor Message class. A child
       class must override this method to define behavior and specify a child of the Message
       class to return in the Reply output.


      Inputs/Outputs

               •      Reply Message —


5522   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5522 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5523 ordinal=5523 -->
## Functions

Functions


    Reply Message specifies the message the actor received.

   •      Actor in —

    Actor in specifies the actor.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Reply —

    Reply is the message that will be returned to the sender of Reply Message.

   •      Actor out —

    Actor out returns the actor.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Message:DropMessage:Drop MessageMessage CoreCore [Protected][Protected]

(Filename: Actor Framework.lvlib:Message.lvclass:Drop Message Core.vi)

Defines what a message does if it is in the message queue when the queue is released.
At this point, the actor has shut down, so it will never process the message.

By default, this method does nothing. A child class may override it to define behavior.
National Instruments provides the Reply Msg class to override this method. This class
releases its internal queue, which causes any caller of the Send Message and Wait For
Response method to stop waiting and return an error.


                                                    © National Instruments 5523

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5523 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5524 ordinal=5524 -->
## Functions

Functions

      Inputs/Outputs

               •      Message in —

           Message in specifies the message.


      Actor:HandleActor:Handle ErrorError [Protected][Protected]

       (Filename: Actor Framework.lvlib:Actor.lvclass:Handle Error.vi)

       Defines how the actor handles an error that occurred while processing a message. By
        default, this method does nothing except stop the actor.


      Inputs/Outputs

               •      Actor in —

            Actor in specifies the actor.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Actor out —

            Actor out returns the actor.

               •      stop actor? —

            stop actor? returns TRUE if the actor should stop. By default, this method always returns TRUE
           because the Handle Error method executes only when the actor experiences an error as a result
             of processing a message. A descendant class may override this method to change this behavior.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5524   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5524 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5525 ordinal=5525 -->
## Functions

Functions

This method also treats error code 43 (coming from error in) as a sign that the actor
shut down normally. In this situation, the Handle Error method does not return the
error on error out, meaning the actor's caller will not receive it. All other error codes
will be returned on error out. A descendant class may override this method to change
this behavior.

Actor:HandleActor:Handle LastLast AckAck CoreCore [Protected][Protected]

(Filename: Actor Framework.lvlib:Actor.lvclass:Handle Last Ack Core.vi)

Defines how the caller actor responds to the Last Ack message from a nested actor. The
Last Ack message is the final message a nested actor sends to its caller before it shuts
down. The message contains information about the final state of the nested actor.

By default, this method does nothing except return any error the nested actor sent. A
descendant class may override this method to define behavior.


Inputs/Outputs

   •      Actor in —

    Actor in specifies the actor.

   •      Last Ack —

    Last Ack specifies the Last Ack message that a nested actor sent.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Actor out —

    Actor out returns the actor.

   •       error out —


                                                    © National Instruments 5525

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5525 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5526 ordinal=5526 -->
## Functions

Functions


             error out contains error information. This output provides standard error out functionality.


       Actor:PreActor:Pre LaunchLaunch InitInit [Protected][Protected]

       (Filename: Actor Framework.lvlib:Actor.lvclass:Pre Launch Init.vi)

       Defines behavior that occurs after the Launch Nested Actor method is invoked but
       before the actor's Actor Core method begins running.

      By default, this method does nothing. A descendant class may override it to define
       behavior.

           Caution Do not use the Pre Launch Init method to call the Launch Root
               Actor method or the Launch Nested Actor method. Doing so causes this
            method to hang. Only use the Launch Root Actor VI from outside all Actor
            Framework VIs, and use the Launch Nested Actor VI from the Actor Core
             method.


      Inputs/Outputs

               •      Actor in —

            Actor in specifies the actor.

               •      Actor out —

            Actor out returns the actor.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The Pre Launch Init method is guaranteed to finish before the Launch Nested Actor

5526   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5526 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5527 ordinal=5527 -->
## Functions

Functions

method returns to its caller and before the actor itself receives any messages. Any
references that the Pre Launch Init method obtains are guaranteed to have the same
lifetime as the actor itself. Any errors that the Pre Launch Init method returns will abort
the launch.

Overrides of the Pre Launch Init method can use the actor's to-caller and to-self
enqueuer.

Actor:StopActor:Stop CoreCore [Protected][Protected]

(Filename: Actor Framework.lvlib:Actor.lvclass:Stop Core.vi)

Defines what the actor does before it stops. Use the final error code input to
determine whether the actor shut down in response to an error.

By default, this method passes the Stop message along to all auto-stop nested actors.
A descendant class may override this method to define additional behavior, such as
shutting down any processes the actor initiated in its override of the Actor Core
method.


Inputs/Outputs

   •      Actor in —

    Actor in specifies the state of the actor after it has stopped handling messages.

   •       final error code —

     final error code specifies the error code, if any, that caused this actor to shut down.

   •      Actor out —

    Actor out returns the actor.


                                                    © National Instruments 5527

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5527 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5528 ordinal=5528 -->
## Functions

Functions

     ConnectivityConnectivity

      Use the Connectivity VIs and functions to work with .NET objects, ActiveX-enabled
       applications, input devices, register addresses, source control, Web services, Windows
        registry keys, and other software, including National Instruments products you
       purchase.


         Palette                     Description
        Object

                  Use the Libraries & Executables VIs and functions to call code from libraries, such as          Libraries &                   dynamic link libraries (DLLs); to manipulate LabVIEW data for use in other         Executables
                       applications; and to call code written in text-based programming languages.


                  Use the Source Control VIs to access common source control features within LabVIEW.        Source                   You must configure LabVIEW to work with a third-party source control provider before
         Control                   you can use the Source Control VIs.


         Port I/O     Use the Port I/O VIs to read from and write to a specific register address.


                  Use the Web Services VIs to build and configure top-level VIs in LabVIEW Web services.
      Web
                   You can accept and process HTTP requests from Web clients, create HTTP sessions,
         Services
                  and perform other tasks associated with Web services communication.


                  Use the .NET functions to create .NET objects, set properties or call methods on those
        .NET         objects, and handle events for those objects in the .NET environment. You also can
                      create a .NET control on the front panel.


         Input
                  Use the Input Device Control VIs to obtain information about the joystick, keyboard,
         Device
                      or mouse connected to a computer.
         Control


5528   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5528 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5529 ordinal=5529 -->
## Functions

Functions


 Palette             Description
 Object

            Use the ActiveX functions to pass properties and methods to and from other ActiveX-
            enabled applications, such as Microsoft Excel.
 ActiveX          Some applications provide ActiveX data in the form of a self-describing data type
              called a variant. To review or process the data in LabVIEW, you must convert it to a
             corresponding LabVIEW data type using the Variant To Data function.


 Windows    Use the Windows Registry Access VIs to create, open, query, enumerate, close, and
 Registry     delete Windows registry keys. You also can enumerate, read, write, and delete the
 Access VIs   value of Windows registry keys.


 Python     Use the Python functions to call Python code from LabVIEW.

 MATLAB(R)  Use the MATLAB® functions to call MATLAB code from LabVIEW.

LibrariesLibraries && ExecutablesExecutables

Use the Libraries & Executables VIs and functions to call code from libraries, such as
dynamic link libraries (DLLs); to manipulate LabVIEW data for use in other applications;
and to call code written in text-based programming languages.


 Palette
           Description
 Object

 Call
 Library
            Calls a DLL or shared library function directly.
 Function
 Node

 System
          Executes a system command. Use the System Exec VI to execute or launch other
 Exec


                                                    © National Instruments 5529

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5529 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5530 ordinal=5530 -->
## Functions

Functions


         Palette                  Description
        Object

                Windows–based applications, command-line applications, (Windows) batch files, or
               (macOS and Linux) script files from within VIs. With the System Exec VI, you can include
                any parameters within your command string that the executing command supports.


      CallCall LibraryLibrary FunctionFunction NodeNode

        Calls a DLL or shared library function directly.

      The Call Library Function Node is expandable and shows data types for the wired
       inputs and outputs, similar to the Bundle function. You can configure the Call Library
       Function Node to specify the library, function, parameters, return value for the node,
        calling conventions, and function callbacks.


      Inputs/Outputs

               •      path in —

           path in identifies the name or path of the shared library you want to call. You must place a
           checkmark in the Specify path on diagram checkbox in the Call Library Function dialog box for
              this input to appear on the connector pane.

           Although you can specify the shared library to call by name or by path, these techniques use
              different search algorithms for locating the shared library and have different ramifications on
              distributing the shared libraries with stand-alone applications. Ensure that you choose the
            proper technique for your use case. For example, always specify system shared libraries, such as
          kernel32.dll, by name.

               •       error in (no error) —


5530   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5530 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5531 ordinal=5531 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •    —

   param 1..n are example input parameters of the library function.

   •      path out —

    path out returns the path to the called DLL or shared library. You must place a checkmark in the
    Specify path on diagram checkbox in the Call Library Function dialog box for this output to
    appear on the connector pane.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •    —

    return value is an example return value of the library function.

   •    —

   param 1..n output are example output parameters of the library function.


Error I/O operates uniquely in this function, which will not execute if an error enters
the node. Error 7 occurs if you provide a path that does not exist for dynamic DLL
loading. Error 1097 occurs if the Call Library Function Node calls external code that
contains an exception.

The Call Library Function Node supports a large number of data types and calling
conventions. You can use this node to call functions in most standard and custom-
made DLLs and shared libraries. If you want to call a DLL that contains ActiveX objects,
use the Automation Open function with the Property Node and the Invoke Node.

The Call Library Function Node consists of pairs of input and output terminals. You can
use one or both terminals. If the node does not generate return value, the top terminal
is unused. Each additional pair of terminals corresponds to a parameter in the
parameter list of the function you call in top-to-bottom order. You pass a value to the
function by wiring to the left terminal of a terminal pair. You read the value of a

                                                    © National Instruments 5531

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5531 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5532 ordinal=5532 -->
## Functions

Functions

      parameter after the function call by wiring from the right terminal of a terminal pair.

        Right-click the node and select Configure from the shortcut menu to display the Call
       Library Function dialog box, which you can use to specify the library name or path,
       function name, calling conventions, parameters, and return value for the node. When
      you click the OK button, the node automatically resizes to have the correct number of
       terminals and sets the terminals to the correct data types.

           Note LabVIEW reserves Windows messages WM_USER through
           WM_USER+99 for internal use only.

      You can use the Call Library Function Node to call code written in text-based
      programming languages.

      Related Information

       Calling Shared Libraries in LabVIEW

       Configure the Call Library Function Node

      Debugging Shared Libraries and Calls to Shared Libraries

        Call Library Function Dialog Box

      LabVIEW Manager Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Connectivity\Libraries and Executables\
        External Code (DLL) Execution.vi

     SystemSystem ExecExec

       Executes a system command. Use the System Exec VI to execute or launch other
      Windows–based applications, command-line applications, (Windows) batch files, or

5532   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5532 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5533 ordinal=5533 -->
## Functions

Functions

(macOS and Linux) script files from within VIs. With the System Exec VI, you can include
any parameters within your command string that the executing command supports.


Inputs/Outputs

   •      expected output size (4096) —

    Use expected output size to improve memory efficiency. Use a number slightly larger than the
    output size you expect. The command runs if you exceed this size, but LabVIEW uses its memory
     less efficiently. The default is 4096.

   •      wait until completion? (T) —

       If wait until completion? is TRUE, standard input is available as input to the command and
    standard output and standard error are available when the command finishes running. If
    FALSE, the command runs in the background and its input and output are not available.

   •     command line —

   command line indicates the command LabVIEW calls to run a program.

       If the executable is not in a directory listed in the PATH environment variable, the command line
    must contain the full path to the executable. (Windows) To use a command that must be
    executed directly from a command prompt window, insert cmd /c before the command.

   •      standard input —

    standard input is the text to pass to the command line as standard input.

   •      working directory —

    working directory is the file system directory from which you want to execute the command.
    You do not have to set working directory.

          Note Do not use working directory to locate the executable you want to run.


                                                    © National Instruments 5533

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5533 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5534 ordinal=5534 -->
## Functions

Functions


                   working directory applies to the executable only after it launches.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      run minimized? (F) —

                    If run minimized? is TRUE, the VI minimizes the run of your executable program. The default is
            FALSE.

             (Linux) run minimized? is unused.

               •      standard output —

           standard output returns information from the program you called if wait until completion is
           TRUE. If wait until completion is FALSE, System Exec returns an empty string.

               •      standard error —

           standard error returns errors from the program you called if wait until completion is TRUE. If
            wait until completion is FALSE, System Exec returns an empty string.

               •      return code —

            return code indicates the system-dependent exit code that the command returns.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      (macOS and Linux) You can use wildcards and shell meta-characters. (Linux) You can
      use pipes.

      To launch an executable with options using the syntax filename.exe -option1
     -option2, create a filename.bat file that calls the executable with the options
       syntax and use this VI to call the filename.bat file.


5534   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5534 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5535 ordinal=5535 -->
## Functions

Functions

System Exec Error Codes

The System Exec VI can return either Windows or LabVIEW error codes. Windows and
LabVIEW error codes also can use the same identifying numbers. For example, the
System Exec VI can return Windows system error code 2, File_not_Found, in addition to
LabVIEW error code 2.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Libraries and Executables\
   Command Line Execution.vi

RunRun AppleScriptAppleScript CodeCode

Executes AppleScript code to communicate with external macOS applications from
LabVIEW.

AppleScript is a scripting language that enables you to control macOS applications as
well as different parts of the OS. Use the Run AppleScript Code VI to request actions or
return information from macOS applications external to LabVIEW using AppleScript
code. For example, you can use this VI to communicate with Finder to set window
settings or export data to a Microsoft Excel file.


Inputs/Outputs

   •      input string —

    input string specifies the AppleScript code you want to use to communicate with external
   macOS applications. Refer to the AppleScript website for more information about the
    AppleScript language. If you input an invalid code string, LabVIEW returns an error.

   •      wait until completion? (T) —


                                                    © National Instruments 5535

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5535 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5536 ordinal=5536 -->
## Functions

Functions


            wait until completion? specifies whether you want to wait until the AppleScript code finishes
            executing before the VI finishes executing. If you specify TRUE, Results and Compile & Runtime
             Errors are available when the command finishes running. If you specify FALSE, the command
            runs in the background and the input and output of the command line are not available. The
             default is TRUE.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      Results —

            Results returns the results from running the AppleScript if wait until completion? is TRUE. If you
           choose to run the AppleScript code in the background by specifying FALSE in wait until
            completion?, Results returns an empty string.

               •      Compile & Runtime Errors —

           Compile & Runtime Errors returns errors that occurred while compiling and running the
            AppleScript code if wait until completion? is TRUE. If you choose to run the AppleScript code in
            the background by specifying FALSE in wait until completion?, Compile & Runtime Errors
             returns an empty string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     PipesPipes

      Use the Pipes VIs to pass data between applications on Linux. Pipes VIs simplify
       process synchronization by allowing separate processes to communicate with each
        other.


5536   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5536 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5537 ordinal=5537 -->
## Functions

Functions


 Palette            Description
 Object

          Opens a named pipe and returns file descriptor, which you pass to subsequent Pipes Open Pipe               VIs.

 Open
 System    Opens a pipe to a system shell command and returns file descriptors that you can pass
 Command  to subsequent Pipes VIs.
 Pipe

 Close Pipe  Closes a pipe. Other processes reading the pipe will receive EOF (end-of-file).


           Reads a number of bytes from a pipe, returning the results in the data string output. Read            For this VI, you must have opened the pipe as a read pipe. The VI does not wait for data,
 From Pipe           so if the amount of data is not available, the VI returns any available data.


 Write To    Writes a data string to a pipe. For this VI, you must have opened the pipe as a write
 Pipe        pipe.


OpenOpen PipePipe

Opens a named pipe and returns file descriptor, which you pass to subsequent Pipes
VIs.

A named pipe is a special file that can be used to communicate between separate
Linux processes. Unlike a normal file, you must open a pipe in read mode, usually from
another process or application, before you open the pipe in write mode so data written
to the pipe can be passed to the reading process. Otherwise, an I/O error occurs and
the open process fails.


                                                    © National Instruments 5537

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5537 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5538 ordinal=5538 -->
## Functions

Functions

      Inputs/Outputs

               •      path to named pipe —

           path to named pipe is the path to the named pipe.

               •     mode —

         mode indicates whether you want to read or write data.

           0              Read
           1                 Write

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        file descriptor —

                file descriptor is the file descriptor to use when reading from and writing to the opened pipe.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     OpenOpen SystemSystem CommandCommand PipePipe

      Opens a pipe to a system shell command and returns file descriptors that you can pass
       to subsequent Pipes VIs.

      You must use the Close Pipe VI to close all returned file descriptors.


5538   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5538 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5539 ordinal=5539 -->
## Functions

Functions

Inputs/Outputs

   •     command line —

   command line indicates which command for LabVIEW to call to run your program.

   •     mode —

   mode determines whether you want to read and/or write data.

    0      Read
    1       Write
    2      Read & Write

   •      return standard error fd? —

    return standard error fd? sets the VI to return error file descriptor when set to TRUE. The
     default is FALSE.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      process ID —

    process ID returns the process ID.

   •      read file descriptor —

    read file descriptor returns a file descriptor if you set mode to Read or Read + Write.

   •      write file descriptor —

    write file descriptor returns a file descriptor if you set mode to Write or Read + Write.

   •       error file descriptor —

    error file descriptor returns a file descriptor you can pass to the Read From Pipe and Close Pipe
     VIs if you set return standard error fd? to TRUE.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5539

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5539 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5540 ordinal=5540 -->
## Functions

Functions

      CloseClose PipePipe

       Closes a pipe. Other processes reading the pipe will receive EOF (end-of-file).


      Inputs/Outputs

               •        file descriptor —

                file descriptor is the file descriptor to use when closing the pipe.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •        file descriptor —

                file descriptor is the file descriptor to use when closing the pipe.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     ReadRead FromFrom PipePipe

      Reads a number of bytes from a pipe, returning the results in the data string output.
       For this VI, you must have opened the pipe as a read pipe. The VI does not wait for
       data, so if the amount of data is not available, the VI returns any available data.


5540   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5540 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5541 ordinal=5541 -->
## Functions

Functions

Inputs/Outputs

   •        file descriptor —

      file descriptor is the file descriptor to use when reading from and writing to the opened pipe.

   •      bytes to read —

    bytes to read is the maximum number of bytes you want the VI to read. This VI might read fewer
    bytes than bytes to read.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      eof? —

       If eof? is TRUE, the other end of the pipe is closed.

   •        file descriptor —

      file descriptor is the file descriptor to use when closing the pipe.

   •      bytes read —

    bytes read is the number of bytes read, which can be less than bytes to read.

   •      data —

    data is the data read from the pipe.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


WriteWrite ToTo PipePipe

Writes a data string to a pipe. For this VI, you must have opened the pipe as a write
pipe.


                                                    © National Instruments 5541

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5541 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5542 ordinal=5542 -->
## Functions

Functions


      Inputs/Outputs

               •        file descriptor —

                file descriptor is the file descriptor to use when reading from and writing to the opened pipe.

               •      data —

           data is the data to write to the pipe.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        file descriptor —

                file descriptor is the file descriptor to use when writing to the opened pipe.

               •      bytes written —

            bytes written is the number of bytes written, which can be less than the number of bytes in
             data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     SourceSource ControlControl

      Use the Source Control VIs to access common source control features within LabVIEW.
      You must configure LabVIEW to work with a third-party source control provider before
      you can use the Source Control VIs.

      The VIs on this palette can return source control error codes.


5542   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5542 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5543 ordinal=5543 -->
## Functions

Functions


Palette              Description
Object

SCC Open    Opens a new and unique reference to a source control project that you can use with
SCC Project   the Source Control VIs.


SCC Get              Copies the latest version of the specified files from source control to the directoryLatest            you specified during source control configuration.
Version


SCC Check In  Checks in the specified files to source control.


SCC Check
             Checks out the specified files from source control.Out

SCC Close              Closes an existing source control reference.SCC Project


SCC Add      Adds the specified files to source control.


SCC Remove  Removes the specified files from source control.


              Returns the current source control status of specified files, including whether a file
SCC File                   is in source control, whether it is checked out, and whether it is the latest version
Status
               available in source control.


SCC Undo     Cancels a previous source control check-out operation and restores the contents of
Check Out     the selected file to the previous version. Any changes you made to the file are lost.


               Displays a dialog box that contains the source control properties of a specified file,
SCC File
             such as the file type and revision number. Some source control providers also return
Properties
               properties in the status message output.


                                                    © National Instruments 5543

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5543 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5544 ordinal=5544 -->
## Functions

Functions


         Palette                       Description
        Object

       SCC File       Returns the source control history for specified files. The source control history
         History       provides information about previous versions of the files.


       SCC Compare  Returns the difference between the specified file and, by default, the latest version
          Files           of the file in source control.


       SCC Compare  Returns the difference between the specified VI and by default, the latest version of
          VIs           the VI in source control.

       SCC Not A
        Source                         Specifies whether a source control reference is a valid refnum.         Control
         Reference

    SCCSCC OpenOpen SCCSCC ProjectProject

      Opens a new and unique reference to a source control project that you can use with
       the Source Control VIs.

      The VI uses the configuration settings from the current source control provider to
       generate the reference. If you wire a LabVIEW project reference to Project Refnum, this
        VI generates a reference to the source control project you specify for the LabVIEW
        project.


      Inputs/Outputs

               •       project refnum —

             project refnum is a reference to a LabVIEW project. If you wire this input, this VI uses the source


5544   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5544 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5545 ordinal=5545 -->
## Functions

Functions


    control configuration settings from the LabVIEW project instead of the settings you configured
     for the LabVIEW environment on the Source Control page of the Options dialog box.

       If the LabVIEW project is configured not to use source control, has a conflict with the current SCC
     provider, or is configured incorrectly, this VI returns an error and does not create a source control
     reference.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      source control reference out —

    source control reference out contains a new and unique reference to the source control project
    configured in LabVIEW.

    Wire this output to the source control reference in input of the Source Control VIs.

   •       status message —

    status message returns provider-specific information about the source control operation.

    Depending on the source control provider, the output might include status information or non-
     critical error messages.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SCCSCC GetGet LatestLatest VersionVersion

Copies the latest version of the specified files from source control to the directory you
specified during source control configuration.


                                                    © National Instruments 5545

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5545 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5546 ordinal=5546 -->
## Functions

Functions

      Inputs/Outputs

               •      advanced options —

           advanced options is reserved for internal use.

               •      source control reference in —

            source control reference in contains a reference to the source control project configured in
           LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
             Project VI.

               •        files —

               files specifies the paths to the files for which the VI gets the latest version. The paths can be
              directories if you specify the retrieval method as directory or directory (recursive).

               •       retrieval method (file) —

              retrieval method specifies the way the VI retrieves files from source control.

           Not all source control providers support retrieval by directory.

           0 file (default)—The VI interprets paths in files as files.
           1 directory—The VI interprets paths in files as directories.
              directory (recursive)—The VI interprets paths in files as directories. If you duplicate directory           2
              paths, the VI retrieves those directories multiple times.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      versions —

            versions specifies the version of the file or files to retrieve. The default is an empty string.

                    If the string is empty, the VI returns the most recent version. Not all source control providers
            support this parameter. The syntax for this parameter varies for each provider. Refer to the
            source control provider documentation for more information about version syntax.

               •      source control reference out —


5546   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5546 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5547 ordinal=5547 -->
## Functions

Functions


    source control reference out returns source control reference in unchanged.

   •       status message —

    status message returns provider-specific information about the source control operation.

    Depending on the source control provider, the output might include status information or non-
     critical error messages.

   •      dialog box cancelled? —

    dialog box cancelled? returns TRUE if you cancelled any source control provider dialog boxes
    that appeared during the source control operation.

    The provider controls the dialog box display. The indicator returns FALSE if no dialog boxes
    displayed.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SCCSCC CheckCheck InIn

Checks in the specified files to source control.


Inputs/Outputs

   •      advanced options —

    advanced options is reserved for internal use.

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in


                                                    © National Instruments 5547

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5547 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5548 ordinal=5548 -->
## Functions

Functions


           LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
             Project VI.

               •        files —

               files specifies the paths to the files to check into source control.

               •     comment —

         comment contains text that describes the reason for the source control operation.

          The source control provider stores this information and adds it to the source control history of
            the files specified in the files control. Depending on the source control provider, if the
         Comments input is empty, a provider-specific dialog box might display so you can enter the
             information.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      keep checked out? (F) —

           keep checked out? specifies whether the VI checks out the files immediately after the source
             control operation completes. The default is FALSE, in which the files are not checked out.

           Not all source control providers support this parameter.

               •      source control reference out —

            source control reference out returns source control reference in unchanged.

               •       status message —

             status message returns provider-specific information about the source control operation.

           Depending on the source control provider, the output might include status information or non-
               critical error messages.

               •      dialog box cancelled? —

            dialog box cancelled? returns TRUE if you cancelled any source control provider dialog boxes
             that appeared during the source control operation.


5548   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5548 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5549 ordinal=5549 -->
## Functions

Functions


    The provider controls the dialog box display. The indicator returns FALSE if no dialog boxes
    displayed.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SCCSCC CheckCheck OutOut

Checks out the specified files from source control.

If you try to check out a file that someone else has checked out, or if you check out a
file without getting the latest version, a provider-specific dialog box might appear
when you run the VI.


Inputs/Outputs

   •      advanced options —

    advanced options is reserved for internal use.

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •        files —

     files specifies the paths to the files to check out of source control.

   •     comment —

   comment contains text that describes the reason for the source control operation.


                                                    © National Instruments 5549

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5549 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5550 ordinal=5550 -->
## Functions

Functions


          The source control provider stores this information and adds it to the source control history of
            the files specified in the files control. Depending on the source control provider, if the
         Comments input is empty, a provider-specific dialog box might display so you can enter the
             information.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      source control reference out —

            source control reference out returns source control reference in unchanged.

               •       status message —

             status message returns provider-specific information about the source control operation.

           Depending on the source control provider, the output might include status information or non-
               critical error messages.

               •      dialog box cancelled? —

            dialog box cancelled? returns TRUE if you cancelled any source control provider dialog boxes
             that appeared during the source control operation.

          The provider controls the dialog box display. The indicator returns FALSE if no dialog boxes
             displayed.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SCCSCC CloseClose SCCSCC ProjectProject

       Closes an existing source control reference.


5550   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5550 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5551 ordinal=5551 -->
## Functions

Functions

Inputs/Outputs

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       status message —

    status message returns provider-specific information about the source control operation.

    Depending on the source control provider, the output might include status information or non-
     critical error messages.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SCCSCC AddAdd

Adds the specified files to source control.


Inputs/Outputs

   •      advanced options —


                                                    © National Instruments 5551

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5551 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5552 ordinal=5552 -->
## Functions

Functions


           advanced options is reserved for internal use.

               •      source control reference in —

            source control reference in contains a reference to the source control project configured in
           LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
             Project VI.

               •        files —

               files specifies the paths to the files to add to source control.

               •     comment —

         comment contains text that describes the reason for the source control operation.

          The source control provider stores this information and adds it to the source control history of
            the files specified in the files control. Depending on the source control provider, if the
         Comments input is empty, a provider-specific dialog box might display so you can enter the
             information.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      keep checked out? (F) —

           keep checked out? specifies whether the VI checks out the files immediately after the source
             control operation completes. The default is FALSE, in which the files are not checked out.

           Not all source control providers support this parameter.

               •      source control reference out —

            source control reference out returns source control reference in unchanged.

               •       status message —

             status message returns provider-specific information about the source control operation.

           Depending on the source control provider, the output might include status information or non-
               critical error messages.

               •      dialog box cancelled? —

5552   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5552 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5553 ordinal=5553 -->
## Functions

Functions


    dialog box cancelled? returns TRUE if you cancelled any source control provider dialog boxes
    that appeared during the source control operation.

    The provider controls the dialog box display. The indicator returns FALSE if no dialog boxes
    displayed.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SCCSCC RemoveRemove

Removes the specified files from source control.

      Caution Be careful when you remove files from source control. Some
       source control providers delete the local directory copy of the file, all
       previous versions of the file that the provider maintains, and the history log
         for the file. Refer to the source control provider documentation for more
       information about the effects of removing files from source control.


Inputs/Outputs

   •      advanced options —

    advanced options is reserved for internal use.

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •        files —

                                                    © National Instruments 5553

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5553 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5554 ordinal=5554 -->
## Functions

Functions


               files specifies the paths to the files to remove from source control.

               •     comment —

         comment contains text that describes the reason for the source control operation.

          The source control provider stores this information and adds it to the source control history of
            the files specified in the files control. Depending on the source control provider, if the
         Comments input is empty, a provider-specific dialog box might display so you can enter the
             information.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      source control reference out —

            source control reference out returns source control reference in unchanged.

               •       status message —

             status message returns provider-specific information about the source control operation.

           Depending on the source control provider, the output might include status information or non-
               critical error messages.

               •      dialog box cancelled? —

            dialog box cancelled? returns TRUE if you cancelled any source control provider dialog boxes
             that appeared during the source control operation.

          The provider controls the dialog box display. The indicator returns FALSE if no dialog boxes
             displayed.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SCCSCC FileFile StatusStatus

       Returns the current source control status of specified files, including whether a file is in


5554   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5554 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5555 ordinal=5555 -->
## Functions

Functions

source control, whether it is checked out, and whether it is the latest version available
in source control.


Inputs/Outputs

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •        files —

     files specifies the paths to the files for which the VI obtains the source control status.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      source control reference out —

    source control reference out returns source control reference in unchanged.

   •       status message —

    status message returns provider-specific information about the source control operation.

    Depending on the source control provider, the output might include status information or non-
     critical error messages.

   •        file status —

      file status returns details of the source control status for each specified file.

         •       in source control? —


                                                    © National Instruments 5555

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5555 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5556 ordinal=5556 -->
## Functions

Functions


                  in source control? indicates whether the file is in source control.

                     •      checked out by user? —

               checked out by user? indicates whether the current user has checked out the file.

              The output does not depend on the location of the checked out file or the checked out by
                other? output.

                     •      checked out by other? —

               checked out by other? indicates whether other users have checked out the file.

                     •      out of date? —

               out of date? indicates whether the file is the latest version available from the source control
                  provider.

                           If the VI returns FALSE, the file is the latest version.

                     •      deleted? —

                deleted? indicates whether the file is deleted from source control.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •        files status flags —

               files status flags returns a bit array that represents the status information. Not all source control
            providers support this parameter.

    SCCSCC UndoUndo CheckCheck OutOut

       Cancels a previous source control check-out operation and restores the contents of the
       selected file to the previous version. Any changes you made to the file are lost.


5556   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5556 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5557 ordinal=5557 -->
## Functions

Functions


Inputs/Outputs

   •      advanced options —

    advanced options is reserved for internal use.

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •        files —

     files specifies the paths to the files to undo the check out.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      source control reference out —

    source control reference out returns source control reference in unchanged.

   •       status message —

    status message returns provider-specific information about the source control operation.

    Depending on the source control provider, the output might include status information or non-
     critical error messages.

   •      dialog box cancelled? —

    dialog box cancelled? returns TRUE if you cancelled any source control provider dialog boxes
    that appeared during the source control operation.

    The provider controls the dialog box display. The indicator returns FALSE if no dialog boxes
    displayed.


                                                    © National Instruments 5557

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5557 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5558 ordinal=5558 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SCCSCC FileFile PropertiesProperties

       Displays a dialog box that contains the source control properties of a specified file,
      such as the file type and revision number. Some source control providers also return
       properties in the status message output.


      Inputs/Outputs

               •      source control reference in —

            source control reference in contains a reference to the source control project configured in
           LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
             Project VI.

               •        file path —

                file path specifies the path to the file for which the VI returns source control properties.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •        file changed? —

                file changed? returns TRUE if a change to the specified file occurred during the source control
             operation.

               •      source control reference out —

            source control reference out returns source control reference in unchanged.

               •       status message —

5558   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5558 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5559 ordinal=5559 -->
## Functions

Functions


    status message returns the source control properties for the specified file or files. Not all source
    control providers return properties in this output.

    By default, all providers return the properties in a provider-specific dialog box.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SCCSCC FileFile HistoryHistory

Returns the source control history for specified files. The source control history
provides information about previous versions of the files.

Depending on the source control provider you use, the history information can appear
in a dialog box or in the status message output.


Inputs/Outputs

   •      advanced options —

    advanced options is reserved for internal use.

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •        files —

     files specifies the paths to the files for which you want to obtain the source control history.

    Depending on the source control provider, you might be able to obtain the source control history


                                                    © National Instruments 5559

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5559 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5560 ordinal=5560 -->
## Functions

Functions


              for only the first file you specify.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      versions —

            versions specifies the version of the file or files to retrieve. The default is an empty string.

                    If the string is empty, the VI returns the most recent version. Not all source control providers
            support this parameter. The syntax for this parameter varies for each provider. Refer to the
            source control provider documentation for more information about version syntax.

               •        file changed? —

                file changed? returns TRUE if a change to the specified file occurred during the source control
             operation.

               •      source control reference out —

            source control reference out returns source control reference in unchanged.

               •       status message —

             status message returns the source control history for the specified file or files.

           Depending on the source control provider, the source control history might also appear in a
             provider-specific dialog box.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SCCSCC CompareCompare FilesFiles

       Returns the difference between the specified file and, by default, the latest version of
       the file in source control.


5560   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5560 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5561 ordinal=5561 -->
## Functions

Functions


Inputs/Outputs

   •      advanced options —

    advanced options is reserved for internal use.

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •        file path —

      file path specifies the path to the file the VI uses for comparison.

   •     compare method —

    compare method specifies the way in which the VI performs a comparison on the files.

       If you select contents, checksum, or time, the comparison is silent, which means the VI does not
    return data in a dialog box. Checksum and time comparisons are faster but less detailed
    comparison methods than contents comparison.

     source control provider default (default)—The VI uses the default comparison method from
    0
     the source control provider. The VI returns data in a dialog box or a status message.
    1 contents—The VI performs a byte-by-byte comparison.
    checksum—The VI uses the checksums of the files to perform a comparison. Not all source
    2
      control providers support checksum comparisons.
     time—The VI uses the timestamps in the files to perform a comparison. Not all source control
    3
      providers support time comparisons.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 5561

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5561 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5562 ordinal=5562 -->
## Functions

Functions

               •     compare options —

          compare options specifies whether to modify the comparison to include case sensitivity and
            white space.

           Not all source control providers support this parameter.

                     •      ignore case? (F) —

                ignore case? specifies whether the comparison is case sensitive. The default is FALSE, in
               which the comparison is case sensitive.

                     •      ignore space? (F) —

                ignore space? specifies whether the comparison includes white spaces. The default is
                FALSE, in which the comparison includes white spaces.


               •      version —

            version specifies the version of the file you want to compare. The default is an empty string.

                    If the string is empty, the VI compares the latest version of the file. Not all source control
            providers support this parameter. The syntax for this parameter varies for each provider. Refer to
            the source control provider documentation for more information about version syntax.

               •        file differs? —

                file differs? returns TRUE if the specified file differs from the version in source control, based on
            the compare method you select.

               •      source control reference out —

            source control reference out returns source control reference in unchanged.

               •       status message —

             status message returns the results of the comparison if the VI performed a silent comparison
           method.

           Depending on the source control provider, the output might include status information or non-
               critical error messages.

               •       error out —


5562   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5562 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5563 ordinal=5563 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


This VI treats files either as text or binary. Depending on the source control provider
you use, the VI displays the differences in a dialog box or returns them in the status
message output. Use the SCC Compare VIs VI to compare LabVIEW file types, such as
VIs, controls, or global variables.

SCCSCC CompareCompare VIsVIs

Returns the difference between the specified VI and by default, the latest version of the
VI in source control.

Use this VI with LabVIEW file types, such as VIs, control, and global variables. The VI
returns an error if you specify file types not specific to LabVIEW, such as text files or
HTML files. Use the SCC Compare Files VI to compare text or binary files.


Inputs/Outputs

   •      application reference —

    application reference is reserved for internal use.

   •      source control reference in —

    source control reference in contains a reference to the source control project configured in
    LabVIEW. The source control reference must be a valid reference created with the SCC Open SCC
    Project VI.

   •       VI path —

     VI path specifies the path to the VI you want to compare.


                                                    © National Instruments 5563

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5563 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5564 ordinal=5564 -->
## Functions

Functions

               •     compare options —

          compare options specifies the methods the VI uses for comparison.

                     •       VI Attributes —

                  VI Attributes specifies whether the comparison includes the VI attributes set in the VI
                 Properties dialog box. The default is FALSE, in which VI attributes are excluded from the
                comparison.

                     •      Front Panel —

                Front Panel specifies whether the comparison includes front panel items. The default is
               TRUE.

                     •     FP position/size —

              FP position/size specifies whether the comparison includes the position and size of the
                  front panel window. The default is FALSE, in which the front panel position and size are
                excluded from the comparison.

                     •      Block Diagram —

               Block Diagram specifies whether the comparison includes block diagram items. The default
                      is TRUE.

                     •     BD cosmetic —

            BD cosmetic specifies whether the comparison includes cosmetic aspects of the block
                diagram. The default is FALSE, in which the cosmetic aspects are excluded from the
                comparison.

                     •     BD position/size —

            BD position/size specifies whether the comparison includes the position and size of the
                block diagram window. The default is FALSE, in which the block diagram position and size
                 are excluded from the comparison.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       interactive? (F) —

5564   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5564 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5565 ordinal=5565 -->
## Functions

Functions


     interactive? specifies whether the VI performs a silent or a visual comparison.

    The default is FALSE, which specifies a silent comparison, in which the VI returns results in the
    status message output. If you select TRUE, the VI performs an interactive visual comparison, in
    which the front panels and block diagrams of the two VI versions display and a dialog box lists
    the differences.

   •      version —

    version specifies the version of the file you want to compare. The default is an empty string.

       If the string is empty, the VI compares the latest version of the file. Not all source control
    providers support this parameter. The syntax for this parameter varies for each provider. Refer to
    the source control provider documentation for more information about version syntax.

   •        file differs? —

      file differs? returns TRUE if the specified VI differs from the version in source control.

   •      source control reference out —

    source control reference out returns source control reference in unchanged.

   •       status message —

    status message returns the results of the comparison if the VI performed a silent comparison
    method.

    Depending on the source control provider, the output might include status information or non-
     critical error messages.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SCCSCC NotNot AA SourceSource ControlControl ReferenceReference

Specifies whether a source control reference is a valid refnum.


                                                    © National Instruments 5565

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5565 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5566 ordinal=5566 -->
## Functions

Functions

      Inputs/Outputs

               •      source control reference in —

            source control reference in contains a reference to the source control project configured in
           LabVIEW.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      not a source control reference? —

           not a source control reference? returns TRUE if source control reference in is not a valid source
             control refnum.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     PortPort I/OI/O

      Use the Port I/O VIs to read from and write to a specific register address.


    WebWeb ServicesServices

      Use the Web Services VIs to build and configure top-level VIs in LabVIEW Web services.
      You can accept and process HTTP requests from Web clients, create HTTP sessions,
      and perform other tasks associated with Web services communication.

           Note This topic assumes familiarity with the Web services introduction and
                 tutorial.


5566   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5566 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5567 ordinal=5567 -->
## Functions

Functions


Palette            Description
Object

Read Form  Reads a single form data value associated with the current HTTP request. Use this VI
Data         for requests that use the multipart/form-data encoding type.


           Reads the form data values received from the specified HTTP request. This VIRead All            processes that form data and assigns those values to elements in 1D arrays. Use this VI
Form Data              for requests that use the multipart/form-data encoding type.


            Returns an array of clusters that contains information about all uploaded filesRead            associated with the specified HTTP request. This information includes the clientUploaded
             filename, the path to the temporary storage location, the content type, and the size inFiles Info             bytes.


           Reads any POST data associated with the current HTTP request. This VI does notRead           handle POST data with the multipart/form-data encoding type. Use the Read FormPostdata
           Data VI to handle this encoding type.


Read       Returns the value for a single request variable associated with the current HTTP
Request     request. Web services include over 30 request variables that provide information such
Variable    as server label, remote address, and cache control related to an HTTP request.


Read All    Reads all request variables associated with the current HTTP request. Web services
Request     include over 30 request variables that provide information such as server label,
Variables   remote address, and cache control related to an HTTP request.


NI Web
           Use the NI Web Server VIs to support Web services deployed to the NI Web Server.
Server


Service     Use the Web Services VIs in startup VIs to access information about a LabVIEW Web


                                                    © National Instruments 5567

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5567 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5568 ordinal=5568 -->
## Functions

Functions


         Palette                     Description
        Object

                        service.


        Output     Use the Output VIs to set HTTP settings and write streaming responses.


                  Use the Conversion VIs to escape or unescape characters in a URL or convert images        Conversion                        for LabVIEW Web services.


         Application Use the Application Web Server VIs to support Web services deployed to the
      Web Server  Application Web Server.


       Related Information

       Overview: Web-based Communication with a LabVIEW Application

       Using the VIs on the Web Services Palette

     ReadRead FormForm DataData

      Reads a single form data value associated with the current HTTP request. Use this VI
        for requests that use the multipart/form-data encoding type.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


5568   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5568 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5569 ordinal=5569 -->
## Functions

Functions

Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      key —

    key specifies the name of the form data element for which to return a value. For example, if an
   HTML form submits the post data, x=2&y=3, you can enter either x or y as the key to retrieve
    the respective value.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      value —

    value returns the value of the specified form data element.

   •     mime type —

   mime type returns the MIME type of the form data associated with the HTTP request. Web
     clients can use HTML forms with the POST HTTP method or clients can use the POST VI to submit
    form data values to a Web service.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5569

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5569 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5570 ordinal=5570 -->
## Functions

Functions

     ReadRead AllAll FormForm DataData

      Reads the form data values received from the specified HTTP request. This VI
       processes that form data and assigns those values to elements in 1D arrays. Use this VI
        for requests that use the multipart/form-data encoding type.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •     Key —


5570   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5570 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5571 ordinal=5571 -->
## Functions

Functions


    Key returns the key of the form data associated with the HTTP request. Web clients can use
   HTML forms with the POST HTTP method or clients can use the POST VI to submit form data
    values to a Web service.

   •      Value —

    Value returns the value of the form data associated with the HTTP request. Web clients can use
   HTML forms with the POST HTTP method or clients can use the POST VI to submit form data
    values to a Web service.

   •     Mime Type —

   Mime Type returns the MIME type of the form data associated with the HTTP request. Web
     clients can use HTML forms with the POST HTTP method or clients can use the POST VI to submit
    form data values to a Web service.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReadRead UploadedUploaded FilesFiles InfoInfo

Returns an array of clusters that contains information about all uploaded files
associated with the specified HTTP request. This information includes the client
filename, the path to the temporary storage location, the content type, and the size in
bytes.

      Note This topic assumes familiarity with the Web services introduction and
        Creating and Accessing a LabVIEW Web Service tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —


                                                    © National Instruments 5571

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5571 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5572 ordinal=5572 -->
## Functions

Functions


          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      UploadedFilesList —

            UploadedFilesList returns an array of clusters that contain information about any uploaded files
            associated with the HTTP request. Each cluster contains the following components describing
            the respective uploaded file:

                     •      Local File Path —

                Local File Path is the path to the uploaded file temporarily stored by the Web services run-
               time engine.

                     •       Client File Name —

                 Client File Name is the name of the uploaded file.

                     •      Content Type —

               Content Type is the content type of the uploaded file.

                     •       Size —

                 Size is the size in bytes of the uploaded file.


5572   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5572 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5573 ordinal=5573 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReadRead PostdataPostdata

Reads any POST data associated with the current HTTP request. This VI does not
handle POST data with the multipart/form-data encoding type. Use the Read Form
Data VI to handle this encoding type.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      postdata —

    postdata returns any POST data associated with the HTTP request. Web clients can use the POST


                                                    © National Instruments 5573

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5573 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5574 ordinal=5574 -->
## Functions

Functions


          HTTP method or the POST VI to submit POST data to a Web service.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     ReadRead RequestRequest VariableVariable

       Returns the value for a single request variable associated with the current HTTP
       request. Web services include over 30 request variables that provide information such
       as server label, remote address, and cache control related to an HTTP request.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •       variable name —

             variable name specifies the request variable from which to return the value. This parameter
            provides a pull-down menu of available request variables.

               •       error in (no error) —


5574   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5574 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5575 ordinal=5575 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      value —

    value returns the value of the specified variable.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReadRead AllAll RequestRequest VariablesVariables

Reads all request variables associated with the current HTTP request. Web services
include over 30 request variables that provide information such as server label, remote
address, and cache control related to an HTTP request.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service


                                                    © National Instruments 5575

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5575 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5576 ordinal=5576 -->
## Functions

Functions


           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      request variables —

            request variables is a cluster that contains two 1D arrays that contain the Key, or name, and
            Value of the request variables associated with the HTTP request. Web services include over 30
            request variables that provide information such as server label, remote address, and cache
             control related to an HTTP request.

                     •     Key —

                     •      Value —


               •       error out —

             error out contains error information. This output provides standard error out functionality.

     NINI WebWeb ServerServer

      Use the NI Web Server VIs to support Web services deployed to the NI Web Server.


5576   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5576 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5577 ordinal=5577 -->
## Functions

Functions


 Palette Object   Description

 Get Auth Details  Returns the authentication details associated with the current HTTP request. The
 for NI Web       authentication details indicate which user account is logged in to the NI Web
 Server           Server.


GetGet AuthAuth DetailsDetails forfor NINI WebWeb ServerServer

Returns the authentication details associated with the current HTTP request. The
authentication details indicate which user account is logged in to the NI Web Server.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

                                                    © National Instruments 5577

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5577 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5578 ordinal=5578 -->
## Functions

Functions


          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      user ID —

            user ID returns the ID of the user currently logged in. If no user is logged in, this output returns
          an empty string.

               •     username —

          username returns the username of the user currently logged in. If no user is logged in, this
           output returns an empty string.

               •       privileges —

             privileges returns the privileges associated with the request, including privileges associated
            with a logged in user.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      ServiceService

      Use the Web Services VIs in startup VIs to access information about a LabVIEW Web
        service.


         Palette
                    Description
        Object

       Read
                    Returns information about the current Web service. Use this VI to programmatically
         Service
                    access the contents of the public and private folders of the Web service.
          Attribute


5578   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5578 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5579 ordinal=5579 -->
## Functions

Functions


 Palette            Description
 Object

 Get Web    Returns whether or not the Web service is stopping. Use this VI in a startup VI to
 Service    monitor the execution of the Web service and to stop the startup VI when the Web
 Status      service stops.


ReadRead ServiceService AttributeAttribute

Returns information about the current Web service. Use this VI to programmatically
access the contents of the public and private folders of the Web service.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service —

    LabVIEW Web Service is an identifier used by Service VIs to access information about the current
   Web service. LabVIEW Web Service works similarly to a refnum in LabVIEW, allowing you to wire
    together Service VIs within your application. You can also wire LabVIEW Web Service Request to
     this input, as LabVIEW Web Service Request inherits from LabVIEW Web Service.

   When you use Service VI(s) within a startup VI, you must assign the control wired to the original
    LabVIEW Web Service input to the connector pane for the Service VI(s) to function.

   •       attribute name —
     attribute name identifies the web service information you want to read. This parameter
    provides a pull-down menu of available attribute names, including:
         •  Private Content Path—Returns the path to the private content folder of the Web service.
         • Public Content Path—Returns the path to the public content folder of the Web service.
         • Web Service Version—Returns the version number of the Web service.
   •       error in (no error) —


                                                    © National Instruments 5579

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5579 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5580 ordinal=5580 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service out —

          LabVIEW Web Service out is used by Service VIs to reference the current Web service. Use
          LabVIEW Web Service out to wire together Service VIs within your application.

               •      value —

            value returns the web service attribute specified by attribute name as a string.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      The code shown below uses Read Service Attribute to generate the path to a specific
          file in the Public Content folder of a Web service.


      GetGet WebWeb ServiceService StatusStatus

       Returns whether or not the Web service is stopping. Use this VI in a startup VI to
      monitor the execution of the Web service and to stop the startup VI when the Web
       service stops.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


5580   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5580 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5581 ordinal=5581 -->
## Functions

Functions

Inputs/Outputs

   •     LabVIEW Web Service —

    LabVIEW Web Service is an identifier used by Service VIs to access information about the current
   Web service. LabVIEW Web Service works similarly to a refnum in LabVIEW, allowing you to wire
    together Service VIs within your application. You can also wire LabVIEW Web Service Request to
     this input, as LabVIEW Web Service Request inherits from LabVIEW Web Service.

   When you use Service VI(s) within a startup VI, you must assign the control wired to the original
    LabVIEW Web Service input to the connector pane for the Service VI(s) to function.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service out —

    LabVIEW Web Service out is used by Service VIs to reference the current Web service. Use
    LabVIEW Web Service out to wire together Service VIs within your application.

   •       service stopping? —

    service stopping? returns TRUE if the current web service is stopping.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

OutputOutput

Use the Output VIs to set HTTP settings and write streaming responses.


                                                    © National Instruments 5581

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5581 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5582 ordinal=5582 -->
## Functions

Functions


         Palette                   Description
        Object

         Set HTTP                    Sets the MIME response type for the current HTTP request. The MIME is a standard        Response                method used to indicate the format of the response including text, images, or other       MIME                     application-specific data.        Type


         Set HTTP  Sets the HTTP status code to return to the Web client for the current HTTP request. The
        Response response code indicates the outcome or status of the request. The default is HTTP code
       Code      200, which indicates a successful request.


                    Sets an HTTP header in the response stream of the current HTTP request that redirects         Set HTTP
                   the Web client to another URL. You must configure the HTTP method VI to use         Redirect                   streaming.


                    Sets an HTTP header in the response stream of the current HTTP request. The top-level
         Set HTTP  VI must be configured to use streaming. Refer to the World Wide Web Consortium
        Header    website at www.w3.org for header field definitions along with example headers,
                     descriptions, and syntax.


                    Writes a streaming response string for top-level VIs configured to use stream output
              mode on the HTTP Method VI Settings page of the Web Service Properties dialog box.
         Write     You can write the response to a buffer in memory or to the socket, and the response can
        Response be either buffered or unbuffered. If the response is buffered, use the Flush Output VI
                      after this VI to send any remaining data that remains in the buffer. The status of error in
                 does not affect the functionality of this VI.


                 Sends any remaining data written by the Write Response VI from the buffer to the
         Flush      socket. Use this VI when the top-level VI is configured to use streaming and buffering on
        Output    the HTTP Method VI Settings page of the Web Service Properties dialog box. The status
                     of error in does not affect the functionality of this VI.


5582   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5582 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5583 ordinal=5583 -->
## Functions

Functions

SetSet HTTPHTTP ResponseResponse MIMEMIME TypeType

Sets the MIME response type for the current HTTP request. The MIME is a standard
method used to indicate the format of the response including text, images, or other
application-specific data.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •     MIME type (text/html) —

   MIME type specifies the MIME response type for the current HTTP request. The default value is
   text/html, which indicates the response is standard HTML format.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web


                                                    © National Instruments 5583

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5583 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5584 ordinal=5584 -->
## Functions

Functions


             Services VIs within your application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      SetSet HTTPHTTP ResponseResponse CodeCode

       Sets the HTTP status code to return to the Web client for the current HTTP request. The
      response code indicates the outcome or status of the request. The default is HTTP
      code 200, which indicates a successful request.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      response code (200) —

           response code specifies the HTTP status code to return to the client. The default is HTTP code
             200, which indicates a successful request.

               •       error in (no error) —


5584   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5584 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5585 ordinal=5585 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SetSet HTTPHTTP RedirectRedirect

Sets an HTTP header in the response stream of the current HTTP request that redirects
the Web client to another URL. You must configure the HTTP method VI to use
streaming.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW


                                                    © National Instruments 5585

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5585 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5586 ordinal=5586 -->
## Functions

Functions


         Web Service Request control to the connector pane of the Web method VI.

               •       redirect URL —

             redirect URL specifies a redirect URL using standard URL syntax.

               •      response code (307) —

           response code specifies the HTTP status code to return to the client. The default is HTTP code
             307, which indicates a temporary redirect using the same request method. Specify HTTP code
           303 to redirect as a GET.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      SetSet HTTPHTTP HeaderHeader

       Sets an HTTP header in the response stream of the current HTTP request. The top-level
        VI must be configured to use streaming. Refer to the World Wide Web Consortium
       website at www.w3.org for header field definitions along with example headers,
       descriptions, and syntax.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


5586   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5586 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5587 ordinal=5587 -->
## Functions

Functions


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      header —

    header specifies the header field to assign a value. Refer to the World Wide Web Consortium
    header field definitions for example headers, along with descriptions and syntax.

   •      header value —

    header value specifies the value of the header field.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5587

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5587 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5588 ordinal=5588 -->
## Functions

Functions

       WriteWrite ResponseResponse

       Writes a streaming response string for top-level VIs configured to use stream output
     mode on the HTTP Method VI Settings page of the Web Service Properties dialog box.
      You can write the response to a buffer in memory or to the socket, and the response
      can be either buffered or unbuffered. If the response is buffered, use the Flush Output
        VI after this VI to send any remaining data that remains in the buffer. The status of error
       in does not affect the functionality of this VI.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      response string —

           response string specifies the response string for a top-level VI that uses streaming, which you
             configure on the HTTP Method VI Settings page of the Web Service Properties dialog box.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —


5588   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5588 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5589 ordinal=5589 -->
## Functions

Functions


    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FlushFlush OutputOutput

Sends any remaining data written by the Write Response VI from the buffer to the
socket. Use this VI when the top-level VI is configured to use streaming and buffering
on the HTTP Method VI Settings page of the Web Service Properties dialog box. The
status of error in does not affect the functionality of this VI.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides


                                                    © National Instruments 5589

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5589 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5590 ordinal=5590 -->
## Functions

Functions


            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     ConversionConversion

      Use the Conversion VIs to escape or unescape characters in a URL or convert images
        for LabVIEW Web services.


         Palette                       Description        Object

        Escape HTTP  Replaces special characters with the appropriate escape sequences according to
       URL          the URL encoding specification RFC 1738.


        Unescape     Replaces escape sequences with the corresponding special characters according to
       HTTP URL     the URL encoding specification RFC 1738.


      PNG Data to
                      Converts a PNG binary stream to a LabVIEW image.
        LV Image

        LV Image to
                      Converts a LabVIEW image to a PNG binary stream.
      PNG Data


5590   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5590 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5591 ordinal=5591 -->
## Functions

Functions

EscapeEscape HTTPHTTP URLURL

Replaces special characters with the appropriate escape sequences according to the
URL encoding specification RFC 1738.


Inputs/Outputs

   •      unescaped string in —

    unescaped string in specifies the string you want to escape.

   •      escaped string out —

    escaped string out returns an escaped string.


UnescapeUnescape HTTPHTTP URLURL

Replaces escape sequences with the corresponding special characters according to the
URL encoding specification RFC 1738.


Inputs/Outputs

   •      escaped string in —

    escaped string in specifies an escaped string.

   •      unescaped string out —

    unescaped string out returns an unescaped string.


                                                    © National Instruments 5591

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5591 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5592 ordinal=5592 -->
## Functions

Functions

     PNGPNG DataData toto LVLV ImageImage

       Converts a PNG binary stream to a LabVIEW image.

      You also can convert a LabVIEW image to a PNG binary stream using the LV Image to
     PNG Data VI.


      Inputs/Outputs

               •     png data —

          png data specifies a binary buffer that represents a PNG file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     image data —

          image data contains the LabVIEW image data.

                     •     image type —

              image type is reserved for future use.

                     •     image depth —

              image depth specifies the color depth of the image, which is the number of bits to use to
                 describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
                    pixel.

              image depth affects how LabVIEW interprets the values of image and colors.

                     •     image —

              image is an array of bytes that describes the color of each pixel in the image in raster order.


5592   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5592 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5593 ordinal=5593 -->
## Functions

Functions


  The value of image depth determines how LabVIEW interprets the value of this output.

   If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
  pixel describes the red value, the second byte describes the green value, and the third byte
  describes the blue value.

   If image depth is 8, each pixel has one byte to describe its color. The value of each bit
  corresponds to an element in colors, which stores 32-bit RGB values where the most
  significant byte is zero, followed in order by red, green, and blue values. Valid values include
  0 through 255.

   If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
  image include 0 through 15.

   If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
  values correspond to element 1 in colors.

  The size of the array might be larger than expected due to padding.

•     mask —

  mask is an array of bytes in which each bit describes mask information for a pixel. The first
  byte describes the first eight pixels, the second byte describes the next eight pixels, and so
  on.

   If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
  LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
  pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

•       colors —

  colors is an array of RGB color values that correspond to the values in image. The value of
  image depth determines how LabVIEW interprets the value of this output.

   If image depth is 24, LabVIEW ignores this output.

   If image depth is 8, the array can have 256 elements.

   If image depth is 4, the array can have 16 elements.

   If image depth is 1, the array can have 2 elements.


                                                © National Instruments 5593

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5593 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5594 ordinal=5594 -->
## Functions

Functions


                           If the array is empty for any depth other than 24 bits per pixel, the image is using the default
              LabVIEW color palette.

                     •      Rectangle —

                Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
                image.

                 Horizontal coordinates increase to the right, and vertical coordinates increase to the
               bottom.

                           •        left —

                          left is the horizontal coordinate of the left edge of the rectangle.

                           •      top —

                   top is the vertical coordinate of the top edge of the rectangle.

                           •       right —

                      right is the horizontal coordinate of the right edge of the rectangle.

                           •     bottom —

                  bottom is the vertical coordinate of the bottom edge of the rectangle.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      LVLV ImageImage toto PNGPNG DataData

       Converts a LabVIEW image to a PNG binary stream.

      You also can convert a PNG binary stream to a LabVIEW image using the PNG Data to LV
      Image VI.


5594   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5594 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5595 ordinal=5595 -->
## Functions

Functions


Inputs/Outputs

   •      compression (none) —

    The quality of the graphic is not affected by the compression, but the graphic file size and speed
     of compression are affected by this value. Valid values range from –1 to 9 and balance file
    compression with speed. The following table lists example values for compression.

     -1  Good compression and speed (default)
    0   No compression
    1   Best speed with compression
    9   Best compression

   •     image data —

    image data contains the LabVIEW image data.

         •     image type —

       image type is reserved for future use.

         •     image depth —

       image depth specifies the color depth of the image, which is the number of bits to use to
         describe the color of each pixel in the image. Valid values include 1, 4, 8, and 24 bits per
          pixel.

       image depth affects how LabVIEW interprets the values of image and colors.

         •     image —

       image is an array of bytes that describes the color of each pixel in the image in raster order.
       The value of image depth determines how LabVIEW interprets the value of this output.

              If image depth is 24, each pixel has three bytes to describe its color. The first byte for each
          pixel describes the red value, the second byte describes the green value, and the third byte


                                                    © National Instruments 5595

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5595 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5596 ordinal=5596 -->
## Functions

Functions


                 describes the blue value.

                           If image depth is 8, each pixel has one byte to describe its color. The value of each bit
                corresponds to an element in colors, which stores 32-bit RGB values where the most
                   significant byte is zero, followed in order by red, green, and blue values. Valid values include
               0 through 255.

                           If image depth is 4, the behavior is similar to when image depth is 8 except valid values in
              image include 0 through 15.

                           If image depth is 1, any value of zero in image corresponds to element 0 in colors. All other
                 values correspond to element 1 in colors.

              The size of the array might be larger than expected due to padding.

                     •     mask —

             mask is an array of bytes in which each bit describes mask information for a pixel. The first
                byte describes the first eight pixels, the second byte describes the next eight pixels, and so
                 on.

                           If a bit is zero, LabVIEW draws the corresponding pixel as transparent. If the array is empty,
              LabVIEW draws all pixels without transparency. If the array does not contain a bit for each
                   pixel in the image, LabVIEW draws any pixels missing from the array without transparency.

                     •       colors —

                 colors is an array of RGB color values that correspond to the values in image. The value of
              image depth determines how LabVIEW interprets the value of this output.

                           If image depth is 24, LabVIEW ignores this output.

                           If image depth is 8, the array can have 256 elements.

                           If image depth is 4, the array can have 16 elements.

                           If image depth is 1, the array can have 2 elements.

                           If the array is empty for any depth other than 24 bits per pixel, the image is using the default
              LabVIEW color palette.

                     •      Rectangle —


5596   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5596 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5597 ordinal=5597 -->
## Functions

Functions


        Rectangle is a cluster that contains coordinates that describe the bounding rectangle of the
        image.

         Horizontal coordinates increase to the right, and vertical coordinates increase to the
        bottom.

                •        left —

                left is the horizontal coordinate of the left edge of the rectangle.

                •      top —

            top is the vertical coordinate of the top edge of the rectangle.

                •       right —

              right is the horizontal coordinate of the right edge of the rectangle.

                •     bottom —

           bottom is the vertical coordinate of the bottom edge of the rectangle.


   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     png data —

   png data describes the binary buffer that represents a PNG file.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ApplicationApplication WebWeb ServerServer

Use the Application Web Server VIs to support Web services deployed to the
Application Web Server.

                                                    © National Instruments 5597

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5597 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5598 ordinal=5598 -->
## Functions

Functions


         Palette                  Description        Object

                Use the Output VIs to configure Embedded Server Pages (ESP) scripting on the
                   Application Web Server.        Output
                 These VIs work only when you publish Web services to the Application Web Server.


                Use the Sessions VIs to manage HTTP sessions and session variables. You can create and
                  destroy HTTP sessions, read and write session variables, and return session information.         Sessions
                 These VIs work only when you publish Web services to the Application Web Server.


                Use the Security VIs to encrypt and decrypt data transfers.
         Security
                 These VIs work only when you publish Web services to the Application Web Server.


      OutputOutput

      Use the Output VIs to configure Embedded Server Pages (ESP) scripting on the
       Application Web Server.

      These VIs work only when you publish Web services to the Application Web Server.


         Palette
                   Description
        Object

         Set ESP   Sets variables to be visible in an ESP scripting template. You can access these variables
         Variable  from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web


5598   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5598 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5599 ordinal=5599 -->
## Functions

Functions


 Palette           Description
 Object

           Services topic at ni.com for more information about using scripting with Web services.
         The data type you wire to the value input determines the polymorphic instance to use.


 Render           Executes the specified ESP scripting template. Refer to the Scripting in LabVIEW Web
 ESP           Services topic at ni.com for more information about using scripting with Web services. Template

SetSet ESPESP VariableVariable

Sets variables to be visible in an ESP scripting template. You can access these variables
from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
Services topic at ni.com for more information about using scripting with Web
services. The data type you wire to the value input determines the polymorphic
instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


  • Set String ESP Variable VI
  • Set Many String ESP Variables VI
  • Set Boolean ESP Variable VI
  • Set Many Boolean ESP Variables VI
  • Set Double ESP Variable VI
  • Set Many Double ESP Variables VI
  • Set Integer ESP Variable VI
  • Set Many Integer ESP Variables VI


                                                    © National Instruments 5599

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5599 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5600 ordinal=5600 -->
## Functions

Functions

    SetSet StringString ESPESP VariableVariable VIVI

       Sets variables to be visible in an ESP scripting template. You can access these variables
      from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
       Services topic at ni.com for more information about using scripting with Web
        services. The data type you wire to the value input determines the polymorphic
       instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      key —

           key sets the name of the ESP variable.

               •      value —

            value specifies the string value to assign to the new ESP variable.

               •       error in (no error) —


5600   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5600 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5601 ordinal=5601 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet ManyMany StringString ESPESP VariablesVariables VIVI

Sets variables to be visible in an ESP scripting template. You can access these variables
from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
Services topic at ni.com for more information about using scripting with Web
services. The data type you wire to the value input determines the polymorphic
instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service


                                                    © National Instruments 5601

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5601 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5602 ordinal=5602 -->
## Functions

Functions


           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      keys —

           keys sets the names of the ESP variables.

               •      values —

            values specifies the array of string values to assign to the new ESP variables.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet BooleanBoolean ESPESP VariableVariable VIVI

       Sets variables to be visible in an ESP scripting template. You can access these variables
      from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
       Services topic at ni.com for more information about using scripting with Web
        services. The data type you wire to the value input determines the polymorphic
       instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


5602   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5602 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5603 ordinal=5603 -->
## Functions

Functions


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      key —

    key sets the name of the ESP variable.

   •      value —

    value specifies the Boolean value to assign to the new ESP variable.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5603

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5603 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5604 ordinal=5604 -->
## Functions

Functions

    SetSet ManyMany BooleanBoolean ESPESP VariablesVariables VIVI

       Sets variables to be visible in an ESP scripting template. You can access these variables
      from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
       Services topic at ni.com for more information about using scripting with Web
        services. The data type you wire to the value input determines the polymorphic
       instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      keys —

           keys sets the names of the ESP variables.

               •      values —

            values specifies the array of Boolean values to assign to the new ESP variables.

               •       error in (no error) —


5604   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5604 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5605 ordinal=5605 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet DoubleDouble ESPESP VariableVariable VIVI

Sets variables to be visible in an ESP scripting template. You can access these variables
from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
Services topic at ni.com for more information about using scripting with Web
services. The data type you wire to the value input determines the polymorphic
instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service


                                                    © National Instruments 5605

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5605 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5606 ordinal=5606 -->
## Functions

Functions


           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      key —

           key sets the name of the ESP variable.

               •      value —

            value specifies the numeric value to assign to the new ESP variable.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    SetSet ManyMany DoubleDouble ESPESP VariablesVariables VIVI

       Sets variables to be visible in an ESP scripting template. You can access these variables
      from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
       Services topic at ni.com for more information about using scripting with Web
        services. The data type you wire to the value input determines the polymorphic
       instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


5606   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5606 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5607 ordinal=5607 -->
## Functions

Functions


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      keys —

    keys sets the names of the ESP variables.

   •      values —

    values specifies the array of numeric values to assign to the new ESP variables.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5607

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5607 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5608 ordinal=5608 -->
## Functions

Functions

    SetSet IntegerInteger ESPESP VariableVariable VIVI

       Sets variables to be visible in an ESP scripting template. You can access these variables
      from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
       Services topic at ni.com for more information about using scripting with Web
        services. The data type you wire to the value input determines the polymorphic
       instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      key —

           key sets the name of the ESP variable.

               •      value —

            value specifies the numeric value to assign to the new ESP variable.

               •       error in (no error) —


5608   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5608 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5609 ordinal=5609 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

SetSet ManyMany IntegerInteger ESPESP VariablesVariables VIVI

Sets variables to be visible in an ESP scripting template. You can access these variables
from the form variables in the ESP template. Refer to the Scripting in LabVIEW Web
Services topic at ni.com for more information about using scripting with Web
services. The data type you wire to the value input determines the polymorphic
instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service


                                                    © National Instruments 5609

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5609 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5610 ordinal=5610 -->
## Functions

Functions


           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      keys —

           keys sets the names of the ESP variables.

               •      values —

            values specifies the array of numeric values to assign to the new ESP variables.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   RenderRender ESPESP TemplateTemplate

       Executes the specified ESP scripting template. Refer to the Scripting in LabVIEW Web
       Services topic at ni.com for more information about using scripting with Web
        services.


5610   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5610 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5611 ordinal=5611 -->
## Functions

Functions

Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •     espName —

   espName specifies the ESP scripting template to execute.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


SessionsSessions

Use the Sessions VIs to manage HTTP sessions and session variables. You can create
and destroy HTTP sessions, read and write session variables, and return session
information.

These VIs work only when you publish Web services to the Application Web Server.


                                                    © National Instruments 5611

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5611 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5612 ordinal=5612 -->
## Functions

Functions


         Palette                   Description
        Object

         Create                   Creates an HTTP session for the current HTTP request.         Session

        Check If
         Session   Checks if an HTTP session is associated with the current HTTP request.
          Exists

        Get       Returns a client-side cookie for the HTTP session. Client-side cookies allow the server to
         Session   reuse the same HTTP session when the same Web client submits multiple HTTP
         ID         requests. You must first establish an HTTP session using the Create Session VI. The
        Cookie    cookie remains valid while the browser on the Web client is open.


                   Destroys the HTTP session associated with the current HTTP request. Use the Create
         Destroy                  Session VI to establish an HTTP session. The status of error in does not affect the         Session                     functionality of this VI.


       Read     Reads the value of an HTTP session variable associated with the current HTTP request.
         Session   You can create session variables by first establishing an HTTP session with the Create
         Variable  Session VI and then using the Write Session Variable VI to create the variables.


       Read All  Reads all HTTP session variables associated with the current HTTP request. You can
         Session   create session variables by first establishing an HTTP session with the Create Session VI
         Variables and then using the Write Session Variable VI to create the variables.


         Write     Creates or replaces a session variable or set of session variables associated with the
         Session   current HTTP request. The data type you wire to the value input determines the
         Variable  polymorphic instance to use.


         Delete    Deletes the HTTP session variable associated with the name key. You can create session
         Session   variables by first establishing an HTTP session with the Create Session VI and then using
         Variable  the Write Session Variable VI to create the variables.


5612   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5612 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5613 ordinal=5613 -->
## Functions

Functions

CreateCreate SessionSession

Creates an HTTP session for the current HTTP request.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      timeout (60000 msec) —

    timeout (60000 msec) specifies the maximum idle time, in milliseconds, before a HTTP session
    times out. The VI completes execution immediately after creating the session. The Web Server
    monitors and deletes the session after the session times out. If you specify zero or less as the
     value, the VI uses the default value (60000 msec).

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web


                                                    © National Instruments 5613

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5613 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5614 ordinal=5614 -->
## Functions

Functions


             Services VIs within your application.

               •      session ID cookie —

            session ID cookie returns a client-side cookie that allows the server to reuse the same HTTP
            session when the same Web client submits another HTTP request. The cookie remains valid
            while the browser on the Web client is open.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   CheckCheck IfIf SessionSession ExistsExists

      Checks if an HTTP session is associated with the current HTTP request.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •       error in (no error) —


5614   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5614 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5615 ordinal=5615 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      session exists? —

    session exists? returns whether an HTTP session is associated with the current HTTP request.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet SessionSession IDID CookieCookie

Returns a client-side cookie for the HTTP session. Client-side cookies allow the server
to reuse the same HTTP session when the same Web client submits multiple HTTP
requests. You must first establish an HTTP session using the Create Session VI. The
cookie remains valid while the browser on the Web client is open.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing


                                                    © National Instruments 5615

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5615 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5616 ordinal=5616 -->
## Functions

Functions


           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      session ID cookie —

            session ID cookie returns a client-side cookie that allows the server to reuse the same HTTP
            session when the same Web client submits another HTTP request. The cookie remains valid
            while the browser on the Web client is open.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    DestroyDestroy SessionSession

       Destroys the HTTP session associated with the current HTTP request. Use the Create
       Session VI to establish an HTTP session. The status of error in does not affect the
       functionality of this VI.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


5616   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5616 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5617 ordinal=5617 -->
## Functions

Functions


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

ReadRead SessionSession VariableVariable

Reads the value of an HTTP session variable associated with the current HTTP request.
You can create session variables by first establishing an HTTP session with the Create
Session VI and then using the Write Session Variable VI to create the variables.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


                                                    © National Instruments 5617

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5617 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5618 ordinal=5618 -->
## Functions

Functions


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      key —

           key identifies the name of the session variable to create or replace.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      value —

            value returns the value of the specified variable.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5618   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5618 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5619 ordinal=5619 -->
## Functions

Functions

ReadRead AllAll SessionSession VariablesVariables

Reads all HTTP session variables associated with the current HTTP request. You can
create session variables by first establishing an HTTP session with the Create Session
VI and then using the Write Session Variable VI to create the variables.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      session variables —


                                                    © National Instruments 5619

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5619 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5620 ordinal=5620 -->
## Functions

Functions


            session variables is a cluster that contains two 1D arrays that contain the Key, or name, and
            Value of the session variables associated with the HTTP request.

                     •     Key —

                     •      Value —


               •       error out —

             error out contains error information. This output provides standard error out functionality.

    WriteWrite SessionSession VariableVariable

       Creates or replaces a session variable or set of session variables associated with the
       current HTTP request. The data type you wire to the value input determines the
      polymorphic instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


            • Write Single Session Variable VI
            • Write Many Session Variables VI
            • Write Boolean Session Variable VI
            • Write Many Boolean Session Variables VI
            • Write Double Session Variable VI
            • Write Many Double Session Variables VI
            • Write Integer Session Variable VI
            • Write Many Integer Session Variables VI


5620   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5620 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5621 ordinal=5621 -->
## Functions

Functions

WriteWrite SingleSingle SessionSession VariableVariable VIVI

Creates or replaces a session variable or set of session variables associated with the
current HTTP request. The data type you wire to the value input determines the
polymorphic instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      key —

    key identifies the name of the session variable to create or replace.

   •      value —

    value specifies the value to assign to the session variable.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 5621

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5621 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5622 ordinal=5622 -->
## Functions

Functions

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      previous value —

            previous value returns the value of the session variable overwritten by the VI.

               •      replaced? —

            replaced? indicates whether the VI overwrote a session variable. replaced? returns FALSE if the
              VI created a new session variable.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    WriteWrite ManyMany SessionSession VariablesVariables VIVI

       Creates or replaces a session variable or set of session variables associated with the
       current HTTP request. The data type you wire to the value input determines the
      polymorphic instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific


5622   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5622 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5623 ordinal=5623 -->
## Functions

Functions


  HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
  you to wire together Web Services VIs within your application. You must wire Web Services VIs to
  the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
  Request out terminal of another VI.

  When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
  Web Service Request control to the connector pane of the Web method VI.

•      keys —

  keys identifies an array of names for session variables to create or replace.

•      values —

  values specifies an array of values to assign to the session variables.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     LabVIEW Web Service Request out —

  LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
  reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
  Services VIs within your application.

•      previous values —

  previous values returns an array of values for session variables overwritten by the VI.

•      replaced ? —

  replaced ? indicates whether the VI overwrote any session variables.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 5623

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5623 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5624 ordinal=5624 -->
## Functions

Functions

    WriteWrite BooleanBoolean SessionSession VariableVariable VIVI

       Creates or replaces a session variable or set of session variables associated with the
       current HTTP request. The data type you wire to the value input determines the
      polymorphic instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      key —

           key identifies the name of the session variable to create or replace.

               •      value —

            value specifies the Boolean value to assign to the session variable.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


5624   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5624 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5625 ordinal=5625 -->
## Functions

Functions

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      previous value —

    previous value returns the value of the session variable overwritten by the VI.

   •      replaced? —

    replaced? indicates whether the VI overwrote a session variable. replaced? returns FALSE if the
     VI created a new session variable.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WriteWrite ManyMany BooleanBoolean SessionSession VariablesVariables VIVI

Creates or replaces a session variable or set of session variables associated with the
current HTTP request. The data type you wire to the value input determines the
polymorphic instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific


                                                    © National Instruments 5625

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5625 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5626 ordinal=5626 -->
## Functions

Functions


          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      keys —

           keys identifies an array of names for session variables to create or replace.

               •      values —

            values specifies the array of Boolean values to assign to the session variables.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      previous values —

            previous values returns an array of values for session variables overwritten by the VI.

               •      replaced ? —

            replaced ? indicates whether the VI overwrote any session variables.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5626   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5626 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5627 ordinal=5627 -->
## Functions

Functions

WriteWrite DoubleDouble SessionSession VariableVariable VIVI

Creates or replaces a session variable or set of session variables associated with the
current HTTP request. The data type you wire to the value input determines the
polymorphic instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      key —

    key identifies the name of the session variable to create or replace.

   •      value —

    value specifies the numeric value to assign to the session variable.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 5627

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5627 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5628 ordinal=5628 -->
## Functions

Functions

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      previous value —

            previous value returns the value of the session variable overwritten by the VI.

               •      replaced? —

            replaced? indicates whether the VI overwrote a session variable. replaced? returns FALSE if the
              VI created a new session variable.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    WriteWrite ManyMany DoubleDouble SessionSession VariablesVariables VIVI

       Creates or replaces a session variable or set of session variables associated with the
       current HTTP request. The data type you wire to the value input determines the
      polymorphic instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific


5628   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5628 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5629 ordinal=5629 -->
## Functions

Functions


  HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
  you to wire together Web Services VIs within your application. You must wire Web Services VIs to
  the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
  Request out terminal of another VI.

  When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
  Web Service Request control to the connector pane of the Web method VI.

•      keys —

  keys identifies an array of names for session variables to create or replace.

•      values —

  values specifies the array of numeric values to assign to the session variables.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     LabVIEW Web Service Request out —

  LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
  reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
  Services VIs within your application.

•      previous values —

  previous values returns an array of values for session variables overwritten by the VI.

•      replaced ? —

  replaced ? indicates whether the VI overwrote any session variables.

•       error out —

  error out contains error information. This output provides standard error out functionality.


                                                   © National Instruments 5629

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5629 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5630 ordinal=5630 -->
## Functions

Functions

    WriteWrite IntegerInteger SessionSession VariableVariable VIVI

       Creates or replaces a session variable or set of session variables associated with the
       current HTTP request. The data type you wire to the value input determines the
      polymorphic instance to use.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      key —

           key identifies the name of the session variable to create or replace.

               •      value —

            value specifies the numeric value to assign to the session variable.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.


5630   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5630 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5631 ordinal=5631 -->
## Functions

Functions

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      previous value —

    previous value returns the value of the session variable overwritten by the VI.

   •      replaced? —

    replaced? indicates whether the VI overwrote a session variable. replaced? returns FALSE if the
     VI created a new session variable.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

WriteWrite ManyMany IntegerInteger SessionSession VariablesVariables VIVI

Creates or replaces a session variable or set of session variables associated with the
current HTTP request. The data type you wire to the value input determines the
polymorphic instance to use.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific


                                                    © National Instruments 5631

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5631 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5632 ordinal=5632 -->
## Functions

Functions


          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      keys —

           keys identifies an array of names for session variables to create or replace.

               •      values —

            values specifies the array of numeric values to assign to the session variables.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •      previous values —

            previous values returns an array of values for session variables overwritten by the VI.

               •      replaced ? —

            replaced ? indicates whether the VI overwrote any session variables.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5632   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5632 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5633 ordinal=5633 -->
## Functions

Functions

DeleteDelete SessionSession VariableVariable

Deletes the HTTP session variable associated with the name key. You can create
session variables by first establishing an HTTP session with the Create Session VI and
then using the Write Session Variable VI to create the variables.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      key —

    key identifies the session variable to delete. This value must match the key value used to create
    the session variable with the Write Session Variable VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to


                                                    © National Instruments 5633

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5633 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5634 ordinal=5634 -->
## Functions

Functions


             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


       SecuritySecurity

      Use the Security VIs to encrypt and decrypt data transfers.

      These VIs work only when you publish Web services to the Application Web Server.


         Palette                  Description        Object

                 Encrypts data using the key associated with the current HTTP request. Associate a key        Encrypt                 with the current HTTP request using the ConfigKey VI or by logging in a user.


                 Decrypts data using the key associated with the current HTTP request. Associate a key
        Decrypt                 with the current HTTP request using the ConfigKey VI or by logging in a user.


        Get     Returns the authentication details associated with the current HTTP request. If you
        Auth    published Web services to the NI Web Server, use the Get Auth Details for NI Web Server VI
          Details   instead.

   EncryptEncrypt

       Encrypts data using the key associated with the current HTTP request. Associate a key
       with the current HTTP request using the ConfigKey VI or by logging in a user.


5634   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5634 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5635 ordinal=5635 -->
## Functions

Functions

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •      data —

    data specifies the data to encrypt.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     LabVIEW Web Service Request out —

    LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
    reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
    Services VIs within your application.

   •      encrypted data —

    encrypted data returns the encrypted data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5635

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5635 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5636 ordinal=5636 -->
## Functions

Functions

   DecryptDecrypt

       Decrypts data using the key associated with the current HTTP request. Associate a key
       with the current HTTP request using the ConfigKey VI or by logging in a user.

           Note For more information about concepts in this topic, refer to the Web
               services introduction and tutorial.


      Inputs/Outputs

               •     LabVIEW Web Service Request —

          LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
          HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
           you to wire together Web Services VIs within your application. You must wire Web Services VIs to
            the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
           Request out terminal of another VI.

         When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
         Web Service Request control to the connector pane of the Web method VI.

               •      encrypted data —

           encrypted data specifies the data to decrypt.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.


5636   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5636 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5637 ordinal=5637 -->
## Functions

Functions

   •      decrypted data —

    decrypted data returns the decrypted data.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

GetGet AuthAuth DetailsDetails

Returns the authentication details associated with the current HTTP request. If you
published Web services to the NI Web Server, use the Get Auth Details for NI Web
Server VI instead.

      Note For more information about concepts in this topic, refer to the Web
        services introduction and tutorial.


Inputs/Outputs

   •     LabVIEW Web Service Request —

    LabVIEW Web Service Request is an identifier used by Web Services VIs to reference a specific
   HTTP request. LabVIEW Web Service Request works similarly to a refnum in LabVIEW, allowing
    you to wire together Web Services VIs within your application. You must wire Web Services VIs to
    the LabVIEW Web Service Request control or an existing value from the LabVIEW Web Service
    Request out terminal of another VI.

   When you use Web Services VI(s) within a Web method VI, you must assign the original LabVIEW
   Web Service Request control to the connector pane of the Web method VI.

   •       error in (no error) —


                                                    © National Instruments 5637

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5637 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5638 ordinal=5638 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     LabVIEW Web Service Request out —

          LabVIEW Web Service Request out is an identifier that VIs on the Web Services palette use to
             reference a specific HTTP request. Use LabVIEW Web Service Request out to wire together Web
             Services VIs within your application.

               •     username —

          username returns the username of the user currently logged in. If no user is logged in, this
           output returns an empty string.

               •      groups —

           groups returns the groups of the user associated with the request. If no user is logged in, this
           output returns the group everyone.

               •      permissions —

            permissions returns the permissions associated with the request, including permissions
            associated with a logged in user and groups that user belongs to.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      key —

           key returns the unique key associated with the login session. A key is associated with the
            request when a user successfully logs in. Each login session generates a unique key. The Encrypt,
            Decrypt, HTTP client Encrypt, and HTTP client Decrypt VIs encrypt and decrypt data using this
           key or a key that the ConfigKey VI generates.

     .NET.NET

      Use the .NET functions to create .NET objects, set properties or call methods on those
       objects, and handle events for those objects in the .NET environment. You also can
       create a .NET control on the front panel.


5638   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5638 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5639 ordinal=5639 -->
## Functions

Functions

      Note

        Creating and communicating with .NET objects in LabVIEW requires the .NET
      CLR 4.0 that installs with LabVIEW. You must use a .NET 2.0 configuration file
             if you want to load .NET 2.0 mixed-mode assemblies. Refer to the
       requirements for using .NET with LabVIEW for more information about .NET
         restrictions in LabVIEW.

        National Instruments strongly recommends that you use .NET objects only in
       LabVIEW projects.


The functions on this palette can return Windows connectivity error codes.

Refer to the labview\examples\Connectivity\Dot NET directory for
examples using the .NET functions.


 Palette             Description
 Object

 Constructor  Creates an instance of a .NET object. This node identifies the constructor from which
 Node        to create a .NET object.

 Property
 Node       Gets (reads) and/or sets (writes) properties of a reference.
 (.NET)

 Invoke
             Invokes a method or action on a reference. Most methods have associated
 Node
             parameters.
 (.NET)

 Close
             Closes a refnum associated with an open VI, VI object, an open application instance,
 Reference
             or a .NET, ActiveX or Python object.
 Function

 To More     Typecasts a reference, such as a control or a type definition, to a more generic class or
 Generic      interface in the inheritance hierarchy.


                                                    © National Instruments 5639

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5639 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5640 ordinal=5640 -->
## Functions

Functions


         Palette                     Description
        Object

         Class
         Function

        To More
          Specific     Typecasts a reference, such as a control or a type definition, to a more specific class or
         Class         interface in the inheritance hierarchy.
         Function

        .NET Object                     Converts a .NET object to a LabVIEW variant.        To Variant


                     Converts a LabVIEW data type to a .NET object. You can convert numeric (except
        To .NET                    extended precision and complex), string, Boolean, timestamp, path, .NET refnum, and
         Object                      array data types.

         Register     Registers a VI to be called when an event occurs. You use this function to register and
        Event       handle .NET and ActiveX events. LabVIEW uses the type of the input reference wired to
         Callback    each item to determine the events for which you can register.

         Unregister
         For Events   Unregisters all events associated with an event registration refnum.
         Function

                     Maintains a static reference to a VI. You can configure the Static VI Reference function
          Static VI     to output a generic or strictly typed VI reference. After you place the Static VI
         Reference   Reference function on a block diagram, double-click the function to display a file
                      dialog box where you can select a VI.

      ConstructorConstructor NodeNode

       Creates an instance of a .NET object. This node identifies the constructor from which to
       create a .NET object.


5640   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5640 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5641 ordinal=5641 -->
## Functions

Functions

Inputs/Outputs

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     new reference —

   new reference returns the reference to a .NET object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


When you place this node on the block diagram, LabVIEW displays the Select .NET
Constructor dialog box. You also can double-click the node to display the dialog box.
Some constructors can contain initialization parameters you can use to create a .NET
object in a particular state. Not all constructors have initialization parameters.

      Tip If you encounter problems loading a particular assembly or accessing
        objects in an assembly, debug the assembly call or use the .NET Assemblies
         in Memory dialog box to verify that the correct version of the assembly is in
      memory.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Dot NET\Calling a Private
   .NET Assembly.vi
  • labview\examples\Connectivity\Dot NET\Task Monitor Using
   .NET Objects.vi

PropertyProperty NodeNode (.NET)(.NET)

Gets (reads) and/or sets (writes) properties of a reference.


                                                    © National Instruments 5641

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5641 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5642 ordinal=5642 -->
## Functions

Functions

      The Property Node (.NET) is preconfigured to access VISA properties, .NET properties,
      and ActiveX properties. The node operates in the same way as a standard Property
      Node.


      Inputs/Outputs

               •      reference —
            reference is the refnum associated with the .NET object for which you want to set or get
             properties.
               •       error in (no error) —
             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.
               •      reference out —
            reference out returns reference unchanged.
               •       error out —
             error out contains error information. This output provides standard error out functionality.
               •      Property —
            property 1..n are examples of properties you want to get (read).

           If you right-click the Property Node (.NET) and select Select Class».NET»Browse from
       the shortcut menu, LabVIEW displays the Select Object From Assembly dialog box.

       Select a property from the shortcut menu to set a property for the object. You also can
        select .NET-specific properties for a .NET object. On the block diagram, right-click a
      .NET object, select Create»Property Node, and select a .NET-specific property from the
       shortcut menu.

            Tip If you encounter problems loading a particular assembly or accessing
               objects in an assembly, debug the assembly call or use the .NET Assemblies
                in Memory dialog box to verify that the correct version of the assembly is in
            memory.


5642   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5642 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5643 ordinal=5643 -->
## Functions

Functions

InvokeInvoke NodeNode (.NET)(.NET)

Invokes a method or action on a reference. Most methods have associated parameters.

The node operates in the same way as a standard Invoke Node.


Inputs/Outputs

   •      reference —
    reference is the refnum associated with the .NET object on which you want to invoke a method
    or perform an action.
   •       error in (no error) —
    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.
   •     Method —
    input 1..n are example input parameters of a method.
   •      reference out —
    reference out returns reference unchanged.
   •       error out —
    error out contains error information. This output provides standard error out functionality.
   •     Method —
    return value is an example return value of a method.
   •     param —

    output 1..n are example output parameters of a method.


If you right-click the Invoke Node (.NET) and select Select Class».NET»Browse from
the shortcut menu, LabVIEW displays the Select Object From Assembly dialog box.

On the front panel or block diagram, right-click a .NET object, select Create»Invoke
Node, and select a method from the shortcut menu to invoke a method for the object.
You also can invoke .NET-specific methods for a .NET object. On the block diagram,
right-click a .NET object, select Create»Invoke Node, and select a .NET-specific
method from the shortcut menu.

                                                    © National Instruments 5643

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5643 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5644 ordinal=5644 -->
## Functions

Functions

            Tip If you encounter problems loading a particular assembly or accessing
               objects in an assembly, debug the assembly call or use the .NET Assemblies
                in Memory dialog box to verify that the correct version of the assembly is in
            memory.

     CloseClose ReferenceReference FunctionFunction

       Closes a refnum associated with an open VI, VI object, an open application instance, or
      a .NET, ActiveX or Python object.


      Inputs/Outputs

               •      reference —

            reference is the refnum associated with an open VI, VI object, an open application instance, or a
           .NET or ActiveX object. reference also accepts 1D arrays of references.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When you create a refnum to a VI, LabVIEW loads the VI into memory. The VI stays in
     memory until you close the refnum and until the VI meets the following conditions:

            • There are no other open references to the referenced VI.
            • The front panel of the VI is not open.
            • The VI is not a subVI of another VI in memory.
            • The VI is not a member of an open project library.

5644   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5644 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5645 ordinal=5645 -->
## Functions

Functions

ToTo MoreMore GenericGeneric ClassClass FunctionFunction

Typecasts a reference, such as a control or a type definition, to a more generic class or
interface in the inheritance hierarchy.

For example, if Class A inherits from Class B, the function upcasts a variable of type A
to a variable of type B.

You can use the To More Generic Class function for casting any class hierarchy in
LabVIEW, including VI Server refnums, .NET/ActiveX refnums, and LabVIEW classes or
interfaces.


Inputs/Outputs

   •       target class —

    target class is the class or interface to which you want to upcast reference.

    You can wire a class specifier constant or any wire of the target type to this input.
   •      reference —

    reference is the refnum or LabVIEW class or interface to upcast.

   •      generic class reference —

    generic class reference is the upcasted reference.

       If an error occurs, generic class reference is Not A Refnum.


This function does not have error in and error out parameters because LabVIEW can
determine at edit time whether you have wired the reference to a compatible target
class. If you wire the reference to an incompatible target class, the wire breaks and
you receive a Class conflict error.

You can use the To More Generic Class function to manipulate the properties or


                                                    © National Instruments 5645

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5645 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5646 ordinal=5646 -->
## Functions

Functions

      methods from a more generic class or interface than that of the reference. For
      example, you can wire an enum control reference to the To More Generic Class
       function to upcast the reference to the Numeric class. You then can manipulate the
      Numeric class properties of the control, but you no longer can access the specific
       properties of the Enum class.

       Wire a Facade VI refnum to reference and a VI refnum to target class to upcast from
      Facade VI to VI.

      Related Information

       Casting LabVIEW Classes

     ToTo MoreMore SpecificSpecific ClassClass FunctionFunction

       Typecasts a reference, such as a control or a type definition, to a more specific class or
        interface in the inheritance hierarchy.

       For example, if Class A inherits from Class B, a variable of type B can hold a value of
       type A. You can use the function to downcast from type B to type A. If the typecast is
        invalid, this function returns an error at run time.

      You can use the To More Specific Class function for casting any class hierarchy in
      LabVIEW, including VI Server refnums, .NET/ActiveX refnums, and LabVIEW classes or
        interfaces.


      Inputs/Outputs

               •       target class —

             target class is the class or interface to which you want to downcast reference.

           You can wire a class specifier constant or any wire of the target type to this input.
               •      reference —


5646   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5646 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5647 ordinal=5647 -->
## Functions

Functions


    reference is the refnum or LabVIEW class or interface to downcast.

   •       error in —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       specific class reference —

     specific class reference is the downcast reference.

       If the target class is incompatible with the reference, the function returns an error and specific
     class reference is Not A Refnum.
   •       error out —

    error out contains error information. This output provides standard error out functionality.


You can use the To More Specific Class function to manipulate the properties or
methods from a more specific class or interface than that of the reference. For
example, if you build an array of references to boolean, numeric, and string controls,
LabVIEW casts these references to the more generic Control class because an array can
contain only one data type, and each of these controls is a member of the Control
class. If you then want to manipulate the properties for only the boolean controls in
the array, you can create a reference to the array and use the To More Specific Class
function to downcast the array reference to the Boolean class.

Wire a VI refnum to reference and a Facade VI refnum to target class to downcast from
VI to Facade VI.

You also can use data value references to downcast classes. The To More Specific Class
function waits to execute until the reference is available for downcast. To downcast a
class or interface, wire the data value reference of the target class or interface to target
class.

Related Information

Casting LabVIEW Classes


                                                    © National Instruments 5647

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5647 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5648 ordinal=5648 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Application Control\VI Server\To More
        Specific Class\To More Specific Class.vi

     .NET.NET ObjectObject ToTo VariantVariant

       Converts a .NET object to a LabVIEW variant.


      Inputs/Outputs

               •      .NET object —

           .NET Object is the .NET object you want to convert to a LabVIEW variant.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       variant —

             variant is the resulting variant data.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     ToTo .NET.NET ObjectObject

       Converts a LabVIEW data type to a .NET object. You can convert numeric (except
      extended precision and complex), string, Boolean, timestamp, path, .NET refnum, and
       array data types.


5648   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5648 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5649 ordinal=5649 -->
## Functions

Functions


Inputs/Outputs

   •      anything —

    anything is any LabVIEW data you want to convert. This parameter is polymorphic.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

       If an error occurs before this node executes, the node only closes the reference passed to it.

   •      .NET object —

    .NET Object is the resulting .NET object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

RegisterRegister EventEvent CallbackCallback

Registers a VI to be called when an event occurs. You use this function to register and
handle .NET and ActiveX events. LabVIEW uses the type of the input reference wired to
each item to determine the events for which you can register.

You can resize the function to register multiple event callbacks at once for the same
.NET or ActiveX object or for a different object.

      Note If you wire Register Event Callback functions together by wiring the
       event callback ref out output of one function to the event callback ref input
        of another function, the last function in the series overwrites all the previous
        Register Event Callback functions.


                                                    © National Instruments 5649

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5649 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5650 ordinal=5650 -->
## Functions

Functions


      Inputs/Outputs

               •      event callback refnum —

           event callback ref accepts a reference to an existing event callback registration.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      event source —

           event source ref accepts a .NET object or an ActiveX automation reference. Click the down arrow
            next to this input and select the type of event you want to generate, such as Mouse Down or
           Double Click. References must be to local objects. You cannot wire a reference to a remote
             object.

               •       VI Ref —

              vi reference is a strict VI reference to the callback VI.

              vi reference must match exactly the data from the registered event and the callback VI must be
             reentrant.
               •      User Parameter —

            user parameter contains data that you want to pass to the callback VI when the .NET or ActiveX
             object generates the event.

            For example, you can wire a string that includes a text message to the user parameter input to
                tell a user for which control the event occurred. If you want to use this parameter, you must wire
                   it before you create the callback VI. You can wire any LabVIEW data type, including a cluster, to
              this parameter.
               •      event callback refnum —

           event callback ref out returns a reference to a new or existing callback registration.


5650   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5650 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5651 ordinal=5651 -->
## Functions

Functions

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Use this function to register .NET and ActiveX events only. To unregister an event for
.NET or ActiveX, wire the event callback ref out output to the Unregister For Events
function.

Use the Event structure or the Register For Events function to register and handle non-
.NET or non-ActiveX events dynamically.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Excel\Excel - ActiveX Event
   Callback.vi
  • labview\examples\Connectivity\ActiveX\ActiveX Event
   Callback.vi
  • labview\examples\Connectivity\Dot NET\Passing Data to a
   .NET Event Callback.vi

UnregisterUnregister ForFor EventsEvents FunctionFunction

Unregisters all events associated with an event registration refnum.

Event structures that use this event registration refnum no longer receive any dynamic
events. National Instruments recommends that you unregister for events when you no
longer need to handle them. If you do not unregister for events, LabVIEW continues to
generate and queue the events as long as the VI runs, even if no Event structure is
waiting to handle them, which consumes memory and can hang the VI if you enable
front panel locking for the events.


                                                    © National Instruments 5651

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5651 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5652 ordinal=5652 -->
## Functions

Functions

      Inputs/Outputs

               •      event registration refnum —

           event registration refnum is a reference to an existing event registration a Register For Events
             function created.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      StaticStatic VIVI ReferenceReference

       Maintains a static reference to a VI. You can configure the Static VI Reference function
       to output a generic or strictly typed VI reference. After you place the Static VI Reference
       function on a block diagram, double-click the function to display a file dialog box
      where you can select a VI.


      Inputs/Outputs

               •    —

              vi reference is the refnum associated with the configured VI.

                    If the VI is not valid, vi reference contains Not A Refnum.

      The Static VI Reference function acts as a subVI and appears in the VI hierarchy of the
       top-level VI. By default, the output is a generic VI reference.


5652   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5652 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5653 ordinal=5653 -->
## Functions

Functions

You can change the output of this function to a strictly typed VI reference. Right-click
the function and select Strictly Typed VI Reference from the shortcut menu to change
the output. A red star in the upper left corner of the function icon indicates the
reference is strictly typed. The strictly typed VI reference identifies the connector pane
of the VI you are calling. You can create a strictly typed VI reference only from a VI or VI
template, not from a polymorphic VI or other non-VI file such as a global variable or
control.

Use a strictly typed VI reference if you want to call the referenced VI with the Call By
Reference node or the Start Asynchronous Call node. When you create a strictly typed
VI reference, you cannot wire vi reference to the Run VI method. You cannot use the
Run VI method to run a VI that is already reserved for execution by another VI. A strictly
typed static VI reference also reserves any subVIs when a top-level VI is reserved, thus
making it ineligible for the Run VI method. Refer to the Run VI method for more
information.

LabVIEW loads the referenced VI into memory when you load the top-level VI. When
the Static VI Reference function outputs a strictly typed VI reference, LabVIEW reserves
the referenced VI as long as the top-level VI is running. LabVIEW closes this reference
when the top-level VI is no longer in memory. You do not have to explicitly close the
reference this function returns.

      Note LabVIEW does not check whether the referenced VI can compile. If the
        referenced VI is broken, LabVIEW does not recognize that it is broken until
       you run the top-level VI. If you execute an Open VI Reference function that
        references the broken VI, you receive an error.

            If you want LabVIEW to check for a broken referenced VI before you run the
        top-level VI, use the referenced VI directly in the top-level VI instead of using a
         Static VI Reference function by clicking the Select a VI icon or text on the
       Functions palette and navigating to the VI you want to add to the block
       diagram.

InputInput DeviceDevice ControlControl

Use the Input Device Control VIs to obtain information about the joystick, keyboard, or

                                                    © National Instruments 5653

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5653 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5654 ordinal=5654 -->
## Functions

Functions

     mouse connected to a computer.

      Use the Query Input Devices VI to obtain information about the devices connected to a
      computer. Use the appropriate Initialize VI to open a reference to and initialize a
       device. Use the Acquire Input Data VI to acquire the data you want. Use the Close Input
       Device VI to close the reference to the device. Refer to the Input Device Control VI Error
      Codes for more information about error codes.

      (Windows) You must have DirectX 8.0 or later to use the Input Device Control VIs.


         Palette
                   Description        Object

           Initialize                Opens a reference to and initializes a joystick device at the index you specify.
         Joystick

           Initialize
                Opens a reference to and initializes the keyboard connected to the computer.        Keyboard

           Initialize                Opens a reference to and initializes the mouse connected to the computer.       Mouse

        Query
         Input     Obtains information about the devices connected to the computer.
         Devices

         Acquire
                   Returns data about the device connected to the computer. Wire data to the device ID
         Input
                    input to determine the polymorphic instance to use or manually select the instance.
        Data

         Close
                   Closes the device you specify in device ID. Wire data to the device ID input to determine
         Input
                   the polymorphic instance to use or manually select the instance.
         Device


5654   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5654 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5655 ordinal=5655 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Input Device Control\
   Monitoring Keyboard and Mouse Activity.vi

InitializeInitialize JoystickJoystick

Opens a reference to and initializes a joystick device at the index you specify.

(Windows) You must have DirectX 8.0 or later to use this VI.


Inputs/Outputs

   •      device index —

    device index is the index of the joystick you want to initialize. The default is 0. Set device index
    to 0 if you have only one joystick connected to the computer.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      device ID —

    device ID identifies which device you initialized.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

InitializeInitialize KeyboardKeyboard

Opens a reference to and initializes the keyboard connected to the computer.

                                                    © National Instruments 5655

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5655 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5656 ordinal=5656 -->
## Functions

Functions

      (Windows) You must have DirectX 8.0 or later to use this VI.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      device ID —

            device ID identifies which device you initialized.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

       InitializeInitialize MouseMouse

      Opens a reference to and initializes the mouse connected to the computer.

      (Windows) You must have DirectX 8.0 or later to use this VI.


      Inputs/Outputs

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      device ID —


5656   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5656 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5657 ordinal=5657 -->
## Functions

Functions


    device ID identifies which device you initialized.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

QueryQuery InputInput DevicesDevices

Obtains information about the devices connected to the computer.

(Windows) You must have DirectX 8.0 or later to use this VI.


Inputs/Outputs

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       joystick info —

     joystick info contains information about the joysticks connected to the computer.

         •      axes total —

        axes total (Windows) is the total number of axes for each joystick connected to the
        computer.

         •      buttons total —

        buttons total (Windows) is the total number of buttons for each joystick connected to the
        computer.

         •     pov total —


                                                    © National Instruments 5657

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5657 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5658 ordinal=5658 -->
## Functions

Functions


              pov total (Windows) is the total number of points of view for each joystick connected to the
                computer.

                     •      device name —

                device name is the device name of each joystick connected to the computer.


               •      key info —

           key info contains information about the keyboard connected to the computer.

                     •      buttons total —

               buttons total (Windows) is the number of keys on the keyboard connected to the computer.

                     •      device name —

                device name is the device name of the keyboard connected to the computer.


               •     mouse info —

         mouse info contains information about the mouse connected to the computer.

                     •      axes total —

               axes total (Windows) is the total number of axes for the mouse connected to the computer.

                     •      buttons total —

               buttons total (Windows) is the total number of buttons for the mouse connected to the
                computer.

                     •      device name —

                device name is the device name of the mouse connected to the computer.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


5658   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5658 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5659 ordinal=5659 -->
## Functions

Functions

The operating system recognizes more than one mouse or keyboard but interprets
them to be one virtual mouse/keyboard. LabVIEW cannot return the output for each
device separately but returns only the sum of both outputs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Input Device Control\
   Monitoring Keyboard and Mouse Activity.vi

AcquireAcquire InputInput DataData

Returns data about the device connected to the computer. Wire data to the device ID
input to determine the polymorphic instance to use or manually select the instance.

(Windows) You must have DirectX 8.0 or later to use this VI.


  • joystickAcquire VI
  • keyboardAcquire VI
  • mouseAcquire VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Input Device Control\
   Monitoring Keyboard and Mouse Activity.vi

joystickAcquirejoystickAcquire VIVI

Returns data about the device connected to the computer. Wire data to the device ID
input to determine the polymorphic instance to use or manually select the instance.

(Windows) You must have DirectX 8.0 or later to use this VI.

                                                    © National Instruments 5659

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5659 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5660 ordinal=5660 -->
## Functions

Functions


      Inputs/Outputs

               •      device ID —

            device ID identifies which device you acquired data from.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      device ID —

            device ID identifies which device to acquire data from.

               •       axis info —

             axis info contains numeric values for the axes. The number of axes depend on the specific
              joystick.

         When you use this VI on a myRIO target, the value of axis info is the raw data value this VI
            acquires from the joystick.

                     •     X axis —

              X axis is the numeric value of the x-axis.

                     •      Y axis —

               Y axis is the numeric value of the y-axis.

                     •     Z axis —

              Z axis is the numeric value of the z-axis.

                     •     X axis rotation —


5660   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5660 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5661 ordinal=5661 -->
## Functions

Functions


     X axis rotation is the numeric value of the x-axis rotation.

      •      Y axis rotation —

      Y axis rotation is the numeric value of the y-axis rotation.

      •     Z axis rotation —

     Z axis rotation is the numeric value of the z-axis rotation (rudder).

      •    U axis —

    U axis is the numeric value of the u-axis.

      •     V axis —

     V axis is the numeric value for the v-axis.


•      button info —

  button info contains Boolean values for up to 32 buttons. A TRUE value indicates that the button
  was pressed when the VI ran.

      •      button 1 —

      •      button 2 —

      •      button 3 —

      •      button 4 —

      •      button 5 —

      •      button 6 —

      •      button 7 —

      •      button 8 —

      •      button 9 —


                                                   © National Instruments 5661

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5661 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5662 ordinal=5662 -->
## Functions

Functions


                     •      button 10 —

                     •      button 11 —

                     •      button 12 —

                     •      button 13 —

                     •      button 14 —

                     •      button 15 —

                     •      button 16 —

                     •      button 17 —

                     •      button 18 —

                     •      button 19 —

                     •      button 20 —

                     •      button 21 —

                     •      button 22 —

                     •      button 23 —

                     •      button 24 —

                     •      button 25 —

                     •      button 26 —

                     •      button 27 —

                     •      button 28 —

                     •      button 29 —

                     •      button 30 —

                     •      button 31 —


5662   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5662 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5663 ordinal=5663 -->
## Functions

Functions


         •      button 32 —


   •       direction info —

    direction info contains numeric values for up to four points of view.

         •     pov 1 —

         •     pov 2 —

         •     pov 3 —

         •     pov 4 —


   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Input Device Control\
   Monitoring Keyboard and Mouse Activity.vi

keyboardAcquirekeyboardAcquire VIVI

Returns data about the device connected to the computer. Wire data to the device ID
input to determine the polymorphic instance to use or manually select the instance.

(Windows) You must have DirectX 8.0 or later to use this VI.


                                                    © National Instruments 5663

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5663 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5664 ordinal=5664 -->
## Functions

Functions

      Inputs/Outputs

               •      device ID —

            device ID identifies which device you acquired data from.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      device ID —

            device ID identifies which device to acquire data from.

               •      keys pressed —

           keys pressed indicates which keys were pressed when the VI ran. This parameter returns values
            associated only with US keyboards.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Connectivity\Input Device Control\
        Monitoring Keyboard and Mouse Activity.vi

      mouseAcquiremouseAcquire VIVI

       Returns data about the device connected to the computer. Wire data to the device ID
       input to determine the polymorphic instance to use or manually select the instance.

      (Windows) You must have DirectX 8.0 or later to use this VI.


5664   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5664 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5665 ordinal=5665 -->
## Functions

Functions


Inputs/Outputs

   •      device ID —

    device ID identifies which device you acquired data from.

   •      key mode —

    key mode determines the key mode to use.

    0 Relative—Defines the mouse coordinates as relative to the last time you called the VI.
     Absolute—Defines the mouse coordinates (axis info) as absolute coordinates relative to the    1     upper left hand corner of the screen.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      device ID —

    device ID identifies which device to acquire data from.

   •       axis info —

     axis info contains the numeric value for axes.

         •      Horizontal —

        Horizontal is the numeric value of the horizontal axis.

         •       Vertical —

         Vertical is the numeric value of the vertical axis.

         •       Scrolling —

         Scrolling is the numeric value of the scrolling axis if the mouse supports it.


                                                    © National Instruments 5665

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5665 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5666 ordinal=5666 -->
## Functions

Functions

               •      button info —

           button info contains Boolean values for up to four buttons. A TRUE value indicates that the
            button was pressed when the VI ran.

                     •      button 1 —

                     •      button 2 —

                     •      button 3 —

                     •      button 4 —


               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Connectivity\Input Device Control\
        Monitoring Keyboard and Mouse Activity.vi

     CloseClose InputInput DeviceDevice

       Closes the device you specify in device ID. Wire data to the device ID input to
      determine the polymorphic instance to use or manually select the instance.

      (Windows) You must have DirectX 8.0 or later to use this VI.


            • closeJoystick VI
            • closeKeyboard VI
            • closeMouse VI


5666   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5666 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5667 ordinal=5667 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Input Device Control\
   Monitoring Keyboard and Mouse Activity.vi

closeJoystickcloseJoystick VIVI

Closes the device you specify in device ID. Wire data to the device ID input to
determine the polymorphic instance to use or manually select the instance.

(Windows) You must have DirectX 8.0 or later to use this VI.


Inputs/Outputs

   •      device ID —

    device ID specifies which device reference to close.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Input Device Control\
   Monitoring Keyboard and Mouse Activity.vi


                                                    © National Instruments 5667

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5667 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5668 ordinal=5668 -->
## Functions

Functions

      closeKeyboardcloseKeyboard VIVI

       Closes the device you specify in device ID. Wire data to the device ID input to
      determine the polymorphic instance to use or manually select the instance.

      (Windows) You must have DirectX 8.0 or later to use this VI.


      Inputs/Outputs

               •      device ID —

            device ID specifies which device reference to close.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Connectivity\Input Device Control\
        Monitoring Keyboard and Mouse Activity.vi

      closeMousecloseMouse VIVI

       Closes the device you specify in device ID. Wire data to the device ID input to
      determine the polymorphic instance to use or manually select the instance.

      (Windows) You must have DirectX 8.0 or later to use this VI.


5668   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5668 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5669 ordinal=5669 -->
## Functions

Functions


Inputs/Outputs

   •      device ID —

    device ID specifies which device reference to close.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Input Device Control\
   Monitoring Keyboard and Mouse Activity.vi

ActiveXActiveX

Use the ActiveX functions to pass properties and methods to and from other ActiveX-
enabled applications, such as Microsoft Excel.

Some applications provide ActiveX data in the form of a self-describing data type
called a variant. To review or process the data in LabVIEW, you must convert it to a
corresponding LabVIEW data type using the Variant To Data function.

      Note ActiveX error codes are documented by Microsoft in winerror.h.


                                                    © National Instruments 5669

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5669 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5670 ordinal=5670 -->
## Functions

Functions


         Palette                     Description
        Object

        Automation
       Open       Returns an automation refnum, which points to a specific ActiveX object.
         Function

         Close                     Closes a refnum associated with an open VI, VI object, an open application instance,         Reference                     or a .NET, ActiveX or Python object.         Function

        To Variant   Converts any LabVIEW data to variant data. You also can use this function to convert
         Function    ActiveX data to variant data.

         Variant To                     Converts variant data to a LabVIEW data type so LabVIEW can display or process the        Data                       data. You also can use this function to convert variant data to ActiveX data.
         Function

         Property
       Node       Gets (reads) and/or sets (writes) properties of a reference.
          (ActiveX)

        Invoke
                     Invokes a method or action on a reference. Most methods have associated       Node                     parameters.          (ActiveX)

         Register     Registers a VI to be called when an event occurs. You use this function to register and
        Event       handle .NET and ActiveX events. LabVIEW uses the type of the input reference wired to
         Callback    each item to determine the events for which you can register.

         Unregister
         For Events   Unregisters all events associated with an event registration refnum.
         Function

                     Maintains a static reference to a VI. You can configure the Static VI Reference function
          Static VI     to output a generic or strictly typed VI reference. After you place the Static VI
         Reference   Reference function on a block diagram, double-click the function to display a file
                      dialog box where you can select a VI.

     AutomationAutomation OpenOpen FunctionFunction

       Returns an automation refnum, which points to a specific ActiveX object.


5670   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5670 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5671 ordinal=5671 -->
## Functions

Functions


Inputs/Outputs

   •      Automation Refnum —

    Automation Refnum provides the object type for the Automation Refnum output.

   •     machine name ("": open local reference) —

    machine name indicates on which machine the VI should open the Automation Refnum. If no
    machine name is given, the object is opened on the local machine.

   •     open new instance (false) —

       If open new instance is TRUE, LabVIEW creates a new instance of the Automation Refnum. If
    FALSE (default), LabVIEW tries to connect to an instance of the refnum that is already open. If the
    attempt is unsuccessful, LabVIEW opens a new instance.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      Automation Refnum —

    Automation Refnum is the refnum associated with an ActiveX object.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Select the class of the object by right-clicking the function and selecting Select ActiveX
Class from the shortcut menu. After you open the refnum, you can pass it to other
ActiveX functions. Select only creatable classes as inputs to this function. If you wire
machine name, the object opens on the remote machine. Otherwise, the object opens
on the local machine.


                                                    © National Instruments 5671

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5671 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5672 ordinal=5672 -->
## Functions

Functions

           Note Distributed COM must be properly installed and configured to open a
             remote reference.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Connectivity\Excel\Excel - ActiveX Event
        Callback.vi

     CloseClose ReferenceReference FunctionFunction

       Closes a refnum associated with an open VI, VI object, an open application instance, or
      a .NET, ActiveX or Python object.


      Inputs/Outputs

               •      reference —

            reference is the refnum associated with an open VI, VI object, an open application instance, or a
           .NET or ActiveX object. reference also accepts 1D arrays of references.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When you create a refnum to a VI, LabVIEW loads the VI into memory. The VI stays in
     memory until you close the refnum and until the VI meets the following conditions:

5672   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5672 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5673 ordinal=5673 -->
## Functions

Functions

  • There are no other open references to the referenced VI.
  • The front panel of the VI is not open.
  • The VI is not a subVI of another VI in memory.
  • The VI is not a member of an open project library.

ToTo VariantVariant FunctionFunction

Converts any LabVIEW data to variant data. You also can use this function to convert
ActiveX data to variant data.


Inputs/Outputs

   •      anything —

    anything is any LabVIEW data you want to convert. This parameter is polymorphic.

   •       variant —

    variant is the resulting variant data.


If you use the To Variant and Variant to Data functions with LabVIEW classes consider
the following caveat.

Variants do not recognize inheritance hierarchies. For example, if you have child data
traveling on a parent class wire and you then wire the parent wire to a To Variant
function, the variant recognizes only the parent data type. If you wire a child data type
to the Variant to Data function to extract the child data, LabVIEW returns an error. You
must wire the parent to the Variant to Data function. Then use the To More Specific
function to retrieve the child class data.

VariantVariant ToTo DataData FunctionFunction

Converts variant data to a LabVIEW data type so LabVIEW can display or process the
data. You also can use this function to convert variant data to ActiveX data.


                                                    © National Instruments 5673

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5673 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5674 ordinal=5674 -->
## Functions

Functions


      Inputs/Outputs

               •      type —

           type specifies the LabVIEW data type of the data stored in variant.

                    If the data is an integer, you can coerce the data to another numeric representation, such as an
             extended-precision, floating-point number.
               •       variant —

             variant is the variant data you want to convert to the LabVIEW data type specified in type.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      data —

           data is the variant changed to the data type specified by type. If variant could not be converted
             to the data type specified, this data returns the default value for the data type.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Using Variant to Data with ActiveX References

       This function also serves the same purpose as the QueryInterface method of ActiveX.
      To use the Variant to Data function to switch between interfaces of an ActiveX object,
         first convert the automation refnum for the ActiveX object to a variant by using the To
       Variant function. Wire the variant version of the refnum to the variant input of the
       Variant to Data function. Then create another automation refnum and select the
       desired interface as the ActiveX class for the refnum. Wire this new automation refnum
       to the type input of the Variant to Data function. LabVIEW associates the specified
        interface with the automation refnum returned by data.


5674   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5674 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5675 ordinal=5675 -->
## Functions

Functions

Using Variant Conversion Functions with LabVIEW Classes

If you use the To Variant and Variant to Data functions with LabVIEW classes, note that
variants do not recognize inheritance hierarchies. For example, if you have child data
traveling on a parent class wire and you then wire the parent wire to a To Variant
function, the variant recognizes only the parent data type. If you wire a child data type
to the Variant to Data function to extract the child data, LabVIEW returns an error. You
must wire the parent to the Variant to Data function. Then use the To More Specific
function to retrieve the child class data.

PropertyProperty NodeNode (ActiveX)(ActiveX)

Gets (reads) and/or sets (writes) properties of a reference.

The Property Node (ActiveX) is preconfigured to access ActiveX properties. The node
operates in the same way as a standard Property Node.


Inputs/Outputs

   •      reference —
    reference is the refnum associated with the ActiveX object for which you want to set or get
     properties.
   •       error in (no error) —
    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.
   •      reference out —
    reference out returns reference unchanged.
   •       error out —
    error out contains error information. This output provides standard error out functionality.
   •      Property —
    property 1..n are examples of properties you want to get (read).

If the property you want to write is variant, you can wire LabVIEW data and it
automatically converts to variant data indicated by a coercion dot. ActiveX does not
support 64-bit integer data types. If you wire 64-bit integer data to a variant parameter

                                                    © National Instruments 5675

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5675 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5676 ordinal=5676 -->
## Functions

Functions

       of an ActiveX Property Node, LabVIEW converts the data to a double-precision,
       floating-point number. If the property is variant, use the Variant To Data function to
       convert to LabVIEW data, if needed. If you right-click the Property Node and select
       Select Class»ActiveX»Browse from the shortcut menu, LabVIEW displays the Select
       Object From Type Library dialog box.

     On the front panel or block diagram, right-click an ActiveX object, select
       Create»Property Node, and select a property from the shortcut menu to set a property
        for the object. You also can select ActiveX-specific properties for an ActiveX object. On
       the block diagram, right-click an ActiveX object, select Create»Property Node, and
        select an ActiveX-specific property from the shortcut menu.

     InvokeInvoke NodeNode (ActiveX)(ActiveX)

       Invokes a method or action on a reference. Most methods have associated parameters.

      The node operates in the same way as a standard Invoke Node.


      Inputs/Outputs

               •      reference —
            reference is the refnum associated with the ActiveX object on which you want to invoke a
          method or perform an action.
               •       error in (no error) —
             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.
               •     Method —
            input 1..n are example input parameters of a method.
               •      reference out —
            reference out returns reference unchanged.
               •       error out —
             error out contains error information. This output provides standard error out functionality.
               •     Method —
            return value is an example return value of a method.
               •    param—

5676   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5676 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5677 ordinal=5677 -->
## Functions

Functions


    output 1..n are example output parameters of a method.


ActiveX does not support 64-bit integer data types. If you wire 64-bit integer data to a
variant parameter of an ActiveX Invoke Node, LabVIEW converts the data to a double-
precision, floating-point number. If you right-click the Invoke Node and select Select
Class»ActiveX»Browse from the shortcut menu, LabVIEW displays the Select Object
From Type Library dialog box.

On the front panel or block diagram, right-click an ActiveX object, select
Create»Invoke Node, and select a method from the shortcut menu to invoke a method
for the object. You also can invoke ActiveX-specific methods for an ActiveX object. On
the block diagram, right-click an ActiveX object, select Create»Invoke Node, and select
an ActiveX-specific method from the shortcut menu.

RegisterRegister EventEvent CallbackCallback

Registers a VI to be called when an event occurs. You use this function to register and
handle .NET and ActiveX events. LabVIEW uses the type of the input reference wired to
each item to determine the events for which you can register.

You can resize the function to register multiple event callbacks at once for the same
.NET or ActiveX object or for a different object.

      Note If you wire Register Event Callback functions together by wiring the
       event callback ref out output of one function to the event callback ref input
        of another function, the last function in the series overwrites all the previous
        Register Event Callback functions.


                                                    © National Instruments 5677

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5677 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5678 ordinal=5678 -->
## Functions

Functions

      Inputs/Outputs

               •      event callback refnum —

           event callback ref accepts a reference to an existing event callback registration.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      event source —

           event source ref accepts a .NET object or an ActiveX automation reference. Click the down arrow
            next to this input and select the type of event you want to generate, such as Mouse Down or
           Double Click. References must be to local objects. You cannot wire a reference to a remote
             object.

               •       VI Ref —

              vi reference is a strict VI reference to the callback VI.

              vi reference must match exactly the data from the registered event and the callback VI must be
             reentrant.
               •      User Parameter —

            user parameter contains data that you want to pass to the callback VI when the .NET or ActiveX
             object generates the event.

            For example, you can wire a string that includes a text message to the user parameter input to
                tell a user for which control the event occurred. If you want to use this parameter, you must wire
                   it before you create the callback VI. You can wire any LabVIEW data type, including a cluster, to
              this parameter.
               •      event callback refnum —

           event callback ref out returns a reference to a new or existing callback registration.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      Use this function to register .NET and ActiveX events only. To unregister an event for
      .NET or ActiveX, wire the event callback ref out output to the Unregister For Events


5678   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5678 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5679 ordinal=5679 -->
## Functions

Functions

function.

Use the Event structure or the Register For Events function to register and handle non-
.NET or non-ActiveX events dynamically.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Excel\Excel - ActiveX Event
   Callback.vi
  • labview\examples\Connectivity\ActiveX\ActiveX Event
   Callback.vi
  • labview\examples\Connectivity\Dot NET\Passing Data to a
   .NET Event Callback.vi

UnregisterUnregister ForFor EventsEvents FunctionFunction

Unregisters all events associated with an event registration refnum.

Event structures that use this event registration refnum no longer receive any dynamic
events. National Instruments recommends that you unregister for events when you no
longer need to handle them. If you do not unregister for events, LabVIEW continues to
generate and queue the events as long as the VI runs, even if no Event structure is
waiting to handle them, which consumes memory and can hang the VI if you enable
front panel locking for the events.


Inputs/Outputs

   •      event registration refnum —

    event registration refnum is a reference to an existing event registration a Register For Events
    function created.

   •       error in (no error) —


                                                    © National Instruments 5679

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5679 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5680 ordinal=5680 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      StaticStatic VIVI ReferenceReference

       Maintains a static reference to a VI. You can configure the Static VI Reference function
       to output a generic or strictly typed VI reference. After you place the Static VI Reference
       function on a block diagram, double-click the function to display a file dialog box
      where you can select a VI.


      Inputs/Outputs

               •    —

              vi reference is the refnum associated with the configured VI.

                    If the VI is not valid, vi reference contains Not A Refnum.

      The Static VI Reference function acts as a subVI and appears in the VI hierarchy of the
       top-level VI. By default, the output is a generic VI reference.

      You can change the output of this function to a strictly typed VI reference. Right-click
       the function and select Strictly Typed VI Reference from the shortcut menu to change
       the output. A red star in the upper left corner of the function icon indicates the
       reference is strictly typed. The strictly typed VI reference identifies the connector pane
       of the VI you are calling. You can create a strictly typed VI reference only from a VI or VI
       template, not from a polymorphic VI or other non-VI file such as a global variable or
        control.

5680   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5680 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5681 ordinal=5681 -->
## Functions

Functions

Use a strictly typed VI reference if you want to call the referenced VI with the Call By
Reference node or the Start Asynchronous Call node. When you create a strictly typed
VI reference, you cannot wire vi reference to the Run VI method. You cannot use the
Run VI method to run a VI that is already reserved for execution by another VI. A strictly
typed static VI reference also reserves any subVIs when a top-level VI is reserved, thus
making it ineligible for the Run VI method. Refer to the Run VI method for more
information.

LabVIEW loads the referenced VI into memory when you load the top-level VI. When
the Static VI Reference function outputs a strictly typed VI reference, LabVIEW reserves
the referenced VI as long as the top-level VI is running. LabVIEW closes this reference
when the top-level VI is no longer in memory. You do not have to explicitly close the
reference this function returns.

      Note LabVIEW does not check whether the referenced VI can compile. If the
        referenced VI is broken, LabVIEW does not recognize that it is broken until
       you run the top-level VI. If you execute an Open VI Reference function that
        references the broken VI, you receive an error.

            If you want LabVIEW to check for a broken referenced VI before you run the
        top-level VI, use the referenced VI directly in the top-level VI instead of using a
         Static VI Reference function by clicking the Select a VI icon or text on the
       Functions palette and navigating to the VI you want to add to the block
       diagram.

WindowsWindows RegistryRegistry AccessAccess VIsVIs

Use the Windows Registry Access VIs to create, open, query, enumerate, close, and
delete Windows registry keys. You also can enumerate, read, write, and delete the
value of Windows registry keys.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.

The VIs on this palette can return Windows registry access error codes.

                                                    © National Instruments 5681

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5681 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5682 ordinal=5682 -->
## Functions

Functions


         Palette                  Description        Object

       Open
         Registry  Opens a reference to a key or subkey in the Windows registry.
        Key

         Create
         Registry  Creates a key in the Windows registry or opens it, if it already exists.
        Key

        Query
         Registry  Retrieves information about keys.
        Key Info

      Enum
         Registry  Enumerates subkeys of the specified key or subkey.
        Keys

         Close
         Registry  Closes a key in the Windows registry.
        Key

         Delete
         Registry  Deletes the specified key or subkey.
        Key

      Enum                Enumerates the values for the specified key or subkey. If retrieve data? is TRUE, the VI         Registry                   returns DWORD data and String/Binary data in addition to values and simple data         Values
                   types.
        Simple


       Read    Reads data and the simplified data type from a registry value. If the key or value does not
         Registry  exist or an unrecoverable error occurs, the VI returns the default data. Wire data to the
         Value    default data input to determine the polymorphic instance to use or manually select the
        Simple   instance.

         Write
         Registry  Writes data to the registry value under the key specified by refnum. Wire data to the
         Value    String/Binary data input to determine the polymorphic instance to use or manually
        Simple

5682   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5682 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5683 ordinal=5683 -->
## Functions

Functions


 Palette          Description
 Object

           select the instance.

 Delete
 Registry  Deletes the specified value for the specified key.
 Value

OpenOpen RegistryRegistry KeyKey

Opens a reference to a key or subkey in the Windows registry.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


Inputs/Outputs

   •     machine (local) —

    machine is the name of the networked machine.

    The default is the local machine.

   •      root key (HKEY_LOCAL_MACHINE) —

    root key is the Windows registry root key.

    0  HKEY_CLASSES_ROOT
    1  HKEY_CURRENT_USER
    2  HKEY_LOCAL_MACHINE


                                                    © National Instruments 5683

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5683 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5684 ordinal=5684 -->
## Functions

Functions


           3  HKEY_USERS
           4  HKEY_PERFORMANCE_DATA
           5  HKEY_CURRENT_CONFIG
           6  HKEY_DYN_DATA

               •      subkey —

           subkey is the name of a subkey of root key. A beginning backslash character \ might cause an
               error.

               •       security access mask (KEY_READ | KEY_WRITE) —

             security access mask is the access rights to assign the key.

           0  KEY_QUERY_VALUE
           1  KEY_SET_VALUE
           2  KEY_CREATE_SUB_KEY
           3  KEY_ENUMERATE_SUB_KEYS
           4  KEY_NOTIFY
           5  KEY_CREATE_LINK
           6  KEY_READ
           7  KEY_WRITE
           8  KEY_ALL_ACCESS
           9  KEY_READ | KEY_WRITE

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       registry view —

             registry view specifies whether to open a 32-bit key or a 64-bit key on a 64-bit operating system.

              Default (default)—LabVIEW selects the type of key based on the version of LabVIEW that is
           0
                installed. For example, if LabVIEW (64-bit) is installed, LabVIEW opens a 64-bit key.
           8 KEY_WOW64_32KEY—Opens a 32-bit key.
           9 KEY_WOW64_64KEY—Opens a 64-bit key.

               •     refnum out —


5684   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5684 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5685 ordinal=5685 -->
## Functions

Functions


    refnum out is a handle to the open key.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi

CreateCreate RegistryRegistry KeyKey

Creates a key in the Windows registry or opens it, if it already exists.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


Inputs/Outputs

   •     machine (local) —

    machine is the name of the networked machine.

    The default is the local machine.

   •      options —


                                                    © National Instruments 5685

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5685 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5686 ordinal=5686 -->
## Functions

Functions


            options is special options for the key.

           0  REG_OPTION_NON_VOLATILE
           1  REG_OPTION_VOLATILE
           2  REG_OPTION_BACKUP_RESTORE

               •      root key (HKEY_LOCAL_MACHINE) —

            root key is the Windows registry root key.

           0  HKEY_CLASSES_ROOT
           1  HKEY_CURRENT_USER
           2  HKEY_LOCAL_MACHINE
           3  HKEY_USERS
           4  HKEY_PERFORMANCE_DATA
           5  HKEY_CURRENT_CONFIG
           6  HKEY_DYN_DATA

               •      subkey —

           subkey is the name of a subkey of root key. A beginning backslash character \ might cause an
               error.

               •       security access mask (KEY_READ | KEY_WRITE) —

             security access mask is the access rights to assign the key.

           0  KEY_QUERY_VALUE
           1  KEY_SET_VALUE
           2  KEY_CREATE_SUB_KEY
           3  KEY_ENUMERATE_SUB_KEYS
           4  KEY_NOTIFY
           5  KEY_CREATE_LINK
           6  KEY_READ
           7  KEY_WRITE
           8  KEY_ALL_ACCESS
           9  KEY_READ | KEY_WRITE

               •       error in (no error) —


5686   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5686 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5687 ordinal=5687 -->
## Functions

Functions


    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       class —

     class specifies the class (object type) of the key.

   •       registry view —

     registry view specifies whether to create a 32-bit key or a 64-bit key on a 64-bit operating
    system.

      Default (default)—LabVIEW selects the type of key based on the version of LabVIEW that is    0       installed. For example, if LabVIEW (64-bit) is installed, LabVIEW creates a 64-bit key.
    8 KEY_WOW64_32KEY—Creates a 32-bit key.
    9 KEY_WOW64_64KEY—Creates a 64-bit key.

   •     refnum out —

    refnum out is a handle to the open key.

   •      action taken —

    action taken is the action taken by the VI.

    0  Unknown
    1  REG_CREATED_NEW_KEY
    2  REG_OPENED_EXISTING_KEY

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi


                                                    © National Instruments 5687

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5687 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5688 ordinal=5688 -->
## Functions

Functions

     QueryQuery RegistryRegistry KeyKey InfoInfo

       Retrieves information about keys.

           Caution Incorrectly modifying the registry can damage Windows or prevent
            you from starting Windows.


      Inputs/Outputs

               •     refnum —

          refnum is a handle to the open key.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is a handle to the open key.

               •       class —

             class specifies the class (object type) of the key.

               •      value info —

            value info is the set of parameters describing the set of values and data.

                     •     numValues —

              numValues is the number of values under the key specified by hKey.

                     •     maxValueNameLen —


5688   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5688 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5689 ordinal=5689 -->
## Functions

Functions


       maxValueNameLen is the length of the longest value name under the key specified by hKey.

         •      maxValueDataLen —

       maxValueDataLen is the length of the longest datum under the key specified by hKey.


   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      subkey info —

    subkey info is the set of parameters describing the subkeys.

         •     numSubKeys —

       numSubKeys is the number of subkeys under the key specified by hKey.

         •     maxSubKeyLen —

       maxSubKeyLen is the length of the longest subkey name under the key specified by hKey.

         •     maxSubKeyClassLen —

       maxSubKeyClassLen is the length of the longest class name under the key specified by
        hKey.


EnumEnum RegistryRegistry KeysKeys

Enumerates subkeys of the specified key or subkey.

Use the Enum Registry Keys VI with the Query Registry Key Info VI.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


                                                    © National Instruments 5689

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5689 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5690 ordinal=5690 -->
## Functions

Functions


      Inputs/Outputs

               •     refnum —

          refnum is a handle to the open key.

               •      subkey info —

           subkey info is a is a set of parameters describing the subkey associated with refnum.

                     •     numSubKeys —

             numSubKeys is the number of subkeys under the key specified by hKey.

                     •     maxSubKeyLen —

             maxSubKeyLen is the length of the longest subkey name under the key specified by hKey.

                     •     maxSubKeyClassLen —

              maxSubKeyClassLen is the length of the longest class name under the key specified by
                hKey.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is a handle to the open key.

               •      subkeys —

           subkeys is an array of the names of all subkeys of the specified key.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5690   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5690 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5691 ordinal=5691 -->
## Functions

Functions

CloseClose RegistryRegistry KeyKey

Closes a key in the Windows registry.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


Inputs/Outputs

   •     refnum —

    refnum is a handle to the open key.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi

DeleteDelete RegistryRegistry KeyKey

Deletes the specified key or subkey.


                                                    © National Instruments 5691

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5691 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5692 ordinal=5692 -->
## Functions

Functions

           Caution Incorrectly modifying the registry can damage Windows or prevent
            you from starting Windows.


      Inputs/Outputs

               •     refnum —

          refnum is a handle to the open key.

               •      subkey —

           subkey is the name of a subkey of root key. A beginning backslash character \ might cause an
               error.

               •       registry view —

             registry view specifies whether to delete a 32-bit key or a 64-bit key on a 64-bit operating
            system.

              Default (default)—LabVIEW selects the type of key based on the version of LabVIEW that is           0                installed. For example, if LabVIEW (64-bit) is installed, LabVIEW deletes a 64-bit key.
           8 KEY_WOW64_32KEY—Deletes a 32-bit key.
           9 KEY_WOW64_64KEY—Deletes a 64-bit key.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is a handle to the open key.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


5692   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5692 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5693 ordinal=5693 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi

EnumEnum RegistryRegistry ValuesValues SimpleSimple

Enumerates the values for the specified key or subkey. If retrieve data? is TRUE, the VI
returns DWORD data and String/Binary data in addition to values and simple data
types.

Use this VI with the Query Registry Key Info VI.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


Inputs/Outputs

   •     refnum —

    refnum is a handle to the open key.

   •       retrieve data? (F) —

     retrieve data? retrieves data and data types, if TRUE.

   •      value info —

    value info is the set of parameters describing the set of values and data.


                                                    © National Instruments 5693

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5693 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5694 ordinal=5694 -->
## Functions

Functions


                     •     numValues —

              numValues is the number of values under the key specified by hKey.

                     •     maxValueNameLen —

             maxValueNameLen is the length of the longest value name under the key specified by hKey.

                     •      maxValueDataLen —

              maxValueDataLen is the length of the longest datum under the key specified by hKey.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •    DWORD data —

        DWORD data is an array of data of Windows registry type DWORD.

               •     refnum out —

          refnum out is a handle to the open key.

               •      values —

            values is an array of value names.

               •      simple data types —

           simple data types is an array of simplified Windows registry data types.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      String/Binary data —

            String/Binary data is an array of data of Windows registry type 'String' or 'Binary'.


5694   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5694 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5695 ordinal=5695 -->
## Functions

Functions

ReadRead RegistryRegistry ValueValue SimpleSimple

Reads data and the simplified data type from a registry value. If the key or value does
not exist or an unrecoverable error occurs, the VI returns the default data. Wire data to
the default data input to determine the polymorphic instance to use or manually
select the instance.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


  • Read Registry Value Simple STR
  • Read Registry Value Simple U32 VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi

ReadRead RegistryRegistry ValueValue SimpleSimple STRSTR

Reads data and the simplified data type from a registry value. If the key or value does
not exist or an unrecoverable error occurs, the VI returns the default data. Wire data to
the default data input to determine the polymorphic instance to use or manually
select the instance.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


                                                    © National Instruments 5695

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5695 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5696 ordinal=5696 -->
## Functions

Functions


      Inputs/Outputs

               •     refnum —

          refnum is a handle to the open key.

               •      value —

            value is the name of the registry value.

               •       default data —

             default data is the data to return if value is not found or if an unrecoverable error occurs.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is the reference number of the configuration data.

               •      simple data type —

           simple data type is the simplified Windows registry type.

               •      String/Binary data —

            String/Binary data is the data of Windows registry type String or Binary.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.


5696   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5696 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5697 ordinal=5697 -->
## Functions

Functions

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi

ReadRead RegistryRegistry ValueValue SimpleSimple U32U32 VIVI

Reads data and the simplified data type from a registry value. If the key or value does
not exist or an unrecoverable error occurs, the VI returns the default data. Wire data to
the default data input to determine the polymorphic instance to use or manually
select the instance.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


Inputs/Outputs

   •     refnum —

    refnum is a handle to the open key.

   •      value —

    value is the name of the registry value.

   •       default data —

    default data is the data to return if value is not found or if an unrecoverable error occurs.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is the reference number of the configuration data.


                                                    © National Instruments 5697

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5697 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5698 ordinal=5698 -->
## Functions

Functions

               •      simple data type —

           simple data type is the simplified Windows registry type.

               •    DWORD data —

        DWORD data is the data of Windows registry type DWORD.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Connectivity\Windows Registry Access\
        Windows Registry Manipulation.vi

      WriteWrite RegistryRegistry ValueValue SimpleSimple

       Writes data to the registry value under the key specified by refnum. Wire data to the
       String/Binary data input to determine the polymorphic instance to use or manually
        select the instance.

           Caution Incorrectly modifying the registry can damage Windows or prevent
            you from starting Windows.


            • Write Registry Value Simple STR
            • Write Registry Value Simple U32 VI

     Examples

       Refer to the following example files included with LabVIEW.


5698   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5698 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5699 ordinal=5699 -->
## Functions

Functions

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi

WriteWrite RegistryRegistry ValueValue SimpleSimple STRSTR

Writes data to the registry value under the key specified by refnum. Wire data to the
String/Binary data input to determine the polymorphic instance to use or manually
select the instance.

      Caution Incorrectly modifying the registry can damage Windows or prevent
       you from starting Windows.


Inputs/Outputs

   •      String/Binary data —

    String/Binary data is the data of Windows registry type String or Binary.

   •     refnum —

    refnum is a handle to the open key.

   •      value —

    value is the name of the registry value.

   •      simple data type —

    simple data type is the simplified Windows registry type.

    0             String
    1           Binary
    2        DWORD


                                                    © National Instruments 5699

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5699 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5700 ordinal=5700 -->
## Functions

Functions

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is a handle to the open key.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Connectivity\Windows Registry Access\
        Windows Registry Manipulation.vi

       WriteWrite RegistryRegistry ValueValue SimpleSimple U32U32 VIVI

       Writes data to the registry value under the key specified by refnum. Wire data to the
       String/Binary data input to determine the polymorphic instance to use or manually
        select the instance.

           Caution Incorrectly modifying the registry can damage Windows or prevent
            you from starting Windows.


      Inputs/Outputs

               •    DWORD data —


5700   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5700 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5701 ordinal=5701 -->
## Functions

Functions


   DWORD data is the data of Windows registry type DWORD.

   •     refnum —

    refnum is a handle to the open key.

   •      value —

    value is the name of the registry value.

   •      simple data type —

    simple data type is the simplified Windows registry type.

    0             String
    1           Binary
    2        DWORD

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •     refnum out —

    refnum out is a handle to the open key.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Connectivity\Windows Registry Access\
   Windows Registry Manipulation.vi


                                                    © National Instruments 5701

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5701 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5702 ordinal=5702 -->
## Functions

Functions

      DeleteDelete RegistryRegistry ValueValue

       Deletes the specified value for the specified key.

           Caution Incorrectly modifying the registry can damage Windows or prevent
            you from starting Windows.


      Inputs/Outputs

               •     refnum —

          refnum is a handle to the open key.

               •      value —

            value is the name of the registry value.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     refnum out —

          refnum out is a handle to the open key.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    PythonPython

      Use the Python functions to call Python code from LabVIEW.


5702   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5702 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5703 ordinal=5703 -->
## Functions

Functions

      Note NI recommends that you use supported versions of Python only,
       though unsupported versions might work with the LabVIEW Python
        functions. Visit ni.com/info and enter the Info Code python to learn more
       about the requirements for installing Python.


 Palette              Description Object

 Open            Opens a Python session with a specific version of Python. The Python session is Python              necessary for configuring multiple Python Nodes to run in a specific version of Session             Python and in the same process.
 Function

 Python                Calls a Python function directly.
 Node

 Close
 Python              Closes a Python session. Session
 Function

 Close              Closes a refnum associated with an open VI, VI object, an open application instance,
 Reference              or a .NET, ActiveX or Python object. Function

OpenOpen PythonPython SessionSession FunctionFunction

Opens a Python session with a specific version of Python. The Python session is
necessary for configuring multiple Python Nodes to run in a specific version of Python
and in the same process.


                                                    © National Instruments 5703

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5703 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5704 ordinal=5704 -->
## Functions

Functions

      Inputs/Outputs

               •      Python version —

           Python version specifies the version of Python in which the Python session runs. This function
            supports Python of versions 3.6 through 3.9 only.

           Although unsupported versions might work with the LabVIEW Python functions, NI recommends
            using supported versions of Python only.
               •      Python path —

           python path specifies the directory where Python is installed. The default is the directory of the
             version of Python determined by python version.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      session out —

            session out returns a reference to the Python session.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     PythonPython NodeNode

        Calls a Python function directly.

      The Python Node is expandable and shows data types for the wired inputs and
       outputs. You can configure the Python Node to specify the Python session, module
       path, and function name.

      The Python Node is not supported on real-time or FPGA targets.


5704   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5704 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5705 ordinal=5705 -->
## Functions

Functions


Inputs/Outputs

   •      session in —

    session in specifies a reference to the Python session. One or more Python Nodes can run in a
     single Python session.

   •     module path —

   module path specifies the path to the Python module. The module contains the Python function
    to call.

   •      function name —

    function name specifies the name of the Python function to call.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      return type —

    return type specifies the data type of return value.

    You must wire the data type to return type to indicate the expected data type of return value. If
    the Python function does not return any value, leave return type unwired.
   •      input parameter —

    input parameter specifies the input parameters of the Python function.

    You can resize the Python Node to add more terminals. You pass a value to the Python function
    by wiring to the left terminal of a terminal pair. You read the value of a parameter after the
    function call by wiring from the right terminal of a terminal pair.
   •      session out —

    session out returns a reference to the Python session.


                                                    © National Instruments 5705

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5705 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5706 ordinal=5706 -->
## Functions

Functions

               •       error out —

             error out contains error information. This output provides standard error out functionality.

               •      return value —

            return value is the return value of the Python function.

               •    —


     Supported Data Types

      The Python Node supports a large number of data types. You can use this node to call
       the following data types:

            • Numerics
            • Arrays, including multi-dimensional arrays
            • Strings
            • Clusters
            • Booleans

      Calling Conventions

       This node converts integers, strings, and Booleans to the corresponding data types in
       Python, converts arrays to lists or NumPy arrays, and converts clusters to tuples.

      Marshaling Arrays to Lists or NumPy Arrays

      By default, the Python Node marshals arrays to lists. To marshal an array wired to
       input parameter to a NumPy array, right-click input parameter and select Marshal to
     NumPy Array from the shortcut menu.

           Note You can marshal only numeric arrays to NumPy arrays.

      Marshaling Clusters to Named Tuples

      By default, the Python Node marshals clusters to tuples. In Python, you can only
       reference items in a tuple by index and iterator. Python supports named tuples, which

5706   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5706 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5707 ordinal=5707 -->
## Functions

Functions

allow you to reference items by name as well. If you want to reference named tuple
items by name, you must marshal clusters to named tuples. To marshal a cluster wired
to an input parameter to a named tuple, right-click input parameter and select
Marshal to Namedtuple from the shortcut menu.

CloseClose PythonPython SessionSession FunctionFunction

Closes a Python session.


Inputs/Outputs

   •      session in —

    session in specifies a reference to the Python session. One or more Python Nodes can run in a
     single Python session.

   •       error in —

    error in describes error conditions that occur before this node runs. With the following
    exception, this input provides standard error in functionality.

    This node runs normally evenifan error occurred before this node runs.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CloseClose ReferenceReference FunctionFunction

Closes a refnum associated with an open VI, VI object, an open application instance, or
a .NET, ActiveX or Python object.


                                                    © National Instruments 5707

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5707 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5708 ordinal=5708 -->
## Functions

Functions

      Inputs/Outputs

               •      reference —

            reference is the refnum associated with an open VI, VI object, an open application instance, or a
           .NET or ActiveX object. reference also accepts 1D arrays of references.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. With the following
             exception, this input provides standard error in functionality.

             This node runs normally evenifan error occurred before this node runs.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


     When you create a refnum to a VI, LabVIEW loads the VI into memory. The VI stays in
     memory until you close the refnum and until the VI meets the following conditions:

            • There are no other open references to the referenced VI.
            • The front panel of the VI is not open.
            • The VI is not a subVI of another VI in memory.
            • The VI is not a member of an open project library.

    MATLAB(R)MATLAB(R)

      Use the MATLAB® functions to call MATLAB code from LabVIEW.


         Palette Object                     Description

       Open MATLAB Session Function    Opens a MATLAB(R) session.

          Call MATLAB Function                Calls the top level MATLAB(R) function in the source file.

         Close MATLAB Session Function     Closes a MATLAB(R) session.


5708   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5708 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5709 ordinal=5709 -->
## Functions

Functions

OpenOpen MATLABMATLAB SessionSession FunctionFunction

Opens a MATLAB(R) session.


Inputs/Outputs

   •      release name —

    release name specifies the release of MATLAB in which the MATLAB session runs. For example,
    R2021a. If no release is specified, the most recent installed release of MATLAB is used.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      session out —

    session out returns a reference to the MATLAB session.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

CallCall MATLABMATLAB FunctionFunction

Calls the top level MATLAB(R) function in the source file.

The Call MATLAB Function is expandable and shows data types for the wired inputs
and outputs. You can configure the Call MATLAB Function to specify the MATLAB
session, source path, and function name.

The Call MATLAB Function is not supported on real-time or FPGA targets.


                                                    © National Instruments 5709

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5709 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5710 ordinal=5710 -->
## Functions

Functions


      Inputs/Outputs

               •      session in —

            session in specifies a reference to the MATLAB session.

               •      source file path —

            source file path specifies the absolute path to the source .m file.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      return type —

            return type specifies the data type of return value. You must wire a constant or control
           matching the data type of the top level MATLAB function return type to return type. For
            example, if the MATLAB function returns an array of doubles, you must wire an array of doubles
            constant or control to return type. If the MATLAB function returns multiple values, wire a cluster
            with elements the correspond to the MATLAB function return values. The name and data types
          and order of the cluster elements must match the MATLAB function return values. For example, if
            the MATLAB function returns a numeric, a Boolean array, and a string, you must wire return type
             to a cluster containing controls or constants of numeric, Boolean array, and string data types in
             that order. Cluster element names must be unique and not empty. If the MATLAB function does
            not return any value, leave return type unwired.

               •      input parameter —

            input parameter specifies the input parameters of the MATLAB function. You must wire the
            inputs in the order that the function calls them. You can resize the MATLAB Node to add more
             terminals. You pass a value to the MATLAB function by wiring to the left terminal of a terminal
               pair. You read the value of a parameter after the function call by wiring from the right terminal of
           a terminal pair.

               •      session out —


5710   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5710 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5711 ordinal=5711 -->
## Functions

Functions


    session out returns a reference to the MATLAB session.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •      return value —

    return value is the return value of the MATLAB function. The data type of return value depends
    on return type.

   •    —


Supported Data Types

The Call MATLAB Function supports the following data types:

  • Numerics
  • Arrays, including multi-dimensional arrays.

        Note 1D arrays are converted to Row Vectors in MATLAB.

  • Strings
  • Clusters
  • Booleans

CloseClose MATLABMATLAB SessionSession FunctionFunction

Closes a MATLAB(R) session.


Inputs/Outputs

   •      session in —


                                                    © National Instruments 5711

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5711 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5712 ordinal=5712 -->
## Functions

Functions


            session in specifies a reference to the MATLAB session.

               •       error in —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

    ControlControl && SimulationSimulation

      Use the Control and Simulation VIs and Functions to design, analyze, simulate, and
      deploy dynamic system models.


         Palette                 Description        Object

               Use the PID VIs to implement Proportional-Integral-Derivative (PID) control applications.
               The first three VIs on the PID palette are different versions of the PID VI. These VIs can be        PID
               used interchangeably depending on the needs of the application. The other VIs on the PID
                  palette can be used with one of the PID VIs for additional functionality.


               Use the Fuzzy Logic VIs to design and control fuzzy systems. You also can use the Fuzzy
        Fuzzy
               System Designer to design fuzzy systems interactively. You can use fuzzy logic to
         Logic
               implement rule-based control for systems requiring control with multiple inputs.

     PIDPID

      Use the PID VIs to implement Proportional-Integral-Derivative (PID) control
       applications. The first three VIs on the PID palette are different versions of the PID VI.

5712   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5712 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5713 ordinal=5713 -->
## Functions

Functions

These VIs can be used interchangeably depending on the needs of the application. The
other VIs on the PID palette can be used with one of the PID VIs for additional
functionality.

PID is a common single-input/single-output control algorithm for many types of
control applications.


 Palette                Description
 Object

              Implements a PID controller using a PID algorithm for simple PID applications or
               high speed control applications that require an efficient algorithm. The PID
               algorithm features control output range limiting with integrator anti-windup and PID              bumpless controller output for PID gain changes. Use the DBL instance of this VI to
              implement a single control loop. Use the DBL Array instance to implement parallel
                multi-loop control.


              Implements a PID controller using a PID algorithm with advanced optional features.
             The advanced PID algorithm includes the features of the algorithm the PID VI uses,
               as well as manual mode control with bumpless manual-to-automatic transitions,
 PID Advanced                nonlinear integral action, two degree-of-freedom control, and error-squared
                 control. Use the DBL instance of this VI to implement a single control loop. Use the
            DBL Array instance to implement parallel multi-loop control.

 PID Advanced  Implements a PID controller using a PID algorithm with advanced optional features,
 Autotuning    and applies autotuning to the controller. You can use this VI in RT applications.

                  Directly controls and tunes a system. You can use this VI to improve performance of
 PID               not only temperature systems, but alsoother types of systems that contain dead Autotuning
                time. This VI uses internal model control to compensate for dead time and tune the (Temperature)
               system.


 PID
                Includes the Autotuning Wizard in addition to the basic PID algorithm. You can use
 Autotuning


                                                    © National Instruments 5713

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5713 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5714 ordinal=5714 -->
## Functions

Functions


         Palette                        Description
        Object

                           this VI instead of the PID VI, which implements a basic PID algorithm. Use the
                         additional inputs and output of this VI to set autotuning parameters, invoke the
                       Autotuning Wizard, and update the PID gains.


                         Selects a set of PID gains from a gain schedule for the control of processes that
        PID Gain       require different sets of gains for different regions of operation, such as highly
        Schedule      nonlinear processes. Use the DBL instance of this VI to implement a single control
                         loop. Use the DBL Array instance to implement parallel multi-loop control.


                       Converts a PID controller or controllers in Academic, Parallel, or Series form into
        PID Structure  the form (Academic) and PID gains units that the PID VIs expect. Wire data to the
        Conversion    proportional, integral, or derivative input to determine the polymorphic instance
                        to use, or manually select the instance.

                     Implements autotuning using the tuning method associated with the polymorphic
        PID            instance you select. This VI generates PID parameters based on the Stimulus signal
        Autotuning    and Response signal you specify. You can use this VI to generate initial parameters
        Design       when you do not have sufficient information about the system you want to tune.
                     You must manually select the polymorphic instance to use.

                        Controls the parameters of a PID controller based on the autotuning technique of
        PID Online     the polymorphic instance you select. You can use this VI in applications with other
        Autotuning    PID VIs, such as PID or PID Advanced, to construct and tune a PID controller. You
                    must manually select the polymorphic instance to use.

                     Implements a PID controller with a lead/lag function, which is generally used as a
                     dynamic compensator in feedforward control schemes. This VI uses a positional
        PID Lead-Lag   algorithm and is an approximation of a true exponential lead/lag. Use the DBL
                        instance of this VI to implement a single control loop. Use the DBL Array instance to
                     implement parallel multi-loop control.


        PID Setpoint   Generates setpoint values over time in a control loop for ramp and soak types of
          Profile         control applications.


5714   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5714 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5715 ordinal=5715 -->
## Functions

Functions


 Palette                Description
 Object

                Applies a fifth-order lowpass finite impulse response (FIR) filter to the input value.
                   Filter cut-off frequency is designed to be 1/10 of the sample frequency of the input PID Control                 value. Use this VI to filter measured values, such as the process variable, in control Input Filter
                 applications. Use the DBL instance of this VI to implement a single control loop. Use
               the DBL Array instance to implement parallel multi-loop control.


                Limits the rate of change of the controller output. Place this VI immediately after
 PID Output    the PID VI in your control application. Use the DBL instance of this VI to implement
 Rate Limiter   a single control loop. Use the DBL Array instance to implement parallel multi-loop
                 control.


               Converts an engineering-units input to a percent-of-range output based on the
 PID EGU to    minimum and maximum range settings. Use the DBL instance of this VI to
 Percentage    implement a single control loop. Use the DBL Array instance to implement parallel
                multi-loop control.


               Converts a percent-of-range input to an engineering-units output based on the
 PID         minimum and maximum range settings. The output is normally limited to the range
 Percentage to  [max...min]. Values outside of the range [max..min] are allowed when coerce
 EGU          output to range? is FALSE. Use the DBL instance of this VI to implement a single
                control loop. Use the DBL Array instance to implement parallel multi-loop control.


PIDPID

Implements a PID controller using a PID algorithm for simple PID applications or high
speed control applications that require an efficient algorithm. The PID algorithm
features control output range limiting with integrator anti-windup and bumpless
controller output for PID gain changes. Use the DBL instance of this VI to implement a
single control loop. Use the DBL Array instance to implement parallel multi-loop
control.


                                                    © National Instruments 5715

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5715 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5716 ordinal=5716 -->
## Functions

Functions


            • PID (DBL) VI
            • PID (DBL Array) VI
            • PID (Compatibility) VI

      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the process variable input determines the
       length of the output array. Other input arrays do not necessarily need to be the same
       length as the process variable input. This VI resizes other input arrays to the same
       length as the process variable input as follows:

            •  If the input array is longer than the process variable input, the input array is
          truncated to the length of the process variable input. Additional values in the array
          are not used.
            •  If the input array is shorter than the process variable input, the last value of the
          input array is repeated until the size matches that of the process variable input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\General PID Simulator.vi

      PIDPID (DBL)(DBL) VIVI

      Implements a PID controller using a PID algorithm for simple PID applications or high
      speed control applications that require an efficient algorithm. The PID algorithm
       features control output range limiting with integrator anti-windup and bumpless
       controller output for PID gain changes. Use the DBL instance of this VI to implement a
       single control loop. Use the DBL Array instance to implement parallel multi-loop
        control.


5716   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5716 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5717 ordinal=5717 -->
## Functions

Functions


Inputs/Outputs

   •      output range —

    output range specifies the range to which to coerce the control output. The default range is –100
    to 100, which corresponds to values specified in terms of percentage of full scale.

    You can change this range to something that is appropriate for your control system. For example,
    you can relate engineering units to engineering units instead of percentage to percentage. This
     VI implements integrator anti-windup when the controller output is saturated at the specified
   minimum or maximum values.

         •      output high —

        output high specifies the maximum value of the controller output. The default is 100.

         •      output low —

        output low specifies the minimum value of the controller output. The default is –100.


   •      setpoint —

    setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

   •      process variable —

    process variable specifies the measured value of the process variable being controlled. This
    value is equal to the feedback value of the feedback control loop.

   •      PID gains —

    PID gains specifies the proportional gain, integral time, and derivative time parameters of the
     controller.

         •      proportional gain (Kc) —


                                                    © National Instruments 5717

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5717 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5718 ordinal=5718 -->
## Functions

Functions


                proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

                  In the equation that defines the PID controller, KC represents the proportional gain.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


               •      dt (s) —

            dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
           than or equal to zero, this VI calculates the time since it was last called using an internal timer
            with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
                -1.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
               error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
             control loop without restarting the entire application. The default is FALSE.

               •      output —

           output returns the control output of the PID algorithm that is applied to the controlled process.
                    If this VI receives an invalid input, output returns NaN.

               •      dt out (s) —

            dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
            or the computed interval if you set dt (s) to –1.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the process variable input determines the
       length of the output array. Other input arrays do not necessarily need to be the same
       length as the process variable input. This VI resizes other input arrays to the same
       length as the process variable input as follows:

5718   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5718 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5719 ordinal=5719 -->
## Functions

Functions

  •  If the input array is longer than the process variable input, the input array is
    truncated to the length of the process variable input. Additional values in the array
    are not used.
  •  If the input array is shorter than the process variable input, the last value of the
    input array is repeated until the size matches that of the process variable input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\General PID Simulator.vi

PIDPID (DBL(DBL Array)Array) VIVI

Implements a PID controller using a PID algorithm for simple PID applications or high
speed control applications that require an efficient algorithm. The PID algorithm
features control output range limiting with integrator anti-windup and bumpless
controller output for PID gain changes. Use the DBL instance of this VI to implement a
single control loop. Use the DBL Array instance to implement parallel multi-loop
control.


Inputs/Outputs

   •      output range —

    output range specifies the range to which to coerce the control output. The default range is -100
    to 100, which corresponds to values specified in terms of percentage of full scale.


                                                    © National Instruments 5719

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5719 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5720 ordinal=5720 -->
## Functions

Functions


           You can change this range to something that is appropriate for your control system. For example,
           you can relate engineering units to engineering units instead of percentage to percentage. This
              VI implements integrator anti-windup when the controller output is saturated at the specified
         minimum or maximum values.

           output range is an array of clusters of the following elements.

                     •      output high —

               output high specifies the maximum value of the controller output. The default is 100.

                     •      output low —

               output low specifies the minimum value of the controller output. The default is -100.


               •      setpoint —

            setpoint specifies the setpoint value, or desired value, of the process variable being controlled.
             This VI resizes the setpoint input array to match the size of the process variable input array.

               •      process variable —

            process variable specifies the measured value of the process variable being controlled. This
            value is equal to the feedback value of the feedback control loop.

               •      PID gains —

           PID gains is an array of clusters of the following elements.

                     •      proportional gain (Kc) —

                proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

                  In the equation that defines the PID controller, KC represents the proportional gain.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

                     •       derivative time (Td, min) —


5720   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5720 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5721 ordinal=5721 -->
## Functions

Functions


         derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


   •      dt (s) —

    dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
    than or equal to zero, this VI calculates the time since it was last called using an internal timer
    with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
     -1.

   •       reinitialize? (F) —

     reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
     error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
    control loop without restarting the entire application. The default is FALSE.

   •      output —

    output returns the control output of the PID algorithm that is applied to the controlled process.
    This VI determines the length of the output array from the size of the process variable input
     array.

   •      dt out (s) —

    dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
    or the computed interval if you set dt (s) to –1.


You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of the process variable input determines the
length of the output array. Other input arrays do not necessarily need to be the same
length as the process variable input. This VI resizes other input arrays to the same
length as the process variable input as follows:

  •  If the input array is longer than the process variable input, the input array is
    truncated to the length of the process variable input. Additional values in the array
    are not used.
  •  If the input array is shorter than the process variable input, the last value of the
    input array is repeated until the size matches that of the process variable input.


                                                    © National Instruments 5721

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5721 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5722 ordinal=5722 -->
## Functions

Functions

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\General PID Simulator.vi

      PIDPID (Compatibility)(Compatibility) VIVI

      Implements a PID controller using a PID algorithm for simple PID applications or high
      speed control applications that require an efficient algorithm. The PID algorithm
       features control output range limiting with integrator anti-windup and bumpless
       controller output for PID gain changes. Use the DBL instance of this VI to implement a
       single control loop. Use the DBL Array instance to implement parallel multi-loop
        control.


      Inputs/Outputs

               •      setpoint —

            setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

               •      process variable —

            process variable specifies the measured value of the process variable being controlled. This
            value is equal to the feedback value of the feedback control loop.

               •      PID parameters —

           PID parameters is a cluster containing the updated PID gains parameters for each controller. You


5722   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5722 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5723 ordinal=5723 -->
## Functions

Functions


  can use the updated values with other PID VIs.

      •     Kp —

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       Ti —

       integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

      •      Td —


•     manual control —

  manual control specifies the value of the control output when auto? is FALSE.

•      options —

  options specifies the settings for the PID control.

      •      sp low —

      sp low specifies the lower bound of the setpoint range in terms of percentage points or
      engineering units.

      •      sp high —

      sp high specifies the upper bound of the setpoint range in terms of percentage points or
      engineering units.

      •      out low —

      out low specifies the lower bound of the output range in terms of percentage points or
      engineering units.

      •      out high —

      out high specifies the upper bound of the output range in terms of percentage points or
      engineering units.

      •      hold (F) —


                                                   © National Instruments 5723

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5723 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5724 ordinal=5724 -->
## Functions

Functions


               hold specifies whether the controller ignores changes in the process variable and suspends
               any integral action. If you set hold as TRUE, output will retain its previous value. The default
                      is FALSE.

                     •      auto (T) —

             TRUE selects automatic control, FALSE puts controller in manual. Bumpless transfer is used
               from automatic to manual.

                     •       pro. band (F) —

                 pro. band indicates whether the proportional value of PID parameters input is proportional
                 gain (Kc) or proportional band (PB). The default is FALSE, which means the proportional
                value is proportional gain. The conversion rate is Kc = 100/PB.

                     •      reverse acting (T) —

                reverse acting specifies whether the control is reverse- or forward-acting. The default is
               TRUE, which means output decreases if the input is greater than the setpoint.

                     •      beta —

               beta specifies the relative emphasis of setpoint tracking to disturbance rejection. The
                 default value of 1 is appropriate for most applications. You can use a smaller value between
               0 and 1 to specify emphasis on disturbance rejection, such as process load changes.

              The VI uses this value in the two degree-of-freedom algorithm.

                     •       linearity —

                  linearity specifies the linearity of the error response. The valid range for linearity is 0 to 1. A
                value of 1 provides a normal linear response, while a value of 0.1 provides an approximately
                 parabolic response.

              The VI uses this value in the nonlinear error calculation and the nonlinear gain factor
                  calculation.

                     •      dt (s) —

                dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s)
                      is less than or equal to zero, this VI calculates the time since it was last called using an


5724   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5724 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5725 ordinal=5725 -->
## Functions

Functions


         internal timer with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value
           explicitly. The default is -1.


   •       iteration —

     iteration is the current iteration of the loop.

    Wire this parameter to the iteration terminal of the While Loop.

   •      output —

    output returns the control output of the PID algorithm that is applied to the controlled process.
       If this VI receives an invalid input, output returns NaN.


You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of the process variable input determines the
length of the output array. Other input arrays do not necessarily need to be the same
length as the process variable input. This VI resizes other input arrays to the same
length as the process variable input as follows:

  •  If the input array is longer than the process variable input, the input array is
    truncated to the length of the process variable input. Additional values in the array
    are not used.
  •  If the input array is shorter than the process variable input, the last value of the
    input array is repeated until the size matches that of the process variable input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\General PID Simulator.vi


                                                    © National Instruments 5725

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5725 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5726 ordinal=5726 -->
## Functions

Functions

     PIDPID AdvancedAdvanced

      Implements a PID controller using a PID algorithm with advanced optional features.
      The advanced PID algorithm includes the features of the algorithm the PID VI uses, as
       well as manual mode control with bumpless manual-to-automatic transitions,
       nonlinear integral action, two degree-of-freedom control, and error-squared control.
      Use the DBL instance of this VI to implement a single control loop. Use the DBL Array
       instance to implement parallel multi-loop control.


            • PID Advanced (DBL) VI
            • PID Advanced (DBL Array) VI

      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the process variable input determines the
       length of the output array. Other input arrays do not necessarily need to be the same
       length as the process variable input. This VI resizes other input arrays to the same
       length as the process variable input as follows:

            •  If the input array is longer than the process variable input, the input array is
          truncated to the length of the process variable input. Additional values in the array
          are not used.
            •  If the input array is shorter than the process variable input, the last value of the
          input array is repeated until the size matches that of the process variable input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Bumpless Manual-to-Automatic Transfer

       This VI supports bumpless manual-to-automatic transfer, which ensures a smooth
       controller output during the transition from manual to automatic control mode.


5726   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5726 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5727 ordinal=5727 -->
## Functions

Functions

Bumpless Automatic-to-Manual Transfer

This VI cannot implement bumpless automatic-to-manual transfer. To ensure a
smooth transition from automatic to manual control mode, you must design your
application so that the manual output value matches the control output value at the
time that the control mode switches from automatic to manual. You can do this by
using a local variable for manual control, as shown in the following block diagram.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Manual-Automatic Control.vi

PIDPID AdvancedAdvanced (DBL)(DBL) VIVI

Implements a PID controller using a PID algorithm with advanced optional features.
The advanced PID algorithm includes the features of the algorithm the PID VI uses, as
well as manual mode control with bumpless manual-to-automatic transitions,
nonlinear integral action, two degree-of-freedom control, and error-squared control.
Use the DBL instance of this VI to implement a single control loop. Use the DBL Array
instance to implement parallel multi-loop control.


                                                    © National Instruments 5727

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5727 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5728 ordinal=5728 -->
## Functions

Functions


      Inputs/Outputs

               •      alpha —

           alpha specifies the derivative filter time constant. Increasing this value increases damping of
             derivative action.

           alpha can be a value between 0 and 1 or NaN, which specifies that no derivative filter is applied.

               •    gamma —

         gamma specifies an amount by which to weight the error applied to derivative action. The
             default value is 0, which avoids the derivative kick, or sudden change in controller output, that
           can occur after a change in the setpoint value.

              In certain cascade control operations where derivative kick is not a concern, increasing gamma
           might improve the speed of the first PID controller.

               •     manual control —

          manual control specifies the value of the control output when auto? is FALSE.

               •      auto? (T) —

           auto? specifies whether to use automatic or manual control. In some situations, you might need
             to switch off the PID controller and operate the system in manual, or open-loop, mode. The
             default is TRUE.

         When auto? is TRUE, this VI uses automatic control. When auto? is FALSE, this VI uses manual
              control. This VI uses bumpless transfer from manual control to automatic control.

               •      output range —


5728   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5728 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5729 ordinal=5729 -->
## Functions

Functions


  output range specifies the range to which to coerce the control output. The default range is –100
  to 100, which corresponds to values specified in terms of percentage of full scale.

  You can change this range to something that is appropriate for your control system. For example,
  you can relate engineering units to engineering units instead of percentage to percentage. This
  VI implements integrator anti-windup when the controller output is saturated at the specified
  minimum or maximum values.

      •      output high —

      output high specifies the maximum value of the controller output. The default is 100.

      •      output low —

      output low specifies the minimum value of the controller output. The default is –100.


•      setpoint —

  setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

•      process variable —

  process variable specifies the measured value of the process variable being controlled. This
  value is equal to the feedback value of the feedback control loop.

•      setpoint range —

  setpoint range specifies the maximum and minimum values for the setpoint/process variable
  range. This VI uses the setpoint range to calculate nonlinear integral action. The default range is
  0 to 100, which corresponds to values specified in terms of percentage of full scale. You can
  change this range to something that is appropriate for your control system. For example, you
  can relate engineering units to engineering units instead of percentage to percentage.

  This VI uses the setpoint range in the nonlinear integral action calculation and the nonlinear
  error calculation.

      •      setpoint high —

      setpoint high specifies the maximum value of the setpoint/process variable range.

      •      setpoint low —


                                                   © National Instruments 5729

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5729 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5730 ordinal=5730 -->
## Functions

Functions


                setpoint low specifies the minimum value of the setpoint/process variable range.


               •      PID gains —

           PID gains specifies the proportional gain, integral time, and derivative time parameters of the
              controller.

                     •      proportional gain (Kc) —

                proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

                  In the equation that defines the PID controller, KC represents the proportional gain.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


               •      dt (s) —

            dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
           than or equal to zero, this VI calculates the time since it was last called using an internal timer
            with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
                -1.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
               error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
             control loop without restarting the entire application. The default is FALSE.

               •      beta —

           beta specifies the relative emphasis of setpoint tracking to disturbance rejection. The default
            value of 1 is appropriate for most applications. You can use a smaller value between 0 and 1 to
             specify emphasis on disturbance rejection, such as process load changes.


5730   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5730 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5731 ordinal=5731 -->
## Functions

Functions


    The VI uses this value in the two degree-of-freedom algorithm.

   •       linearity —

     linearity specifies the linearity of the error response. The valid range for linearity is 0 to 1. A
    value of 1 provides a normal linear response, while a value of 0.1 provides an approximately
    parabolic response.

    The VI uses this value in the nonlinear error calculation and the nonlinear gain factor calculation.

   •      output —

    output returns the control output of the PID algorithm that is applied to the controlled process.
       If this VI receives an invalid input, output returns NaN.

   •      dt out (s) —

    dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
    or the computed interval if you set dt (s) to –1.


You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of the process variable input determines the
length of the output array. Other input arrays do not necessarily need to be the same
length as the process variable input. This VI resizes other input arrays to the same
length as the process variable input as follows:

  •  If the input array is longer than the process variable input, the input array is
    truncated to the length of the process variable input. Additional values in the array
    are not used.
  •  If the input array is shorter than the process variable input, the last value of the
    input array is repeated until the size matches that of the process variable input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Bumpless Manual-to-Automatic Transfer

This VI supports bumpless manual-to-automatic transfer, which ensures a smooth


                                                    © National Instruments 5731

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5731 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5732 ordinal=5732 -->
## Functions

Functions

       controller output during the transition from manual to automatic control mode.

     Bumpless Automatic-to-Manual Transfer

       This VI cannot implement bumpless automatic-to-manual transfer. To ensure a
      smooth transition from automatic to manual control mode, you must design your
       application so that the manual output value matches the control output value at the
      time that the control mode switches from automatic to manual. You can do this by
       using a local variable for manual control, as shown in the following block diagram.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Manual-Automatic Control.vi

      PIDPID AdvancedAdvanced (DBL(DBL Array)Array) VIVI

      Implements a PID controller using a PID algorithm with advanced optional features.
      The advanced PID algorithm includes the features of the algorithm the PID VI uses, as
       well as manual mode control with bumpless manual-to-automatic transitions,
       nonlinear integral action, two degree-of-freedom control, and error-squared control.
      Use the DBL instance of this VI to implement a single control loop. Use the DBL Array
       instance to implement parallel multi-loop control.


5732   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5732 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5733 ordinal=5733 -->
## Functions

Functions


Inputs/Outputs

   •    gamma —

   gamma specifies an amount by which to weight the error applied to derivative action. The
     default value is 0, which avoids the derivative kick, or sudden change in controller output, that
    can occur after a change in the setpoint value.

     In certain cascade control operations where derivative kick is not a concern, increasing gamma
    might improve the speed of the first PID controller.

    This VI resizes the gamma input array to match the size of the process variable input array.

   •     manual control —

    manual control specifies the value of the control output when auto? is FALSE. This VI resizes the
    manual control input array to match the size of the process variable input array.

   •      auto? (T) —

    auto? specifies whether to use automatic or manual control. When auto? is TRUE, this VI uses
    automatic control. When auto? is FALSE, this VI uses manual control. This VI uses bumpless
     transfer from manual control to automatic control. The default is TRUE.

    This VI resizes the auto? input array to match the size of the process variable input array.

   •      output range —

    output range specifies the range to which to coerce the control output. The default range is -100
    to 100, which corresponds to values specified in terms of percentage of full scale.

    You can change this range to something that is appropriate for your control system. For example,
    you can relate engineering units to engineering units instead of percentage to percentage. This


                                                    © National Instruments 5733

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5733 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5734 ordinal=5734 -->
## Functions

Functions


              VI implements integrator anti-windup when the controller output is saturated at the specified
         minimum or maximum values.

           output range is an array of clusters of the following elements.

                     •      output high —

               output high specifies the maximum value of the controller output. The default is 100.

                     •      output low —

               output low specifies the minimum value of the controller output. The default is –100.


               •      setpoint —

            setpoint specifies the setpoint value, or desired value, of the process variable being controlled.
             This VI resizes the setpoint input array to match the size of the process variable input array.

               •      process variable —

            process variable specifies the measured value of the process variable being controlled. This
            value is equal to the feedback value of the feedback control loop.

               •      setpoint range —

            setpoint range specifies the maximum and minimum values for the setpoint/process variable
             range. This VI uses the setpoint range to calculate nonlinear integral action. The default range is
           0 to 100, which corresponds to values specified in terms of percentage of full scale. You can
           change this range to something that is appropriate for your control system. For example, you
           can relate engineering units to engineering units instead of percentage to percentage.

             This VI uses the setpoint range in the nonlinear integral action calculation and the nonlinear
             error calculation.

                     •      setpoint high —

                setpoint high specifies the maximum value of the setpoint/process variable range.

                     •      setpoint low —

                setpoint low specifies the minimum value of the setpoint/process variable range.


5734   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5734 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5735 ordinal=5735 -->
## Functions

Functions

•      PID gains —

  PID gains is an array of clusters of the following elements.

      •      proportional gain (Kc) —

      proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       integral time (Ti, min) —

       integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

      •       derivative time (Td, min) —

       derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


•      dt (s) —

  dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
  than or equal to zero, this VI calculates the time since it was last called using an internal timer
  with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
   -1.

•       reinitialize? (F) —

   reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
   error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
  control loop without restarting the entire application. The default is FALSE.

•      beta —

  beta specifies the relative emphasis of disturbance rejection to setpoint tracking. The default
  value of 1 is appropriate for most applications. You can use a smaller value between 0 and 1 to
  specify emphasis on disturbance rejection, such as process load changes. This VI resizes the beta
  input array to match the size of the process variable input array.

•       linearity —

  linearity specifies the linearity of the error response. The valid range for linearity is 0 to 1. A
  value of 1 provides a normal linear response, while a value of 0.1 provides an approximately
  parabolic response.


                                                   © National Instruments 5735

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5735 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5736 ordinal=5736 -->
## Functions

Functions


          The VI uses this value in the nonlinear error calculation and the nonlinear gain factor calculation.

               •      output —

           output returns the control output of the PID algorithm that is applied to the controlled process.
             This VI determines the length of the output array from the size of the process variable input
              array.

               •      dt out (s) —

            dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
            or the computed interval if you set dt (s) to –1.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the process variable input determines the
       length of the output array. Other input arrays do not necessarily need to be the same
       length as the process variable input. This VI resizes other input arrays to the same
       length as the process variable input as follows:

            •  If the input array is longer than the process variable input, the input array is
          truncated to the length of the process variable input. Additional values in the array
          are not used.
            •  If the input array is shorter than the process variable input, the last value of the
          input array is repeated until the size matches that of the process variable input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Bumpless Manual-to-Automatic Transfer

       This VI supports bumpless manual-to-automatic transfer, which ensures a smooth
       controller output during the transition from manual to automatic control mode.

     Bumpless Automatic-to-Manual Transfer

       This VI cannot implement bumpless automatic-to-manual transfer. To ensure a
      smooth transition from automatic to manual control mode, you must design your

5736   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5736 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5737 ordinal=5737 -->
## Functions

Functions

application so that the manual output value matches the control output value at the
time that the control mode switches from automatic to manual. You can do this by
using a local variable for manual control, as shown in the following block diagram.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Manual-Automatic Control.vi

PIDPID AdvancedAdvanced AutotuningAutotuning

Implements a PID controller using a PID algorithm with advanced optional features,
and applies autotuning to the controller. You can use this VI in RT applications.

      Note This VI incorporates the functionality of both the PID Advanced VI and
       the PID Online Autotuning VI.


                                                    © National Instruments 5737

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5737 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5738 ordinal=5738 -->
## Functions

Functions


      Inputs/Outputs

               •      alpha —

           alpha specifies the derivative filter time constant. Increasing this value increases damping of
             derivative action.

           alpha can be a value between 0 and 1 or NaN, which specifies that no derivative filter is applied.

               •    gamma —

         gamma specifies an amount by which to weight the error applied to derivative action. The
             default value is 0, which avoids the derivative kick, or sudden change in controller output, that
           can occur after a change in the setpoint value.

              In certain cascade control operations where derivative kick is not a concern, increasing gamma
           might improve the speed of the first PID controller.

               •     manual control —

          manual control specifies the value of the control output when auto? is FALSE.

               •      auto? (F) —

           auto? specifies whether the PID controller uses automatic or manual control. This VI considers
            the autotune? input and the technique you specify in the autotuning parameters input when
            determining the Boolean value to propagate to the auto? input of the PID Advanced VI. The
             default is FALSE.

               •      output range —

           output range specifies the range to which to coerce the control output. The default range is –100


5738   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5738 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5739 ordinal=5739 -->
## Functions

Functions


  to 100, which corresponds to values specified in terms of percentage of full scale.

  You can change this range to something that is appropriate for your control system. For example,
  you can relate engineering units to engineering units instead of percentage to percentage. This
  VI implements integrator anti-windup when the controller output is saturated at the specified
  minimum or maximum values.

      •      output high —

      output high specifies the maximum value of the controller output. The default is 100.

      •      output low —

      output low specifies the minimum value of the controller output. The default is –100.


•      setpoint —

  setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

•      process variable —

  process variable specifies the measured value of the process variable being controlled. This
  value is equal to the feedback value of the feedback control loop.

•      autotune? (F) —

  autotune? specifies to begin autotuning. Wire this input from a Boolean control with latched
  mechanical action and a default value of FALSE. The default is FALSE.

•      PID gains —

  PID gains specifies the proportional gain, integral time, and derivative time parameters of the
  controller.

      •      proportional gain (Kc) —

      proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       integral time (Ti, min) —


                                                   © National Instruments 5739

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5739 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5740 ordinal=5740 -->
## Functions

Functions


                  integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


               •      dt (s) —

            dt (s) specifies the loop-cycle time, or interval in seconds, at which the PID Online Autotuning
          and PID Advanced VIs are called. If dt (s) is less than or equal to zero, the VIs calculate the time
             since they were last called using an internal timer with 1 ms resolution. If dt (s) must be less than
           1 ms, specify the value explicitly. The default is –1.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
               error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
             control loop without restarting the entire application. The default is FALSE.

               •      beta —

           beta specifies the relative emphasis of disturbance rejection to setpoint tracking. The default
            value of 1 is appropriate for most applications. You can use a smaller value between 0 and 1 to
             specify emphasis on disturbance rejection, such as process load changes.

          The PID Advanced VI uses this value in the two degree-of-freedom algorithm. If Autotune? is
           TRUE, this VI sets beta to 1.

               •      autotuning parameters —

            autotuning parameters specifies various parameters used for the autotuning process. You can
             select these values manually in the Autotuning Wizard.

                     •      technique —

               technique specifies the autotuning technique to use.

                Step Open Loop—Specifies to use open-loop (step test) tuning, which assumes that you
               0
                can model any process as a first-order lag and a pure dead time system.


5740   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5740 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5741 ordinal=5741 -->
## Functions

Functions


       Step Closed Loop—Specifies to use closed-loop (ultimate gain) tuning, which is very      1
        accurate, but requires that your process be in steady-state oscillation.
        Relay—Specifies to use relay feedback tuning, which applies an on-off relay in a closed-
      2 loop test in order to obtain controlled oscillations and extract values for ultimate gain and
        ultimate frequency. This technique also incorporates hysteresis to reduce noise.
       PID Relay—Specifies to use PID relay tuning, which connects a relay and an extra feedback      3        signal with the setpoint and keeps the PID controller in the loop with the relay.

      •      type of controller —

      type of controller specifies which parameters to return as the output of the tuning process.

      0 P—Specifies to return only the proportional parameters.
      1 PI—Specifies to return the proportional and integral parameters.
      2 PID—Specifies to return the proportional, integral, and derivative parameters.

      •      control specification —

       control specification specifies the desired response performance of the PID parameters
      determined by the autotuning process.

      0 normal—Specifies a normal response performance.
        fast—Specifies a fast response performance. Faster response generally results in a smaller
      1         rise time.
        slow—(Default) Specifies a slow response performance. Slower response generally results
      2         in less overshoot.

      •      amplitude —

      amplitude specifies the amplitude of the setpoint relay action. The setpoint relay is
      between setpoint – amplitude and setpoint + amplitude.


•      output —

  output returns the control output of the PID algorithm that is applied to the controlled process.
   If this VI receives an invalid input, output returns NaN.

•      tuned PID gains —


                                                   © National Instruments 5741

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5741 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5742 ordinal=5742 -->
## Functions

Functions


          Tuned PID Gains retains the tuned proportional gain, integral time, and derivative time
           parameters of the controller.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


               •      tuning completed? —

            tuning completed? indicates completion of the autotuning process. You can use this output to
           determine when to update the PID gains.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Autotuning PID Online.vi

     PIDPID AutotuningAutotuning (Temperature)(Temperature)

        Directly controls and tunes a system. You can use this VI to improve performance of
       not only temperature systems, but alsoother types of systems that contain dead time.
       This VI uses internal model control to compensate for dead time and tune the system.


5742   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5742 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5743 ordinal=5743 -->
## Functions

Functions


Inputs/Outputs

   •     manual control —

    manual control specifies the value of the control output when auto? is FALSE.

   •      auto? (T) —

    auto? specifies whether to use automatic or manual control. In some situations, you might need
    to switch off the PID controller and operate the system in manual, or open-loop, mode. The
     default is TRUE.

   When auto? is TRUE, this VI uses automatic control. When auto? is FALSE, this VI uses manual
     control. This VI uses bumpless transfer from manual control to automatic control.

   •      output range —

    output range specifies the range to which to coerce the control output. The default range is –100
    to 100, which corresponds to values specified in terms of percentage of full scale.

    You can change this range to something that is appropriate for your control system. For example,
    you can relate engineering units to engineering units instead of percentage to percentage. This
     VI implements integrator anti-windup when the controller output is saturated at the specified
   minimum or maximum values.

         •      output high —

        output high specifies the maximum value of the controller output. The default is 100.

         •      output low —


                                                    © National Instruments 5743

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5743 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5744 ordinal=5744 -->
## Functions

Functions


               output low specifies the minimum value of the controller output. The default is –100.


               •      desired temperature —

            desired temperature specifies the desired temperature (setpoint value) of the system.

               •     measured temperature —

          measured temperature specifies the measured temperature (measured value of the process
             variable) of the system. This value is equal to the feedback value of the feedback control loop.

               •      plant parameters in —

            plant parameters in specifies the gain, time constant, and time delay (dead time) of the plant.

                     •      process gain —

                process gain specifies the process gain (K).

                     •      time constant (s) —

               time constant (s) specifies the time constant (T), in seconds.

                     •      delay time (s) —

                delay time (s) specifies the delay time (L), in seconds.


               •      autotune? (F) —

           autotune? specifies to begin autotuning. Wire this input from a Boolean control with latched
           mechanical action and a default value of FALSE. The default is FALSE.

               •      PID gains in —

           PID gains in specifies the proportional gain, integral time, and derivative time parameters of the
              controller.

                     •      proportional gain (Kc) —


5744   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5744 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5745 ordinal=5745 -->
## Functions

Functions


      proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       integral time (Ti, min) —

       integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

      •       derivative time (Td, min) —

       derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


•      dt (s) —

  dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
  than or equal to zero, this VI calculates the time since it was last called using an internal timer
  with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
   -1.

•       reinitialize? (F) —

   reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
   error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
  control loop without restarting the entire application. The default is FALSE.

•      beta —

  beta specifies the relative emphasis of setpoint tracking to disturbance rejection. The default
  value of 1 is appropriate for most applications. You can use a smaller value between 0 and 1 to
  specify emphasis on disturbance rejection, such as process load changes.

  The VI uses this value in the two degree-of-freedom algorithm.

•      autotuning parameters —

  autotuning parameters specifies various parameters used for the autotuning process.

      •      type of controller —

      type of controller specifies which parameters to return as the output of the tuning process.


                                                   © National Instruments 5745

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5745 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5746 ordinal=5746 -->
## Functions

Functions


               0 P—Specifies to return only the proportional parameters.
               1 PI—Specifies to return the proportional and integral parameters.
               2 PID—Specifies to return the proportional, integral, and derivative parameters.

                     •      time constant factor —

               time constant factor specifies a divider to apply to the identified time constant to obtain
                the desired time constant response. Setting time constant factor to a value greater than 1
              makes the desired time constant used in the design faster. Setting time constant factor to a
                value less than 1 makes the response slower.

                     •      step amplitude —

                step amplitude specifies the amplitude of the setpoint relay action. The setpoint relay is
              between setpoint- amplitudeand setpoint+ amplitude.


               •      alpha —

           alpha specifies the derivative filter time constant. Increasing this value increases damping of
             derivative action.

           alpha can be a value between 0 and 1 or NaN, which specifies that no derivative filter is applied.

               •      output —

           output returns the control output of the PID algorithm that is applied to the controlled process.
                    If this VI receives an invalid input, output returns NaN.

               •      tuning completed? —

            tuning completed? returns TRUE when the autotuning process is complete. You can use this
           output to determine when to update the PID gains in.

               •      plant parameters out —

            plant parameters out returns the calculated gain, time constant, and dead time of the plant.

                     •      process gain —


5746   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5746 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5747 ordinal=5747 -->
## Functions

Functions


        process gain returns the calculated process gain (K).

         •      time constant (s) —

        time constant (s) returns the calculated time constant (T), in seconds.

         •      delay time (s) —

        delay time (s) returns the calculated delay time (L), in seconds.


   •      PID gains out —

    PID gains out returns the updated PID gain parameters upon completion of the autotuning
    process. Normal output values are identical to the values in the PID gains in input.

         •      proportional gain (Kc) —

        proportional gain (Kc) returns the proportional gain of the controller.

         •       integral time (Ti, min) —

         integral time (Ti, min) returns the integral time in minutes.

         •       derivative time (Td, min) —

         derivative time (Td, min) returns the derivative time in minutes.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning Smith
   Predictor.vi

PIDPID AutotuningAutotuning

Includes the Autotuning Wizard in addition to the basic PID algorithm. You can use this

                                                    © National Instruments 5747

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5747 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5748 ordinal=5748 -->
## Functions

Functions

        VI instead of the PID VI, which implements a basic PID algorithm. Use the additional
       inputs and output of this VI to set autotuning parameters, invoke the Autotuning
       Wizard, and update the PID gains.

           Note Because this VI invokes the Autotuning Wizard, which requires user
                interaction, it is not available on RT. To perform autotuning on an RT target,
             use the PID Advanced Autotuning VI.


      Inputs/Outputs

               •      autotuning parameters —

            autotuning parameters specifies various parameters used for the autotuning process. You can
             select these values manually in the Autotuning Wizard.

                     •       controller type —

                 controller type specifies which parameters to return as the output of the tuning process.

               0 PID—Specifies to return the proportional, integral, and derivative parameters.
               1 PI (default)—Specifies to return the proportional and integral parameters.
               2 P—Specifies to return only the proportional parameters.

                     •       relay cycles —

                 relay cycles specifies the number of setpoint relay cycles to use to determine the ultimate
                 gain and period. More cycles result in more accurate parameter estimation; however, slower
               systems might require more time for numerous cycles.

                     •       relay amplitude —


5748   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5748 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5749 ordinal=5749 -->
## Functions

Functions


       relay amplitude specifies the amplitude of the setpoint relay action. The setpoint relay is
      between setpoint– relayamplitudeand setpoint+ relayamplitude.

      •      control specification —

       control specification specifies the desired response performance of the PID parameters
      determined by the autotuning process.

      0 normal—Specifies a normal response performance.
        fast—Specifies a fast response performance. Faster response generally results in a smaller      1         rise time.
        slow—(Default) Specifies a slow response performance. Slower response generally results      2
         in less overshoot.

      •     PV noise level —

     PV noise level specifies an estimation of the noise level of the process variable. This value is
      used as the hysteresis for the setpoint relay action.


•      output range —

  output range specifies the range to which to coerce the control output. The default range is –100
  to 100, which corresponds to values specified in terms of percentage of full scale.

  You can change this range to something that is appropriate for your control system. For example,
  you can relate engineering units to engineering units instead of percentage to percentage. This
  VI implements integrator anti-windup when the controller output is saturated at the specified
  minimum or maximum values.

      •      output high —

      output high specifies the maximum value of the controller output. The default is 100.

      •      output low —

      output low specifies the minimum value of the controller output. The default is –100.


•      setpoint —


                                                   © National Instruments 5749

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5749 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5750 ordinal=5750 -->
## Functions

Functions


            setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

               •      process variable —

            process variable specifies the measured value of the process variable being controlled. This
            value is equal to the feedback value of the feedback control loop.

               •      PID gains —

           PID gains specifies the proportional gain, integral time, and derivative time parameters of the
              controller.

                     •      proportional gain (Kc) —

                proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

                  In the equation that defines the PID controller, KC represents the proportional gain.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


               •      dt (s) —

            dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
           than or equal to zero, this VI calculates the time since it was last called using an internal timer
            with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
                -1.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
               error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
             control loop without restarting the entire application. The default is FALSE.

               •      autotune? (F) —

           autotune? starts the autotuning procedure and invokes the Autotuning Wizard, when TRUE. Wire


5750   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5750 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5751 ordinal=5751 -->
## Functions

Functions


     this input from a Boolean control with latched mechanical action and a default value of FALSE.

   •      output —

    output returns the control output of the PID algorithm that is applied to the controlled process.
       If this VI receives an invalid input, output returns NaN.

   •      tuning completed? —

    tuning completed? indicates completion of the autotuning process. You can use this output to
    determine when to update the PID gains.

   •      PID gains out —

    PID gains out returns the updated PID gain parameters upon completion of the autotuning
    process. Normal output values are identical to the values in the PID gains input.

         •      proportional gain (Kc) —

        proportional gain (Kc) returns the proportional gain of the controller.

         •       integral time (Ti, min) —

         integral time (Ti, min) returns the integral time in minutes.

         •       derivative time (Td, min) —

         derivative time (Td, min) returns the derivative time in minutes.


   •      dt out (s) —

    dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
    or the computed interval if you set dt (s) to –1.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\General Auto PID
   Simulator.vi


                                                    © National Instruments 5751

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5751 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5752 ordinal=5752 -->
## Functions

Functions

     PIDPID GainGain ScheduleSchedule

       Selects a set of PID gains from a gain schedule for the control of processes that require
        different sets of gains for different regions of operation, such as highly nonlinear
       processes. Use the DBL instance of this VI to implement a single control loop. Use the
     DBL Array instance to implement parallel multi-loop control.


            • PID Gain Schedule (DBL) VI
            • PID Gain Schedule (DBL Array) VI

      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the gain scheduling value input determines the
       length of the output array. Other input arrays do not necessarily need to be the same
       length as the gain scheduling value input. This VI resizes other input arrays to the
     same length as the gain scheduling value input as follows:

            •  If the input array is longer than the gain scheduling value input, the input array is
          truncated to the length of the gain scheduling value input. Additional values in the
           array are not used.
            •  If the input array is shorter than the gain scheduling value input, the last value of
          the input array is repeated until the size matches that of the gain scheduling value
           input.

        In this manner, an input value that should be used for each output calculation does
       not need to be specified repeatedly in the array passed into this VI. Instead, the array
      can consist of a single value that is used for each output calculation.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Gain Scheduling Simulator.vi


5752   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5752 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5753 ordinal=5753 -->
## Functions

Functions

PIDPID GainGain ScheduleSchedule (DBL)(DBL) VIVI

Selects a set of PID gains from a gain schedule for the control of processes that require
different sets of gains for different regions of operation, such as highly nonlinear
processes. Use the DBL instance of this VI to implement a single control loop. Use the
DBL Array instance to implement parallel multi-loop control.


Inputs/Outputs

   •      gain scheduling value —

    gain scheduling value specifies the current input value to use to select PID gains from the gain
    schedule.

   •      PID gain schedule —

    PID gain schedule specifies the gain schedule for the proportional, integral, and derivative gain
    parameters. Specify the maximum values for the PID gain schedule in ascending order. This VI
    uses the first set of PID gains in the array for all gain scheduling values less than the
    corresponding maximum value.

       If you define a maximum setpoint value and the actual setpoint rises above that value, this VI
    continues to behave as if the maximum setpoint value were still in effect.

         •      PID gains —

        PID gains specifies the proportional gain, integral time, and derivative time parameters of
        the controller.

                •      proportional gain (Kc) —

             proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

              In the equation that defines the PID controller, KC represents the proportional gain.

                •       integral time (Ti, min) —


                                                    © National Instruments 5753

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5753 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5754 ordinal=5754 -->
## Functions

Functions


                      integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

                           •       derivative time (Td, min) —

                      derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


                     •     max value —

            max value specifies the maximum value of the range of the gain scheduling value.


               •      index out —

            index out returns the index of the element in the PID gain schedule array corresponding to the
           PID gains out output.

               •      PID gains out —

           PID gains out returns the current PID gains from the gain schedule.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the gain scheduling value input determines the
       length of the output array. Other input arrays do not necessarily need to be the same
       length as the gain scheduling value input. This VI resizes other input arrays to the
     same length as the gain scheduling value input as follows:


5754   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5754 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5755 ordinal=5755 -->
## Functions

Functions

  •  If the input array is longer than the gain scheduling value input, the input array is
    truncated to the length of the gain scheduling value input. Additional values in the
    array are not used.
  •  If the input array is shorter than the gain scheduling value input, the last value of
   the input array is repeated until the size matches that of the gain scheduling value
    input.

In this manner, an input value that should be used for each output calculation does
not need to be specified repeatedly in the array passed into this VI. Instead, the array
can consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Gain Scheduling Simulator.vi

PIDPID GainGain ScheduleSchedule (DBL(DBL Array)Array) VIVI

Selects a set of PID gains from a gain schedule for the control of processes that require
different sets of gains for different regions of operation, such as highly nonlinear
processes. Use the DBL instance of this VI to implement a single control loop. Use the
DBL Array instance to implement parallel multi-loop control.


Inputs/Outputs

   •      gain scheduling value —

    gain scheduling value specifies the current input value to use to select PID gains from the gain
    schedule.

   •      PID gain schedule —

    PID gain schedule specifies the gain schedule for the proportional, integral, and derivative gain
    parameters. Specify the maximum values for the PID gain schedule in ascending order. This VI


                                                    © National Instruments 5755

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5755 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5756 ordinal=5756 -->
## Functions

Functions


            uses the first set of PID gains in the array for all gain scheduling values less than the
            corresponding maximum value.

                    If you define a maximum setpoint value and the actual setpoint rises above that value, this VI
            continues to behave as if the maximum setpoint value were still in effect.

                     •      PID gains —

               PID gains specifies the proportional gain, integral time, and derivative time parameters of
                the controller.

                           •      proportional gain (Kc) —

                    proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

                       In the equation that defines the PID controller, KC represents the proportional gain.

                           •       integral time (Ti, min) —

                      integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

                           •       derivative time (Td, min) —

                      derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


                     •     max value —

            max value specifies the maximum value of the range of the gain scheduling value.


               •      index out —

            index out returns the indexes of the elements in the PID gain schedule array corresponding to
           each element of the PID gains out output array.

               •      PID gains out —

           PID gains out returns the current PID gains from the gain schedule.

                     •      proportional gain (Kc) —


5756   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5756 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5757 ordinal=5757 -->
## Functions

Functions


        proportional gain (Kc) returns the proportional gain of the controller.

         •       integral time (Ti, min) —

         integral time (Ti, min) returns the integral time in minutes.

         •       derivative time (Td, min) —

         derivative time (Td, min) returns the derivative time in minutes.


You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of the gain scheduling value input determines the
length of the output array. Other input arrays do not necessarily need to be the same
length as the gain scheduling value input. This VI resizes other input arrays to the
same length as the gain scheduling value input as follows:

  •  If the input array is longer than the gain scheduling value input, the input array is
    truncated to the length of the gain scheduling value input. Additional values in the
    array are not used.
  •  If the input array is shorter than the gain scheduling value input, the last value of
   the input array is repeated until the size matches that of the gain scheduling value
    input.

In this manner, an input value that should be used for each output calculation does
not need to be specified repeatedly in the array passed into this VI. Instead, the array
can consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Gain Scheduling Simulator.vi

PIDPID StructureStructure ConversionConversion

Converts a PID controller or controllers in Academic, Parallel, or Series form into the

                                                    © National Instruments 5757

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5757 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5758 ordinal=5758 -->
## Functions

Functions

      form (Academic) and PID gains units that the PID VIs expect. Wire data to the
       proportional, integral, or derivative input to determine the polymorphic instance to
       use, or manually select the instance.


            • PID Structure Conversion (DBL) VI
            • PID Structure Conversion (DBL Array) VI

      Each PID form produces the same result but incorporates information in a different
      manner. The following equations describe each form:

      PID Academic


      PID Parallel


      To convert a controller in Parallel form to Academic form, this VI converts the
       proportional, integral, and derivative values according to their changes in units and
       applies the following transformations:

    Kc = KpTi = Kc/KiTd = Kd/Kp

      PID Series


      To convert a controller in Series form to Academic form, this VI converts the
       proportional, integral, and derivative values according to their changes in units and
       applies the following transformations:

                Ti = T'I+T'D


5758   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5758 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5759 ordinal=5759 -->
## Functions

Functions

PIDPID StructureStructure ConversionConversion (DBL)(DBL) VIVI

Converts a PID controller or controllers in Academic, Parallel, or Series form into the
form (Academic) and PID gains units that the PID VIs expect. Wire data to the
proportional, integral, or derivative input to determine the polymorphic instance to
use, or manually select the instance.


Inputs/Outputs

   •      proportional unit —

    proportional unit specifies the units associated with the proportional (P) component of the PID
     controller to convert.

    The relationship between the available units is Kc = 100 / PB.

     Gain (Kc)
    0 (default)—Specifies that the proportional component is expressed in terms of proportional
      gain (Kc).
    Band (PB)
    1      —Specifies that the proportional component is expressed in terms of proportional band (PB).

   •      PID structure —

    PID structure specifies the initial form of the PID controller.

    Refer to the Details section of this topic for the equations that represent each form.

     Academic (Standard)
    0
       (default)—Specifies that the controller is in PID Academic form.
       Parallel
    1
      —Specifies that the controller is in PID Parallel form.


                                                    © National Instruments 5759

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5759 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5760 ordinal=5760 -->
## Functions

Functions


               Series           2
              —Specifies that the controller is in PID Series form.

               •      proportional —

            proportional specifies the value of the proportional (P) component of the PID controller to
             convert.

               •       integral —

             integral specifies the value of the integral (I) component of the PID controller to convert.

               •       derivative —

             derivative specifies the value of the derivative (D) component of the PID controller to convert.

               •       integral unit —

             integral unit specifies the units associated with the integral (I) component of the PID controller
             to convert.

           min           0
               (default)—Specifies that the integral component is expressed in minutes.
              s           1
              —Specifies that the integral component is expressed in seconds.

               •       derivative unit —

             derivative unit specifies the units associated with the derivative (D) component of the PID
             controller to convert.

           min
           0
               (default)—Specifies that the derivative component is expressed in minutes.
              s
           1
              —Specifies that the derivative component is expressed in seconds.

               •      PID gains —

           PID gains returns the updated PID gains parameters, which you can use with other PID VIs.

                     •      proportional gain (Kc) —


5760   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5760 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5761 ordinal=5761 -->
## Functions

Functions


        proportional gain (Kc) returns the proportional gain of the controller.

          •       integral time (Ti, min) —

         integral time (Ti, min) returns the integral time in minutes.

          •       derivative time (Td, min) —

         derivative time (Td, min) returns the derivative time in minutes.


Each PID form produces the same result but incorporates information in a different
manner. The following equations describe each form:

PID Academic


PID Parallel


To convert a controller in Parallel form to Academic form, this VI converts the
proportional, integral, and derivative values according to their changes in units and
applies the following transformations:

Kc = KpTi = Kc/KiTd = Kd/Kp

PID Series


To convert a controller in Series form to Academic form, this VI converts the
proportional, integral, and derivative values according to their changes in units and
applies the following transformations:


                                                    © National Instruments 5761

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5761 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5762 ordinal=5762 -->
## Functions

Functions

                Ti = T'I+T'D

      PIDPID StructureStructure ConversionConversion (DBL(DBL Array)Array) VIVI

       Converts a PID controller or controllers in Academic, Parallel, or Series form into the
      form (Academic) and PID gains units that the PID VIs expect. Wire data to the
       proportional, integral, or derivative input to determine the polymorphic instance to
       use, or manually select the instance.


      Inputs/Outputs

               •      proportional unit —

            proportional unit specifies the units associated with the proportional (P) component of the PID
             controller to convert.

          The relationship between the available units is Kc = 100 / PB.

            Gain (Kc)
           0 (default)—Specifies that the proportional component is expressed in terms of proportional
              gain (Kc).
           Band (PB)
           1
             —Specifies that the proportional component is expressed in terms of proportional band (PB).

               •      PID structure —

           PID structure specifies the initial form of the PID controller.

             Refer to the Details section of this topic for the equations that represent each form.

            Academic (Standard)
           0
               (default)—Specifies that the controller is in PID Academic form.


5762   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5762 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5763 ordinal=5763 -->
## Functions

Functions


     Parallel  1
    —Specifies that the controller is in PID Parallel form.
    Series  2    —Specifies that the controller is in PID Series form.

•      proportional —

  proportional specifies the values of the proportional (P) components of the PID controllers to
  convert.

•       integral —

  integral specifies the values of the integral (I) components of the PID controllers to convert.

•       derivative —

  derivative specifies the values of the derivative (D) components of the PID controllers to convert.

•       integral unit —

  integral unit specifies the units associated with the integral (I) component of the PID controller
  to convert.

   min  0
    (default)—Specifies that the integral component is expressed in minutes.
    s  1
    —Specifies that the integral component is expressed in seconds.

•       derivative unit —

  derivative unit specifies the units associated with the derivative (D) component of the PID
  controller to convert.

   min
  0
    (default)—Specifies that the derivative component is expressed in minutes.
    s
  1
    —Specifies that the derivative component is expressed in seconds.

•      PID parameters —

  PID parameters returns an array containing the updated PID gains parameters for each


                                                   © National Instruments 5763

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5763 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5764 ordinal=5764 -->
## Functions

Functions


              controller. You can use the updated values with other PID VIs.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


      Each PID form produces the same result but incorporates information in a different
      manner. The following equations describe each form:

      PID Academic


      PID Parallel


      To convert a controller in Parallel form to Academic form, this VI converts the
       proportional, integral, and derivative values according to their changes in units and
       applies the following transformations:

    Kc = KpTi = Kc/KiTd = Kd/Kp

      PID Series


      To convert a controller in Series form to Academic form, this VI converts the
       proportional, integral, and derivative values according to their changes in units and

5764   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5764 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5765 ordinal=5765 -->
## Functions

Functions

applies the following transformations:

          Ti = T'I+T'D

PIDPID AutotuningAutotuning DesignDesign

Implements autotuning using the tuning method associated with the polymorphic
instance you select. This VI generates PID parameters based on the Stimulus signal
and Response signal you specify. You can use this VI to generate initial parameters
when you do not have sufficient information about the system you want to tune. You
must manually select the polymorphic instance to use.


  • PID Autotuning Design (Auto) VI
  • PID Autotuning Design (Ziegler-Nichols) VI
  • PID Autotuning Design (Cohen-Coon) VI
  • PID Autotuning Design (Chien-Hrones-Reswick) VI
  • PID Autotuning Design (Internal Model Control) VI

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning PID Offline.vi

PIDPID AutotuningAutotuning DesignDesign (Auto)(Auto) VIVI

Implements autotuning using the tuning method associated with the polymorphic
instance you select. This VI generates PID parameters based on the Stimulus signal
and Response signal you specify. You can use this VI to generate initial parameters
when you do not have sufficient information about the system you want to tune. You
must manually select the polymorphic instance to use.


                                                    © National Instruments 5765

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5765 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5766 ordinal=5766 -->
## Functions

Functions


      Inputs/Outputs

               •       Ziegler-Nichols Speed —

             Ziegler-Nichols Speed specifies the desired response performance of the PID parameters.

              Fast—(Default) Specifies a fast response performance. Faster response generally results in a           0              smaller rise time.
           1 Normal—Specifies a normal response performance.
             Slow—Specifies a slow response performance. Slower response generally results in less           2              overshoot.

               •      Type of Controller —

           Type of Controller specifies which parameters to return as the PID gains.

           0 P—(Default) Specifies to return only the proportional parameters.
           1 PI—Specifies to return the proportional and integral parameters.
           2 PID—Specifies to return the proportional, integral, and derivative parameters.

               •      Stimulus signal —

            Stimulus signal specifies an array that represents the stimulus signal.

               •      Response signal —

           Response signal specifies an array that represents the response signal.

               •      closed-loop? —

            closed-loop? specifies whether the system is a closed-loop system. If you set closed-loop? to
           TRUE, this VI estimates open-loop parameter values based on the closed-loop values it identifies
           from the input signals.

               •      dt (s) —


5766   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5766 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5767 ordinal=5767 -->
## Functions

Functions


  dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
  zero, this VI uses an internal timer with a one millisecond resolution. The default is 0.

•       Controller Gain (K) —

  Controller Gain (K) specifies an initial value for the controller gain, which this VI uses to
  calculate the integral time (Ti, min) component of PID gains. The default is 0.

•      stimulus operating point —

  stimulus operating point returns the calculated stimulus offset for the plant.

•      response operating point —

  response operating point returns the calculated response offset for the plant.

•      PID gains —

  PID gains returns the calculated PID gains values for the plant.

      •      proportional gain (Kc) —

      proportional gain (Kc) returns the proportional gain of the controller.

      •       integral time (Ti, min) —

       integral time (Ti, min) returns the integral time in minutes.

      •       derivative time (Td, min) —

       derivative time (Td, min) returns the derivative time in minutes.


•      Plant Parameters —

  Plant Parameters returns the calculated gain, time constant, and dead time of the plant.

      •      Plant Gain (K) —

      Plant Gain (K) returns the calculated process gain (K).

      •     Time Constant (T) —


                                                   © National Instruments 5767

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5767 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5768 ordinal=5768 -->
## Functions

Functions


              Time Constant (T) returns the calculated time constant (T), in seconds.

                     •     Dead Time (L) —

             Dead Time (L) returns the calculated dead time (L), in seconds.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Autotuning PID Offline.vi

      PIDPID AutotuningAutotuning DesignDesign (Ziegler-Nichols)(Ziegler-Nichols) VIVI

      Implements autotuning using the tuning method associated with the polymorphic
       instance you select. This VI generates PID parameters based on the Stimulus signal
      and Response signal you specify. You can use this VI to generate initial parameters
     when you do not have sufficient information about the system you want to tune. You
      must manually select the polymorphic instance to use.

           Note This instance uses the Ziegler-Nichols tuning method.


      Inputs/Outputs

               •       Ziegler-Nichols Speed —

             Ziegler-Nichols Speed specifies the desired response performance of the PID parameters.


5768   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5768 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5769 ordinal=5769 -->
## Functions

Functions


    Fast—(Default) Specifies a fast response performance. Faster response generally results in a  0
    smaller rise time.
  1 Normal—Specifies a normal response performance.
   Slow—Specifies a slow response performance. Slower response generally results in less  2   overshoot.

•      Type of Controller —

  Type of Controller specifies which parameters to return as the PID gains.

  0 P—(Default) Specifies to return only the proportional parameters.
  1 PI—Specifies to return the proportional and integral parameters.
  2 PID—Specifies to return the proportional, integral, and derivative parameters.

•      Stimulus signal —

  Stimulus signal specifies an array that represents the stimulus signal.

•      Response signal —

  Response signal specifies an array that represents the response signal.

•      closed-loop? —

  closed-loop? specifies whether the system is a closed-loop system. If you set closed-loop? to
  TRUE, this VI estimates open-loop parameter values based on the closed-loop values it identifies
  from the input signals.

•      dt (s) —

  dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
  zero, this VI uses an internal timer with a one millisecond resolution. The default is 0.

•       Controller Gain (K) —

  Controller Gain (K) specifies an initial value for the controller gain, which this VI uses to
  calculate the integral time (Ti, min) component of PID gains. The default is 0.

•      stimulus operating point —

  stimulus operating point returns the calculated stimulus offset for the plant.

•      response operating point —

                                                   © National Instruments 5769

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5769 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5770 ordinal=5770 -->
## Functions

Functions


           response operating point returns the calculated response offset for the plant.

               •      PID gains —

           PID gains returns the calculated PID gains values for the plant.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


               •      Plant Parameters —

            Plant Parameters returns the calculated gain, time constant, and dead time of the plant.

                     •      Plant Gain (K) —

                Plant Gain (K) returns the calculated process gain (K).

                     •     Time Constant (T) —

              Time Constant (T) returns the calculated time constant (T), in seconds.

                     •     Dead Time (L) —

             Dead Time (L) returns the calculated dead time (L), in seconds.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Autotuning PID Offline.vi

5770   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5770 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5771 ordinal=5771 -->
## Functions

Functions

PIDPID AutotuningAutotuning DesignDesign (Cohen-Coon)(Cohen-Coon) VIVI

Implements autotuning using the tuning method associated with the polymorphic
instance you select. This VI generates PID parameters based on the Stimulus signal
and Response signal you specify. You can use this VI to generate initial parameters
when you do not have sufficient information about the system you want to tune. You
must manually select the polymorphic instance to use.

      Note This instance uses the Cohen-Coon tuning method.


Inputs/Outputs

   •      Type of Controller —

    Type of Controller specifies which parameters to return as the PID gains.

    0 P—(Default) Specifies to return only the proportional parameters.
    1 PI—Specifies to return the proportional and integral parameters.
    2 PID—Specifies to return the proportional, integral, and derivative parameters.

   •      Stimulus signal —

    Stimulus signal specifies an array that represents the stimulus signal.

   •      Response signal —

    Response signal specifies an array that represents the response signal.

   •      closed-loop? —

    closed-loop? specifies whether the system is a closed-loop system. If you set closed-loop? to
    TRUE, this VI estimates open-loop parameter values based on the closed-loop values it identifies
    from the input signals.


                                                    © National Instruments 5771

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5771 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5772 ordinal=5772 -->
## Functions

Functions

               •      dt (s) —

            dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
              zero, this VI uses an internal timer with a one millisecond resolution. The default is 0.

               •       Controller Gain (K) —

             Controller Gain (K) specifies an initial value for the controller gain, which this VI uses to
             calculate the integral time (Ti, min) component of PID gains. The default is 0.

               •      stimulus offset —

            stimulus offset returns the calculated stimulus offset for the plant.

               •      response offset —

           response offset returns the calculated response offset for the plant.

               •      PID gains —

           PID gains returns the calculated PID gains values for the plant.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


               •      Plant Parameters —

            Plant Parameters returns the calculated gain, time constant, and dead time of the plant.

                     •      Plant Gain (K) —

                Plant Gain (K) returns the calculated process gain (K).

                     •     Time Constant (T) —


5772   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5772 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5773 ordinal=5773 -->
## Functions

Functions


       Time Constant (T) returns the calculated time constant (T), in seconds.

         •     Dead Time (L) —

       Dead Time (L) returns the calculated dead time (L), in seconds.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning PID Offline.vi

PIDPID AutotuningAutotuning DesignDesign (Chien-Hrones-Reswick)(Chien-Hrones-Reswick) VIVI

Implements autotuning using the tuning method associated with the polymorphic
instance you select. This VI generates PID parameters based on the Stimulus signal
and Response signal you specify. You can use this VI to generate initial parameters
when you do not have sufficient information about the system you want to tune. You
must manually select the polymorphic instance to use.

      Note This instance uses the Chien-Hrones-Reswick tuning method.


Inputs/Outputs

   •      Tuning specifications —

    Tuning specifications specifies which formula to use to convert the model to PID parameters.


                                                    © National Instruments 5773

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5773 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5774 ordinal=5774 -->
## Functions

Functions


             This input provides formulas for 0% and 20% overshoot.

           0      Regulator - 0%
           1      Regulator - 20%
           2     Servo - 0%
           3     Servo - 20%

               •      Type of Controller —

           Type of Controller specifies which parameters to return as the PID gains.

           0 P—(Default) Specifies to return only the proportional parameters.
           1 PI—Specifies to return the proportional and integral parameters.
           2 PID—Specifies to return the proportional, integral, and derivative parameters.

               •      Stimulus signal —

            Stimulus signal specifies an array that represents the stimulus signal.

               •      Response signal —

           Response signal specifies an array that represents the response signal.

               •      closed-loop? —

            closed-loop? specifies whether the system is a closed-loop system. If you set closed-loop? to
           TRUE, this VI estimates open-loop parameter values based on the closed-loop values it identifies
           from the input signals.

               •      dt (s) —

            dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
              zero, this VI uses an internal timer with a one millisecond resolution. The default is 0.

               •       Controller Gain (K) —

             Controller Gain (K) specifies an initial value for the controller gain, which this VI uses to
             calculate the integral time (Ti, min) component of PID gains. The default is 0.

               •      stimulus offset —

            stimulus offset returns the calculated stimulus offset for the plant.


5774   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5774 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5775 ordinal=5775 -->
## Functions

Functions

   •      response offset —

    response offset returns the calculated response offset for the plant.

   •      PID gains —

    PID gains returns the calculated PID gains values for the plant.

         •      proportional gain (Kc) —

        proportional gain (Kc) returns the proportional gain of the controller.

         •       integral time (Ti, min) —

         integral time (Ti, min) returns the integral time in minutes.

         •       derivative time (Td, min) —

         derivative time (Td, min) returns the derivative time in minutes.


   •      Plant Parameters —

    Plant Parameters returns the calculated gain, time constant, and dead time of the plant.

         •      Plant Gain (K) —

        Plant Gain (K) returns the calculated process gain (K).

         •     Time Constant (T) —

       Time Constant (T) returns the calculated time constant (T), in seconds.

         •     Dead Time (L) —

       Dead Time (L) returns the calculated dead time (L), in seconds.


Examples

Refer to the following example files included with LabVIEW.


                                                    © National Instruments 5775

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5775 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5776 ordinal=5776 -->
## Functions

Functions

            • labview\examples\control\PID\Autotuning PID Offline.vi

      PIDPID AutotuningAutotuning DesignDesign (Internal(Internal ModelModel Control)Control) VIVI

      Implements autotuning using the tuning method associated with the polymorphic
       instance you select. This VI generates PID parameters based on the Stimulus signal
      and Response signal you specify. You can use this VI to generate initial parameters
     when you do not have sufficient information about the system you want to tune. You
      must manually select the polymorphic instance to use.

           Note This instances uses internal model control to estimate the response.


      Inputs/Outputs

               •      Desired Time Constant (tau_c) —

            Desired Time Constant (tau_c) specifies a time constant value at which you want the system to
           perform after you close the loop. This VI uses this value to adjust the PID gains according to the
             internal model control method and as appropriate for a first-order model with delay.

               •      Type of Controller —

           Type of Controller specifies which parameters to return as the PID gains.

           0 P—(Default) Specifies to return only the proportional parameters.
           1 PI—Specifies to return the proportional and integral parameters.
           2 PID—Specifies to return the proportional, integral, and derivative parameters.

               •      Stimulus signal —

            Stimulus signal specifies an array that represents the stimulus signal.

               •      Response signal —

5776   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5776 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5777 ordinal=5777 -->
## Functions

Functions


  Response signal specifies an array that represents the response signal.

•      closed-loop? —

  closed-loop? specifies whether the system is a closed-loop system. If you set closed-loop? to
  TRUE, this VI estimates open-loop parameter values based on the closed-loop values it identifies
  from the input signals.

•      dt (s) —

  dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
  zero, this VI uses an internal timer with a one millisecond resolution. The default is 0.

•       Controller Gain (K) —

  Controller Gain (K) specifies an initial value for the controller gain, which this VI uses to
  calculate the integral time (Ti, min) component of PID gains. The default is 0.

•      stimulus offset —

  stimulus offset returns the calculated stimulus offset for the plant.

•      response offset —

  response offset returns the calculated response offset for the plant.

•      PID gains —

  PID gains returns the calculated PID gains values for the plant.

      •      proportional gain (Kc) —

      proportional gain (Kc) returns the proportional gain of the controller.

      •       integral time (Ti, min) —

       integral time (Ti, min) returns the integral time in minutes.

      •       derivative time (Td, min) —

       derivative time (Td, min) returns the derivative time in minutes.


•      Plant Parameters —


                                                   © National Instruments 5777

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5777 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5778 ordinal=5778 -->
## Functions

Functions


            Plant Parameters returns the calculated gain, time constant, and dead time of the plant.

                     •      Plant Gain (K) —

                Plant Gain (K) returns the calculated process gain (K).

                     •     Time Constant (T) —

              Time Constant (T) returns the calculated time constant (T), in seconds.

                     •     Dead Time (L) —

             Dead Time (L) returns the calculated dead time (L), in seconds.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Autotuning PID Offline.vi

     PIDPID OnlineOnline AutotuningAutotuning

       Controls the parameters of a PID controller based on the autotuning technique of the
      polymorphic instance you select. You can use this VI in applications with other PID VIs,
      such as PID or PID Advanced, to construct and tune a PID controller. You must
      manually select the polymorphic instance to use.


            • PID Online Autotuning (Step Open Loop) VI
            • PID Online Autotuning (Step Closed Loop) VI
            • PID Online Autotuning (Relay Feedback) VI
            • PID Online Autotuning (PID on the loop) VI


5778   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5778 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5779 ordinal=5779 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning PID Online and
   Inline.vi

PIDPID OnlineOnline AutotuningAutotuning (Step(Step OpenOpen Loop)Loop) VIVI

Controls the parameters of a PID controller based on the autotuning technique of the
polymorphic instance you select. You can use this VI in applications with other PID VIs,
such as PID or PID Advanced, to construct and tune a PID controller. You must
manually select the polymorphic instance to use.


Inputs/Outputs

   •      autotuning parameters —

    autotuning parameters specifies various parameters used for the autotuning process.

         •      type of controller —

        type of controller specifies which parameters to return as the output of the tuning process.

        0 P—Specifies to return only the proportional parameters.
        1 PI—Specifies to return the proportional and integral parameters.
        2 PID—Specifies to return the proportional, integral, and derivative parameters.

         •       relay cycles —


                                                    © National Instruments 5779

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5779 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5780 ordinal=5780 -->
## Functions

Functions


                 relay cycles specifies the number of setpoint relay cycles to use to determine the ultimate
                 gain and period. More cycles result in more accurate parameter estimation; however, slower
               systems might require more time for numerous cycles.

                     •       relay amplitude —

                 relay amplitude specifies the amplitude of the setpoint relay action. The setpoint relay is
              between setpoint– relayamplitudeand setpoint+ relayamplitude.

                     •      control specifications —

                 control specification specifies the desired response performance of the PID parameters
               determined by the autotuning process.

               0 normal—Specifies a normal response performance.
                  fast—Specifies a fast response performance. Faster response generally results in a smaller
               1                     rise time.
                 slow—(Default) Specifies a slow response performance. Slower response generally results
               2                    in less overshoot.

                     •     PV noise level —

             PV noise level specifies an estimation of the noise level of the process variable. This value is
               used as the hysteresis for the setpoint relay action.


               •      manipulated variable —

           manipulated variable specifies a quantity or condition to vary as a function of the actuating
             error signal so as to change the value of the directly controlled variable. The manipulated
             variable also can be referred to as the controller output.

               •      setpoint —

            setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

               •      process variable —

            process variable specifies the measured value of the process variable being controlled. This
            value is equal to the feedback value of the feedback control loop.

               •      PID gains in —

5780   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5780 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5781 ordinal=5781 -->
## Functions

Functions


  PID gains in specifies the proportional gain, integral time, and derivative time parameters of the
  controller.

      •      proportional gain (Kc) —

      proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       integral time (Ti, min) —

       integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

      •       derivative time (Td, min) —

       derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


•      dt (s) —

  dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
  zero, this VI uses an internal timer with a one millisecond resolution. The default is –1. Use the
  same dt (s) value as you use for the PID or PID Advanced VI.

•       reinitialize? (F) —

   reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
   error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
  control loop without restarting the entire application. The default is FALSE.

•      autotune? (F) —

  autotune? specifies to begin autotuning. Wire this input from a Boolean control with latched
  mechanical action and a default value of FALSE. The default is FALSE.

•      setpoint out —

  setpoint out returns the updated setpoint value.

•      process variable out —

  process variable out returns the value of the process variable. If autotune? is TRUE, this output
  returns 0.


                                                   © National Instruments 5781

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5781 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5782 ordinal=5782 -->
## Functions

Functions

               •      tuning completed? —

            tuning completed? returns TRUE when the autotuning process is complete. You can use this
           output to determine when to update the PID gains in.

               •      PID gains out —

           PID gains out returns the updated PID gain parameters upon completion of the autotuning
             process. Normal output values are identical to the values in the PID gains in input.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


               •      tuned PID gains —

           tuned PID gains returns the tuned proportional gain, integral time, and derivative time
           parameters of the controller.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


5782   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5782 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5783 ordinal=5783 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning PID Online and
   Inline.vi

PIDPID OnlineOnline AutotuningAutotuning (Step(Step ClosedClosed Loop)Loop) VIVI

Controls the parameters of a PID controller based on the autotuning technique of the
polymorphic instance you select. You can use this VI in applications with other PID VIs,
such as PID or PID Advanced, to construct and tune a PID controller. You must
manually select the polymorphic instance to use.

      Note Use this instance for closed-loop tuning.


Inputs/Outputs

   •      autotuning parameters —

    autotuning parameters specifies various parameters used for the autotuning process.

         •      type of controller —

        type of controller specifies which parameters to return as the output of the tuning process.

        0 P—Specifies to return only the proportional parameters.
        1 PI—Specifies to return the proportional and integral parameters.
        2 PID—Specifies to return the proportional, integral, and derivative parameters.


                                                    © National Instruments 5783

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5783 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5784 ordinal=5784 -->
## Functions

Functions


                     •       relay cycles —

                 relay cycles specifies the number of setpoint relay cycles to use to determine the ultimate
                 gain and period. More cycles result in more accurate parameter estimation; however, slower
               systems might require more time for numerous cycles.

                     •       relay amplitude —

                 relay amplitude specifies the amplitude of the setpoint relay action. The setpoint relay is
              between setpoint– relayamplitudeand setpoint+ relayamplitude.

                     •      control specifications —

                 control specification specifies the desired response performance of the PID parameters
               determined by the autotuning process.

               0 normal—Specifies a normal response performance.
                  fast—Specifies a fast response performance. Faster response generally results in a smaller               1                     rise time.
                 slow—(Default) Specifies a slow response performance. Slower response generally results               2                    in less overshoot.

                     •     PV noise level —

             PV noise level specifies an estimation of the noise level of the process variable. This value is
               used as the hysteresis for the setpoint relay action.


               •      manipulated variable —

           manipulated variable specifies a quantity or condition to vary as a function of the actuating
             error signal so as to change the value of the directly controlled variable. The manipulated
             variable also can be referred to as the controller output.

               •      setpoint —

            setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

               •      process variable —

            process variable specifies the measured value of the process variable being controlled. This
            value is equal to the feedback value of the feedback control loop.


5784   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5784 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5785 ordinal=5785 -->
## Functions

Functions

•      PID gains in —

  PID gains in specifies the proportional gain, integral time, and derivative time parameters of the
  controller.

      •      proportional gain (Kc) —

      proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       integral time (Ti, min) —

       integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

      •       derivative time (Td, min) —

       derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


•      dt (s) —

  dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
  zero, this VI uses an internal timer with a one millisecond resolution. The default is –1. Use the
  same dt (s) value as you use for the PID or PID Advanced VI.

•       reinitialize? (F) —

   reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
   error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
  control loop without restarting the entire application. The default is FALSE.

•      autotune? (F) —

  autotune? specifies to begin autotuning. Wire this input from a Boolean control with latched
  mechanical action and a default value of FALSE. The default is FALSE.

•      setpoint out —

  setpoint out returns the updated setpoint value.

•      process variable out —

  process variable out returns the value of the process variable. If autotune? is TRUE, this output


                                                   © National Instruments 5785

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5785 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5786 ordinal=5786 -->
## Functions

Functions


             returns 0.

               •      tuning completed? —

            tuning completed? returns TRUE when the autotuning process is complete. You can use this
           output to determine when to update the PID gains in.

               •      PID gains out —

           PID gains out returns the updated PID gain parameters upon completion of the autotuning
             process. Normal output values are identical to the values in the PID gains in input.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


               •      tuned PID gains —

           tuned PID gains returns the tuned proportional gain, integral time, and derivative time
           parameters of the controller.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


5786   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5786 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5787 ordinal=5787 -->
## Functions

Functions

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning PID Online and
   Inline.vi

PIDPID OnlineOnline AutotuningAutotuning (Relay(Relay Feedback)Feedback) VIVI

Controls the parameters of a PID controller based on the autotuning technique of the
polymorphic instance you select. You can use this VI in applications with other PID VIs,
such as PID or PID Advanced, to construct and tune a PID controller. You must
manually select the polymorphic instance to use.

      Note Use this instance for relay feedback tuning, which applies an on-off
        relay in a closed-loop test in order to obtain controlled oscillations and
        extract values for ultimate gain and ultimate frequency. This technique also
        incorporates hysteresis to reduce noise.


Inputs/Outputs

   •      autotuning parameters —

    autotuning parameters specifies various parameters used for the autotuning process.

         •      type of controller —

        type of controller specifies which parameters to return as the output of the tuning process.


                                                    © National Instruments 5787

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5787 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5788 ordinal=5788 -->
## Functions

Functions


               0 P—Specifies to return only the proportional parameters.
               1 PI—Specifies to return the proportional and integral parameters.
               2 PID—Specifies to return the proportional, integral, and derivative parameters.

                     •       relay cycles —

                 relay cycles specifies the number of setpoint relay cycles to use to determine the ultimate
                 gain and period. More cycles result in more accurate parameter estimation; however, slower
               systems might require more time for numerous cycles.

                     •       relay amplitude —

                 relay amplitude specifies the amplitude of the setpoint relay action. The setpoint relay is
              between setpoint– relayamplitudeand setpoint+ relayamplitude.

                     •      control specifications —

                 control specification specifies the desired response performance of the PID parameters
               determined by the autotuning process.

               0 normal—Specifies a normal response performance.
                  fast—Specifies a fast response performance. Faster response generally results in a smaller
               1                     rise time.
                 slow—(Default) Specifies a slow response performance. Slower response generally results               2                    in less overshoot.

                     •     PV noise level —

             PV noise level specifies an estimation of the noise level of the process variable. This value is
               used as the hysteresis for the setpoint relay action.


               •      manipulated variable —

           manipulated variable specifies a quantity or condition to vary as a function of the actuating
             error signal so as to change the value of the directly controlled variable. The manipulated
             variable also can be referred to as the controller output.

               •      setpoint —


5788   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5788 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5789 ordinal=5789 -->
## Functions

Functions


  setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

•      process variable —

  process variable specifies the measured value of the process variable being controlled. This
  value is equal to the feedback value of the feedback control loop.

•      PID gains in —

  PID gains in specifies the proportional gain, integral time, and derivative time parameters of the
  controller.

      •      proportional gain (Kc) —

      proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       integral time (Ti, min) —

       integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

      •       derivative time (Td, min) —

       derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


•      dt (s) —

  dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
  zero, this VI uses an internal timer with a one millisecond resolution. The default is –1. Use the
  same dt (s) value as you use for the PID or PID Advanced VI.

•       reinitialize? (F) —

   reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
   error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
  control loop without restarting the entire application. The default is FALSE.

•      autotune? (F) —

  autotune? specifies to begin autotuning. Wire this input from a Boolean control with latched
  mechanical action and a default value of FALSE. The default is FALSE.


                                                   © National Instruments 5789

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5789 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5790 ordinal=5790 -->
## Functions

Functions

               •      setpoint out —

            setpoint out returns the updated setpoint value.

               •      process variable out —

            process variable out returns the value of the process variable. If autotune? is TRUE, this output
             returns 0.

               •      tuning completed? —

            tuning completed? returns TRUE when the autotuning process is complete. You can use this
           output to determine when to update the PID gains in.

               •      PID gains out —

           PID gains out returns the updated PID gain parameters upon completion of the autotuning
             process. Normal output values are identical to the values in the PID gains in input.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


               •      tuned PID gains —

           tuned PID gains returns the tuned proportional gain, integral time, and derivative time
           parameters of the controller.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —


5790   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5790 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5791 ordinal=5791 -->
## Functions

Functions


         integral time (Ti, min) returns the integral time in minutes.

         •       derivative time (Td, min) —

         derivative time (Td, min) returns the derivative time in minutes.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning PID Online and
   Inline.vi

PIDPID OnlineOnline AutotuningAutotuning (PID(PID onon thethe loop)loop) VIVI

Controls the parameters of a PID controller based on the autotuning technique of the
polymorphic instance you select. You can use this VI in applications with other PID VIs,
such as PID or PID Advanced, to construct and tune a PID controller. You must
manually select the polymorphic instance to use.

      Note Use this instance for PID relay tuning, which connects a relay and an
        extra feedback signal with the setpoint and keeps the PID controller in the
       loop with the relay.


Inputs/Outputs

   •      autotuning parameters —

                                                    © National Instruments 5791

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5791 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5792 ordinal=5792 -->
## Functions

Functions


            autotuning parameters specifies various parameters used for the autotuning process.

                     •      type of controller —

               type of controller specifies which parameters to return as the output of the tuning process.

               0 P—Specifies to return only the proportional parameters.
               1 PI—Specifies to return the proportional and integral parameters.
               2 PID—Specifies to return the proportional, integral, and derivative parameters.

                     •       relay cycles —

                 relay cycles specifies the number of setpoint relay cycles to use to determine the ultimate
                 gain and period. More cycles result in more accurate parameter estimation; however, slower
               systems might require more time for numerous cycles.

                     •       relay amplitude —

                 relay amplitude specifies the amplitude of the setpoint relay action. The setpoint relay is
              between setpoint– relayamplitudeand setpoint+ relayamplitude.

                     •      control specifications —

                 control specification specifies the desired response performance of the PID parameters
               determined by the autotuning process.

               0 normal—Specifies a normal response performance.
                  fast—Specifies a fast response performance. Faster response generally results in a smaller               1                     rise time.
                 slow—(Default) Specifies a slow response performance. Slower response generally results
               2
                    in less overshoot.

                     •     PV noise level —

             PV noise level specifies an estimation of the noise level of the process variable. This value is
               used as the hysteresis for the setpoint relay action.


               •      manipulated variable —

           manipulated variable specifies a quantity or condition to vary as a function of the actuating


5792   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5792 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5793 ordinal=5793 -->
## Functions

Functions


  error signal so as to change the value of the directly controlled variable. The manipulated
  variable also can be referred to as the controller output.

•      setpoint —

  setpoint specifies the setpoint value, or desired value, of the process variable being controlled.

•      process variable —

  process variable specifies the measured value of the process variable being controlled. This
  value is equal to the feedback value of the feedback control loop.

•      PID gains in —

  PID gains in specifies the proportional gain, integral time, and derivative time parameters of the
  controller.

      •      proportional gain (Kc) —

      proportional gain (Kc) specifies the proportional gain of the controller. The default is 1.

       In the equation that defines the PID controller, KC represents the proportional gain.

      •       integral time (Ti, min) —

       integral time (Ti, min) specifies the integral time in minutes. The default is 0.01.

      •       derivative time (Td, min) —

       derivative time (Td, min) specifies the derivative time in minutes. The default is 0.


•      dt (s) —

  dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
  zero, this VI uses an internal timer with a one millisecond resolution. The default is –1. Use the
  same dt (s) value as you use for the PID or PID Advanced VI.

•       reinitialize? (F) —

   reinitialize? specifies whether to reinitialize the internal parameters, such as the integrated
   error, of the controller. Set reinitialize? to TRUE if your application must stop and restart the
  control loop without restarting the entire application. The default is FALSE.


                                                   © National Instruments 5793

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5793 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5794 ordinal=5794 -->
## Functions

Functions

               •      autotune? (F) —

           autotune? specifies to begin autotuning. Wire this input from a Boolean control with latched
           mechanical action and a default value of FALSE. The default is FALSE.

               •      setpoint out —

            setpoint out returns the updated setpoint value.

               •      process variable out —

            process variable out returns the value of the process variable. If autotune? is TRUE, this output
             returns 0.

               •      tuning completed? —

            tuning completed? returns TRUE when the autotuning process is complete. You can use this
           output to determine when to update the PID gains in.

               •      PID gains out —

           PID gains out returns the updated PID gain parameters upon completion of the autotuning
             process. Normal output values are identical to the values in the PID gains in input.

                     •      proportional gain (Kc) —

                proportional gain (Kc) returns the proportional gain of the controller.

                     •       integral time (Ti, min) —

                  integral time (Ti, min) returns the integral time in minutes.

                     •       derivative time (Td, min) —

                 derivative time (Td, min) returns the derivative time in minutes.


               •      tuned PID gains —

           tuned PID gains returns the tuned proportional gain, integral time, and derivative time
           parameters of the controller.

                     •      proportional gain (Kc) —


5794   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5794 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5795 ordinal=5795 -->
## Functions

Functions


        proportional gain (Kc) returns the proportional gain of the controller.

         •       integral time (Ti, min) —

         integral time (Ti, min) returns the integral time in minutes.

         •       derivative time (Td, min) —

         derivative time (Td, min) returns the derivative time in minutes.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Autotuning PID Online and
   Inline.vi

PIDPID Lead-LagLead-Lag

Implements a PID controller with a lead/lag function, which is generally used as a
dynamic compensator in feedforward control schemes. This VI uses a positional
algorithm and is an approximation of a true exponential lead/lag. Use the DBL instance
of this VI to implement a single control loop. Use the DBL Array instance to implement
parallel multi-loop control.


  • PID Lead-Lag (DBL) VI
  • PID Lead-Lag (DBL Array) VI

You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of input determines the length of the output
array. Other input arrays do not necessarily need to be the same length as input. This
VI resizes other input arrays to the same length as input as follows:


                                                    © National Instruments 5795

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5795 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5796 ordinal=5796 -->
## Functions

Functions

            •  If the input array is longer than input, the input array is truncated to the length of
           input. Additional values in the array are not used.
            •  If the input array is shorter than input, the last value of the input array is repeated
            until the size matches that of input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Simulation - Cascade and
        Feedforward Surge Tank Level.vi

      PIDPID Lead-LagLead-Lag (DBL)(DBL) VIVI

      Implements a PID controller with a lead/lag function, which is generally used as a
      dynamic compensator in feedforward control schemes. This VI uses a positional
       algorithm and is an approximation of a true exponential lead/lag. Use the DBL instance
       of this VI to implement a single control loop. Use the DBL Array instance to implement
        parallel multi-loop control.


      Inputs/Outputs

               •      time unit —

               •      input —

            input specifies the input value.

               •      tuning parameters —


5796   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5796 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5797 ordinal=5797 -->
## Functions

Functions


  tuning parameters specifies the tuning parameters.

      •      gain —

      gain specifies the DC gain. The default is 1. Setting gain to a negative value produces an
       inverting amplifier with an additional 180-degree phase shift.

      •       lag time —

       lag time specifies the phase lag in minutes. A value of zero turns off the lag.

      •      lead time —

      lead time specifies the phase lead in minutes. A value of zero turns off the lead. Large lead
      time values might result in a wild oscillation of the output.


•      output range —

  output range specifies the range to which to coerce the control output. The default range is –100
  to 100, which corresponds to values specified in terms of percentage of full scale.

  You can change this range to something that is appropriate for your control system. For example,
  you can relate engineering units to engineering units instead of percentage to percentage. This
  VI implements integrator anti-windup when the controller output is saturated at the specified
  minimum or maximum values.

      •      output high —

      output high specifies the maximum value of the controller output. The default is 100.

      •      output low —

      output low specifies the minimum value of the controller output. The default is –100.


•      dt (s) —

  dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
  than or equal to zero, this VI calculates the time since it was last called using an internal timer
  with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
   -1.

•       reinitialize? (F) —

                                                   © National Instruments 5797

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5797 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5798 ordinal=5798 -->
## Functions

Functions


              reinitialize? specifies whether to reinitialize the output to the current input value.

               •      output —

           output returns the control output of the PID algorithm that is applied to the controlled process.

               •      dt out (s) —

            dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
            or the computed interval if you set dt (s) to –1.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of input determines the length of the output
        array. Other input arrays do not necessarily need to be the same length as input. This
        VI resizes other input arrays to the same length as input as follows:

            •  If the input array is longer than input, the input array is truncated to the length of
           input. Additional values in the array are not used.
            •  If the input array is shorter than input, the last value of the input array is repeated
            until the size matches that of input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Simulation - Cascade and
        Feedforward Surge Tank Level.vi

      PIDPID Lead-LagLead-Lag (DBL(DBL Array)Array) VIVI

      Implements a PID controller with a lead/lag function, which is generally used as a
      dynamic compensator in feedforward control schemes. This VI uses a positional
       algorithm and is an approximation of a true exponential lead/lag. Use the DBL instance
       of this VI to implement a single control loop. Use the DBL Array instance to implement

5798   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5798 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5799 ordinal=5799 -->
## Functions

Functions

parallel multi-loop control.


Inputs/Outputs

   •      time unit —

   •      input —

    input specifies the input value.

   •      tuning parameters —

    tuning parameters specifies the tuning parameters.

         •      gain —

        gain specifies the DC gain. The default is 1. Setting gain to a negative value produces an
         inverting amplifier with an additional 180-degree phase shift.

         •       lag time —

         lag time specifies the phase lag in minutes. A value of zero turns off the lag.

         •      lead time —

        lead time specifies the phase lead in minutes. A value of zero turns off the lead. Large lead
        time values might result in a wild oscillation of the output.


   •      output range —

    output range specifies the range to which to coerce the control output. The default range is –100
    to 100, which corresponds to values specified in terms of percentage of full scale.

    You can change this range to something that is appropriate for your control system. For example,
    you can relate engineering units to engineering units instead of percentage to percentage. This


                                                    © National Instruments 5799

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5799 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5800 ordinal=5800 -->
## Functions

Functions


              VI implements integrator anti-windup when the controller output is saturated at the specified
         minimum or maximum values.

                     •      output high —

               output high specifies the maximum value of the controller output. The default is 100.

                     •      output low —

               output low specifies the minimum value of the controller output. The default is –100.


               •      dt (s) —

            dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
           than or equal to zero, this VI calculates the time since it was last called using an internal timer
            with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
                -1.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the output to the current input value.

               •      output —

           output returns the control output of the PID algorithm that is applied to the controlled process.
             This VI determines the length of the output from the size of the input array.

               •      dt out (s) —

            dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
            or the computed interval if you set dt (s) to –1.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of input determines the length of the output
        array. Other input arrays do not necessarily need to be the same length as input. This
        VI resizes other input arrays to the same length as input as follows:

            •  If the input array is longer than input, the input array is truncated to the length of
           input. Additional values in the array are not used.
            •  If the input array is shorter than input, the last value of the input array is repeated

5800   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5800 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5801 ordinal=5801 -->
## Functions

Functions

    until the size matches that of input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Simulation - Cascade and
   Feedforward Surge Tank Level.vi

PIDPID SetpointSetpoint ProfileProfile

Generates setpoint values over time in a control loop for ramp and soak types of
control applications.


Inputs/Outputs

   •      setpoint profile —

    setpoint profile specifies an array of time and setpoint value pairs that define the profile of the
    setpoint as a function of time.

         •      time (s) —

        time (s) specifies the time values in the setpoint profile. Specify the time (s) values in
        ascending order.

         •      setpoint —

         setpoint specifies the setpoint values in the setpoint profile.


   •      dt (s) —

                                                    © National Instruments 5801

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5801 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5802 ordinal=5802 -->
## Functions

Functions


            dt (s) specifies the loop-cycle time, or interval in seconds, at which this VI is called. If dt (s) is less
           than or equal to zero, this VI calculates the time since it was last called using an internal timer
            with 1 ms resolution. If dt (s) must be less than 1 ms, specify the value explicitly. The default is
                -1.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the output to the setpoint profile at time t= 0.

               •      setpoint —

            setpoint specifies the setpoint values in the setpoint profile.

               •       profile complete? —

              profile complete? indicates whether the elapsed time is greater than or equal to the last defined
           time value in the setpoint profile.

               •      elapsed time (s) —

           elapsed time (s) returns the elapsed time, in seconds, since the first call of the VI or since the
               reinitialization of the VI.

               •      dt out (s) —

            dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
            or the computed interval if you set dt (s) to –1.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Simulation - Cascade and
        Feedforward Surge Tank Level.vi

     PIDPID ControlControl InputInput FilterFilter

       Applies a fifth-order lowpass finite impulse response (FIR) filter to the input value.
         Filter cut-off frequency is designed to be 1/10 of the sample frequency of the input
       value. Use this VI to filter measured values, such as the process variable, in control


5802   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5802 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5803 ordinal=5803 -->
## Functions

Functions

applications. Use the DBL instance of this VI to implement a single control loop. Use
the DBL Array instance to implement parallel multi-loop control.

To ensure that the filter does not attenuate useful measurement information, set the
sampling rate of the control system at least 10 times faster than the fastest time
constant of the physical system.


  • PID Control Input Filter (DBL) VI
  • PID Control Input Filter (DBL Array) VI

You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of input determines the length of the output
array. Other input arrays do not necessarily need to be the same length as input. This
VI resizes other input arrays to the same length as input as follows:

  •  If the input array is longer than input, the input array is truncated to the length of
    input. Additional values in the array are not used.
  •  If the input array is shorter than input, the last value of the input array is repeated
    until the size matches that of input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

      Note You also can use Filters PtByPt VIs if the application requires more
         flexible filtering options. Refer to the example VI linked in the following
        section for more information about using these VIs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\PID with Noise Plant.vi


                                                    © National Instruments 5803

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5803 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5804 ordinal=5804 -->
## Functions

Functions

      PIDPID ControlControl InputInput FilterFilter (DBL)(DBL) VIVI

       Applies a fifth-order lowpass finite impulse response (FIR) filter to the input value.
         Filter cut-off frequency is designed to be 1/10 of the sample frequency of the input
       value. Use this VI to filter measured values, such as the process variable, in control
       applications. Use the DBL instance of this VI to implement a single control loop. Use
       the DBL Array instance to implement parallel multi-loop control.

      To ensure that the filter does not attenuate useful measurement information, set the
      sampling rate of the control system at least 10 times faster than the fastest time
       constant of the physical system.


      Inputs/Outputs

               •      input —

            input specifies the unfiltered measured input value.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the output to the current input value.

               •      output —

           output returns the filtered input value.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of input determines the length of the output
        array. Other input arrays do not necessarily need to be the same length as input. This
        VI resizes other input arrays to the same length as input as follows:

            •  If the input array is longer than input, the input array is truncated to the length of
           input. Additional values in the array are not used.
            •  If the input array is shorter than input, the last value of the input array is repeated
            until the size matches that of input.


5804   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5804 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5805 ordinal=5805 -->
## Functions

Functions

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

      Note You also can use Filters PtByPt VIs if the application requires more
         flexible filtering options. Refer to the example VI linked in the following
        section for more information about using these VIs.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\PID with Noise Plant.vi

PIDPID ControlControl InputInput FilterFilter (DBL(DBL Array)Array) VIVI

Applies a fifth-order lowpass finite impulse response (FIR) filter to the input value.
Filter cut-off frequency is designed to be 1/10 of the sample frequency of the input
value. Use this VI to filter measured values, such as the process variable, in control
applications. Use the DBL instance of this VI to implement a single control loop. Use
the DBL Array instance to implement parallel multi-loop control.

To ensure that the filter does not attenuate useful measurement information, set the
sampling rate of the control system at least 10 times faster than the fastest time
constant of the physical system.


Inputs/Outputs

   •      input —

    input specifies the unfiltered measured input value.

   •       reinitialize? (F) —


                                                    © National Instruments 5805

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5805 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5806 ordinal=5806 -->
## Functions

Functions


              reinitialize? specifies whether to reinitialize the output to the current input value.

               •      output —

           output returns the filtered input value. This VI determines the length of the output array from
            the size of the input array.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of input determines the length of the output
        array. Other input arrays do not necessarily need to be the same length as input. This
        VI resizes other input arrays to the same length as input as follows:

            •  If the input array is longer than input, the input array is truncated to the length of
           input. Additional values in the array are not used.
            •  If the input array is shorter than input, the last value of the input array is repeated
            until the size matches that of input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

           Note You also can use Filters PtByPt VIs if the application requires more
                 flexible filtering options. Refer to the example VI linked in the following
               section for more information about using these VIs.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\PID with Noise Plant.vi

     PIDPID OutputOutput RateRate LimiterLimiter

       Limits the rate of change of the controller output. Place this VI immediately after the
      PID VI in your control application. Use the DBL instance of this VI to implement a single
       control loop. Use the DBL Array instance to implement parallel multi-loop control.


5806   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5806 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5807 ordinal=5807 -->
## Functions

Functions


  • PID Output Rate Limiter (DBL) VI
  • PID Output Rate Limiter (DBL Array) VI

Use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of the input (controller output) input determines
the length of the output array. Other input arrays do not necessarily need to be the
same length as the input (controller output) input. This VI resizes other input arrays to
the same length as the input (controller output) input as follows:

  •  If the input array is longer than the input (controller output) input, the input array
     is truncated to the length of the input (controller output) input. Additional values
    in the array are not used.
  •  If the input array is shorter than the input (controller output) input, the last value
    of the input array is repeated until the size matches that of the input (controller
   output) input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\PID with Noise Plant.vi

PIDPID OutputOutput RateRate LimiterLimiter (DBL)(DBL) VIVI

Limits the rate of change of the controller output. Place this VI immediately after the
PID VI in your control application. Use the DBL instance of this VI to implement a single
control loop. Use the DBL Array instance to implement parallel multi-loop control.


                                                    © National Instruments 5807

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5807 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5808 ordinal=5808 -->
## Functions

Functions


      Inputs/Outputs

               •      input (controller output) —

            input (controller output) specifies the current control output value from the PID VI.

               •        initial output —

               initial output specifies the output value on the first call or reinitialization of this VI.

               •      output rate (EGU/min) —

           output rate (EGU/min) specifies the maximum rate of change of the controller output.

               •      dt (s) —

            dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
              zero, this VI uses an internal timer with a one millisecond resolution. The default is –1. Use the
          same dt (s) value as you use for the PID or PID Advanced VI.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the output to the initial output value.

               •      output —

           output returns the current control output with a limited rate change.

               •      dt out (s) —

            dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
            or the computed interval if you set dt (s) to –1.


      Use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the input (controller output) input determines
       the length of the output array. Other input arrays do not necessarily need to be the
     same length as the input (controller output) input. This VI resizes other input arrays to
       the same length as the input (controller output) input as follows:

5808   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5808 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5809 ordinal=5809 -->
## Functions

Functions

  •  If the input array is longer than the input (controller output) input, the input array
     is truncated to the length of the input (controller output) input. Additional values
    in the array are not used.
  •  If the input array is shorter than the input (controller output) input, the last value
    of the input array is repeated until the size matches that of the input (controller
   output) input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\PID with Noise Plant.vi

PIDPID OutputOutput RateRate LimiterLimiter (DBL(DBL Array)Array) VIVI

Limits the rate of change of the controller output. Place this VI immediately after the
PID VI in your control application. Use the DBL instance of this VI to implement a single
control loop. Use the DBL Array instance to implement parallel multi-loop control.


Inputs/Outputs

   •      input (controller output) —

    input (controller output) specifies the current control output value from the PID VI.

   •        initial output —

     initial output specifies the output value on the first call or reinitialization of this VI. This VI
     resizes the initial output input array to match the size of the input (controller output) input


                                                    © National Instruments 5809

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5809 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5810 ordinal=5810 -->
## Functions

Functions


              array.

               •      output rate (EGU/min) —

           output rate (EGU/min) specifies the maximum rate of change of the controller output. This VI
              resizes the output rate (EGU/min) input array to match the size of the input (controller output)
            input array.

               •      dt (s) —

            dt (s) specifies the interval, in seconds, at which this VI is called. If dt (s) is less than or equal to
              zero, this VI uses an internal timer with a one millisecond resolution. The default is –1. Use the
          same dt (s) value as you use for the PID or PID Advanced VI.

               •       reinitialize? (F) —

              reinitialize? specifies whether to reinitialize the output to the initial output value.

               •      output —

           output returns the current control output with a limited rate change. This VI determines the
            length of the output array from the size of the input (controller output) input array.

               •      dt out (s) —

            dt out (s) returns the actual time interval in seconds. dt out (s) returns either the value of dt (s)
            or the computed interval if you set dt (s) to –1.


      Use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the input (controller output) input determines
       the length of the output array. Other input arrays do not necessarily need to be the
     same length as the input (controller output) input. This VI resizes other input arrays to
       the same length as the input (controller output) input as follows:

            •  If the input array is longer than the input (controller output) input, the input array
              is truncated to the length of the input (controller output) input. Additional values
            in the array are not used.
            •  If the input array is shorter than the input (controller output) input, the last value
           of the input array is repeated until the size matches that of the input (controller
          output) input.


5810   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5810 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5811 ordinal=5811 -->
## Functions

Functions

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\PID with Noise Plant.vi

PIDPID EGUEGU toto PercentagePercentage

Converts an engineering-units input to a percent-of-range output based on the
minimum and maximum range settings. Use the DBL instance of this VI to implement a
single control loop. Use the DBL Array instance to implement parallel multi-loop
control.


  • PID EGU to Percentage (DBL) VI
  • PID EGU to Percentage (DBL Array) VI

You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
applications. In this case, the length of the input (EGU) input determines the length of
the output array. Other input arrays do not necessarily need to be the same length as
the input (EGU) input. This VI resizes other input arrays to the same length as the
input (EGU) input as follows:

  •  If the input array is longer than the input (EGU) input, the input array is truncated
    to the length of the input (EGU) input. Additional values in the array are not used.
  •  If the input array is shorter than the input (EGU) input, the last value of the input
    array is repeated until the size matches that of the input (EGU) input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.


                                                    © National Instruments 5811

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5811 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5812 ordinal=5812 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Manual-Automatic Control
        with Engineering Units.vi

      PIDPID EGUEGU toto PercentagePercentage (DBL)(DBL) VIVI

       Converts an engineering-units input to a percent-of-range output based on the
     minimum and maximum range settings. Use the DBL instance of this VI to implement a
       single control loop. Use the DBL Array instance to implement parallel multi-loop
        control.


      Inputs/Outputs

               •     maximum (EGU) —

         maximum (EGU) specifies the input value, in engineering units, corresponding to 100% of the
                full scale.

               •      input (EGU) —

            input (EGU) specifies the input value in engineering units.

               •     minimum (EGU) —

         minimum (EGU) specifies the input value, in engineering units, corresponding to 0% of the full
              scale.

               •   % span —

       % span returns the output value in percentage of full scale.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the input (EGU) input determines the length of

5812   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5812 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5813 ordinal=5813 -->
## Functions

Functions

the output array. Other input arrays do not necessarily need to be the same length as
the input (EGU) input. This VI resizes other input arrays to the same length as the
input (EGU) input as follows:

  •  If the input array is longer than the input (EGU) input, the input array is truncated
    to the length of the input (EGU) input. Additional values in the array are not used.
  •  If the input array is shorter than the input (EGU) input, the last value of the input
    array is repeated until the size matches that of the input (EGU) input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Manual-Automatic Control
   with Engineering Units.vi

PIDPID EGUEGU toto PercentagePercentage (DBL(DBL Array)Array) VIVI

Converts an engineering-units input to a percent-of-range output based on the
minimum and maximum range settings. Use the DBL instance of this VI to implement a
single control loop. Use the DBL Array instance to implement parallel multi-loop
control.


Inputs/Outputs

   •     maximum (EGU) —

   maximum (EGU) specifies the input value, in engineering units, corresponding to 100% of the
      full scale. This VI resizes the maximum (EGU) input array to match the % span input array.

   •      input (EGU) —

                                                    © National Instruments 5813

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5813 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5814 ordinal=5814 -->
## Functions

Functions


            input (EGU) specifies the input value in engineering units.

               •     minimum (EGU) —

         minimum (EGU) specifies the input value, in engineering units, corresponding to 0% of the full
              scale. This VI resizes the minimum (EGU) input array to match the size of the input (EGU) array.

               •   % span —

       % span returns the output value in percentage of full scale. This VI determines the length of the
       % span array from the size of the input (EGU) array.


      You can use the DBL Array instance of this polymorphic VI in multi-loop PID control
       applications. In this case, the length of the input (EGU) input determines the length of
       the output array. Other input arrays do not necessarily need to be the same length as
       the input (EGU) input. This VI resizes other input arrays to the same length as the
       input (EGU) input as follows:

            •  If the input array is longer than the input (EGU) input, the input array is truncated
           to the length of the input (EGU) input. Additional values in the array are not used.
            •  If the input array is shorter than the input (EGU) input, the last value of the input
           array is repeated until the size matches that of the input (EGU) input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Manual-Automatic Control
        with Engineering Units.vi

     PIDPID PercentagePercentage toto EGUEGU

       Converts a percent-of-range input to an engineering-units output based on the
     minimum and maximum range settings. The output is normally limited to the range

5814   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5814 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5815 ordinal=5815 -->
## Functions

Functions

[max...min]. Values outside of the range [max..min] are allowed when coerce output to
range? is FALSE. Use the DBL instance of this VI to implement a single control loop. Use
the DBL Array instance to implement parallel multi-loop control.


  • PID Percentage to EGU (DBL) VI
  • PID Percentage to EGU (DBL Array) VI

The DBL Array instance of this polymorphic VI can be used in multi-loop PID control
applications. In this case, the length of the % span input determines the length of the
output array. Other input arrays do not necessarily need to be the same length as the
% span input. This VI resizes other input arrays to the same length as the % span input
as follows:

  •  If the input array is longer than the % span input, the input array is truncated to
   the length of the % span input. Additional values in the array are not used.
  •  If the input array is shorter than the % span input, the last value of the input array
     is repeated until the size matches that of the % span input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Manual-Automatic Control
   with Engineering Units.vi

PIDPID PercentagePercentage toto EGUEGU (DBL)(DBL) VIVI

Converts a percent-of-range input to an engineering-units output based on the
minimum and maximum range settings. The output is normally limited to the range
[max...min]. Values outside of the range [max..min] are allowed when coerce output to
range? is FALSE. Use the DBL instance of this VI to implement a single control loop. Use

                                                    © National Instruments 5815

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5815 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5816 ordinal=5816 -->
## Functions

Functions

       the DBL Array instance to implement parallel multi-loop control.


      Inputs/Outputs

               •      coerce output to range? (T) —

            coerce output to range? specifies whether to coerce the output to the specified range when %
           span is greater than 100% or less than 0%.

               •     maximum (EGU) —

         maximum (EGU) specifies the input value, in engineering units, corresponding to 100% of the
                full scale.

               •   % span —

       % span specifies the input value in percentage of full scale.

               •     minimum (EGU) —

         minimum (EGU) specifies the input value, in engineering units, corresponding to 0% of the full
              scale.

               •      output (EGU) —

           output (EGU) returns the output value in engineering units.


      The DBL Array instance of this polymorphic VI can be used in multi-loop PID control
       applications. In this case, the length of the % span input determines the length of the
      output array. Other input arrays do not necessarily need to be the same length as the
    % span input. This VI resizes other input arrays to the same length as the % span input
       as follows:

            •  If the input array is longer than the % span input, the input array is truncated to
          the length of the % span input. Additional values in the array are not used.
            •  If the input array is shorter than the % span input, the last value of the input array

5816   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5816 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5817 ordinal=5817 -->
## Functions

Functions

     is repeated until the size matches that of the % span input.

In this manner, an input value that must be used for each output calculation does not
need to be specified repeatedly in the array passed into this VI. Instead, the array can
consist of a single value that is used for each output calculation.

Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\control\PID\Manual-Automatic Control
   with Engineering Units.vi

PIDPID PercentagePercentage toto EGUEGU (DBL(DBL Array)Array) VIVI

Converts a percent-of-range input to an engineering-units output based on the
minimum and maximum range settings. The output is normally limited to the range
[max...min]. Values outside of the range [max..min] are allowed when coerce output to
range? is FALSE. Use the DBL instance of this VI to implement a single control loop. Use
the DBL Array instance to implement parallel multi-loop control.


Inputs/Outputs

   •      coerce output to range? (T) —

    coerce output to range? specifies whether to coerce the output to the specified range when %
    span is greater than 100% or less than 0%.

   •     maximum (EGU) —

   maximum (EGU) specifies the input value, in engineering units, corresponding to 100% of the
      full scale. This VI resizes the maximum (EGU) input array to match the % span input array.

   •   % span —


                                                    © National Instruments 5817

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5817 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5818 ordinal=5818 -->
## Functions

Functions


       % span specifies the input value in percentage of full scale.

               •     minimum (EGU) —

         minimum (EGU) specifies the input value, in engineering units, corresponding to 0% of the full
              scale. This VI resizes the minimum (EGU) input array to match the % span input array.

               •      output (EGU) —

           output (EGU) returns the output value in engineering units. This VI determines the length of the
           output (EGU) array from the size of the % span input array.


      The DBL Array instance of this polymorphic VI can be used in multi-loop PID control
       applications. In this case, the length of the % span input determines the length of the
      output array. Other input arrays do not necessarily need to be the same length as the
    % span input. This VI resizes other input arrays to the same length as the % span input
       as follows:

            •  If the input array is longer than the % span input, the input array is truncated to
          the length of the % span input. Additional values in the array are not used.
            •  If the input array is shorter than the % span input, the last value of the input array
              is repeated until the size matches that of the % span input.

        In this manner, an input value that must be used for each output calculation does not
      need to be specified repeatedly in the array passed into this VI. Instead, the array can
       consist of a single value that is used for each output calculation.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\PID\Manual-Automatic Control
        with Engineering Units.vi

     FuzzyFuzzy LogicLogic

      Use the Fuzzy Logic VIs to design and control fuzzy systems. You also can use the Fuzzy
      System Designer to design fuzzy systems interactively. You can use fuzzy logic to

5818   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5818 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5819 ordinal=5819 -->
## Functions

Functions

implement rule-based control for systems requiring control with multiple inputs.

The VIs on this palette can return general LabVIEW error codes and specific PID and
Fuzzy Logic error codes.


 Palette              Description Object

 FL Fuzzy
            Implements a fuzzy logic controller for the fuzzy system you specify. Controller


 FL Save      Saves a fuzzy system to a .fs file. You can use the FL Load Fuzzy System VI to load
 Fuzzy        the .fs file you save. You also can load and save .fs  files in the Fuzzy System
 System       Designer.


 FL Load     Loads a fuzzy system from a .fs file. Use the FL Save Fuzzy System VI to save the
 Fuzzy      .fs file after you make any modifications. You also can load and save .fs files in the
 System      Fuzzy System Designer.


 FL New              Creates a fuzzy system. You also can use the Fuzzy System Designer to create fuzzy
 Fuzzy             systems interactively. System


            Use the Variables VIs to modify the linguistic variables in a fuzzy system. Linguistic
 Variables     variables represent, in words, the input variables and output variables of the system
            you want to control.


            Use the Membership VIs to modify the membership functions for linguistic variables
                in a fuzzy system. Membership functions represent the degree of membership of
 Membership
                 linguistic variables within their linguistic terms. The degree of membership is
             continuous between 0 and 1.


                                                    © National Instruments 5819

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5819 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5820 ordinal=5820 -->
## Functions

Functions


         Palette                      Description
        Object

                   Use the Rules VIs to modify the rules for a fuzzy system. Rules describe, in words, the
         Rules         relationships between input and output linguistic variables based on their linguistic
                      terms.


     FLFL FuzzyFuzzy ControllerController

      Implements a fuzzy logic controller for the fuzzy system you specify.

      By default, this VI implements a fuzzy logic controller for a single-input single-output
       (SISO) fuzzy system. You must manually select the polymorphic instance you want to
       use.


            • FL Fuzzy Controller (SISO) VI
            • FL Fuzzy Controller (SIMO) VI
            • FL Fuzzy Controller (MISO) VI
            • FL Fuzzy Controller (MIMO) VI

      FLFL FuzzyFuzzy ControllerController (SISO)(SISO) VIVI

      Implements a fuzzy logic controller for the fuzzy system you specify.

      By default, this VI implements a fuzzy logic controller for a single-input single-output
       (SISO) fuzzy system. You must manually select the polymorphic instance you want to
       use.


5820   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5820 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5821 ordinal=5821 -->
## Functions

Functions

Inputs/Outputs

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
    output from another VI to the fuzzy system in input of this VI.

   •      input value —

    input value specifies the value of the input variable in the fuzzy system. The fuzzy logic
     controller evaluates the output value(s) according to the input value and the rules of the fuzzy
    system.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      rule-invoked value? —

    rule-invoked value? indicates whether the fuzzy logic controller invoked a rule to evaluate the
    corresponding output value. output value is zero either if the fuzzy controller evaluates the
    output variable to zero based on the input value(s) and the rules of the fuzzy system or if the
    fuzzy logic controller does not invoke any rule to evaluate the output variable. rule-invoked
    value? indicates, when FALSE, that the rule base is incomplete.

   •      fuzzy system out —

    fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
    fuzzy system in input of another VI.

   •      output value —

    output value returns the value of the output variable in the fuzzy system. The fuzzy logic
     controller evaluates the output value according to the input value(s) and the rules of the fuzzy
    system. If output value is zero, use the rule-invoked value? indicator to determine whether the
    fuzzy controller evaluated the corresponding output variable to zero or if the fuzzy logic
     controller did not invoke any rule to evaluate the output variable.

   •       rule weights —

    rule weights returns the rule weights that the fuzzy logic controller uses to scale the
    membership functions of the output linguistic variables. The implication method specifies how
    the fuzzy logic controller performs this scaling. For each rule, the rule weight is the truth value of


                                                    © National Instruments 5821

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5821 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5822 ordinal=5822 -->
## Functions

Functions


            the aggregated antecedent multiplied by the degree of support you specify for the rule.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL FuzzyFuzzy ControllerController (SIMO)(SIMO) VIVI

      Implements a fuzzy logic controller for the fuzzy system you specify.

      By default, this VI implements a fuzzy logic controller for a single-input single-output
       (SISO) fuzzy system. You must manually select the polymorphic instance you want to
       use.


      Inputs/Outputs

               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •      input value —

            input value specifies the value of the input variable in the fuzzy system. The fuzzy logic
             controller evaluates the output value(s) according to the input value and the rules of the fuzzy
            system.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      rule-invoked values? —


5822   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5822 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5823 ordinal=5823 -->
## Functions

Functions


    rule-invoked values? indicates whether the fuzzy logic controller invoked a rule to evaluate the
    corresponding output values. An element of the output values array is zero either if the fuzzy
     controller evaluates the corresponding output variable to zero based on the input value(s) and
    the rules of the fuzzy system or if the fuzzy logic controller does not invoke any rule to evaluate
    the output variable. rule-invoked values? indicates, when FALSE, that the rule base is
    incomplete.

   •      fuzzy system out —

    fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
    fuzzy system in input of another VI.

   •      output values —

    output values returns the values of the output variables in the fuzzy system. The fuzzy logic
     controller evaluates the output values according to the input value(s) and the rules of the fuzzy
    system. If an element of the output values array is zero, use the rule-invoked values? indicator
    to determine whether the fuzzy controller evaluated the corresponding output variable to zero
    or if the fuzzy logic controller did not invoke any rule to evaluate the output variable.

   •       rule weights —

    rule weights returns the rule weights that the fuzzy logic controller uses to scale the
    membership functions of the output linguistic variables. The implication method specifies how
    the fuzzy logic controller performs this scaling. For each rule, the rule weight is the truth value of
    the aggregated antecedent multiplied by the degree of support you specify for the rule.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FLFL FuzzyFuzzy ControllerController (MISO)(MISO) VIVI

Implements a fuzzy logic controller for the fuzzy system you specify.

By default, this VI implements a fuzzy logic controller for a single-input single-output
(SISO) fuzzy system. You must manually select the polymorphic instance you want to
use.


                                                    © National Instruments 5823

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5823 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5824 ordinal=5824 -->
## Functions

Functions


      Inputs/Outputs

               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •      input values —

            input values specifies the values of the input variables in the fuzzy system. The fuzzy logic
             controller evaluates the output value(s) according to the input values and the rules of the fuzzy
            system.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      rule-invoked value? —

            rule-invoked value? indicates whether the fuzzy logic controller invoked a rule to evaluate the
            corresponding output value. output value is zero either if the fuzzy controller evaluates the
           output variable to zero based on the input value(s) and the rules of the fuzzy system or if the
             fuzzy logic controller does not invoke any rule to evaluate the output variable. rule-invoked
            value? indicates, when FALSE, that the rule base is incomplete.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •      output value —

           output value returns the value of the output variable in the fuzzy system. The fuzzy logic
             controller evaluates the output value according to the input value(s) and the rules of the fuzzy
            system. If output value is zero, use the rule-invoked value? indicator to determine whether the
             fuzzy controller evaluated the corresponding output variable to zero or if the fuzzy logic
             controller did not invoke any rule to evaluate the output variable.

               •       rule weights —

5824   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5824 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5825 ordinal=5825 -->
## Functions

Functions


    rule weights returns the rule weights that the fuzzy logic controller uses to scale the
    membership functions of the output linguistic variables. The implication method specifies how
    the fuzzy logic controller performs this scaling. For each rule, the rule weight is the truth value of
    the aggregated antecedent multiplied by the degree of support you specify for the rule.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FLFL FuzzyFuzzy ControllerController (MIMO)(MIMO) VIVI

Implements a fuzzy logic controller for the fuzzy system you specify.

By default, this VI implements a fuzzy logic controller for a single-input single-output
(SISO) fuzzy system. You must manually select the polymorphic instance you want to
use.


Inputs/Outputs

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
    output from another VI to the fuzzy system in input of this VI.

   •      input values —

    input values specifies the values of the input variables in the fuzzy system. The fuzzy logic
     controller evaluates the output value(s) according to the input values and the rules of the fuzzy
    system.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 5825

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5825 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5826 ordinal=5826 -->
## Functions

Functions

               •      rule-invoked values? —

            rule-invoked values? indicates whether the fuzzy logic controller invoked a rule to evaluate the
            corresponding output values. An element of the output values array is zero either if the fuzzy
             controller evaluates the corresponding output variable to zero based on the input value(s) and
            the rules of the fuzzy system or if the fuzzy logic controller does not invoke any rule to evaluate
            the output variable. rule-invoked values? indicates, when FALSE, that the rule base is
            incomplete.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •      output values —

           output values returns the values of the output variables in the fuzzy system. The fuzzy logic
             controller evaluates the output values according to the input value(s) and the rules of the fuzzy
            system. If an element of the output values array is zero, use the rule-invoked values? indicator
             to determine whether the fuzzy controller evaluated the corresponding output variable to zero
            or if the fuzzy logic controller did not invoke any rule to evaluate the output variable.

               •       rule weights —

             rule weights returns the rule weights that the fuzzy logic controller uses to scale the
          membership functions of the output linguistic variables. The implication method specifies how
            the fuzzy logic controller performs this scaling. For each rule, the rule weight is the truth value of
            the aggregated antecedent multiplied by the degree of support you specify for the rule.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     FLFL SaveSave FuzzyFuzzy SystemSystem

      Saves a fuzzy system to a .fs file. You can use the FL Load Fuzzy System VI to load the
     .fs file you save. You also can load and save .fs  files in the Fuzzy System Designer.


5826   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5826 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5827 ordinal=5827 -->
## Functions

Functions

Inputs/Outputs

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
    output from another VI to the fuzzy system in input of this VI.

   •        file path —

      file path specifies the path to the .fs  file. You must specify an absolute path. If you specify an
    empty or relative path, this VI returns an error.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      fuzzy system out —

    fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
    fuzzy system in input of another VI.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

FLFL LoadLoad FuzzyFuzzy SystemSystem

Loads a fuzzy system from a .fs file. Use the FL Save Fuzzy System VI to save the .fs
file after you make any modifications. You also can load and save .fs files in the Fuzzy
System Designer.


Inputs/Outputs

   •        file path —

      file path specifies the path to the .fs  file. You must specify an absolute path. If you specify an


                                                    © National Instruments 5827

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5827 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5828 ordinal=5828 -->
## Functions

Functions


          empty or relative path, this VI returns an error.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

     FLFL NewNew FuzzyFuzzy SystemSystem

       Creates a fuzzy system. You also can use the Fuzzy System Designer to create fuzzy
      systems interactively.


      Inputs/Outputs

               •       defuzzification method —

             defuzzification method specifies the defuzzification method this VI uses to convert the degrees
             of membership of output linguistic variables into numerical values.

           0 Center of Area—Specifies to use the Center of Area defuzzification method.
           1 Modified Center of Area—Specifies to use the modified Center of Area defuzzification method.
           2 Center of Sums—Specifies to use the Center of Sums defuzzification method.
           3 Center of Maximum—Specifies to use the Center of Maximum defuzzification method.


5828   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5828 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5829 ordinal=5829 -->
## Functions

Functions


  4 Mean of Maximum—Specifies to use the Mean of Maximum defuzzification method.

•      input variables —

  input variables specifies the input linguistic variables for the fuzzy system.

      •     name —

     name specifies the name of the linguistic variable.

      •      range —

      range specifies the minimum and maximum values of the linguistic variable.

      •     membership functions —

     membership functions specifies the linguistic terms for the linguistic variable and the
      degree of membership of the linguistic variable within those linguistic terms. Each element
       of the membership functions array corresponds to a linguistic term.

             •     name —

        name specifies the name of the membership function, or linguistic term, you want to
           modify.

             •      shape —

         shape specifies the shape of the function that determines the degrees of membership
            for the linguistic variable.

             •      points —

           points specifies the values of the linguistic variable corresponding to the base and top
            points, in order from left to right and base to top, of the membership function. The
          degree of membership of the linguistic variable within the linguistic term name is 0 at
          the base points and 1 at the top points. Specify one point for a singleton function, three
           points for a triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-
           defined functions.

             •       color —


                                                   © National Instruments 5829

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5829 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5830 ordinal=5830 -->
## Functions

Functions


                     color specifies the color of the membership function when you view the membership
                     function in the Fuzzy System Designer. You can wire a color box constant to this input.

                           •      user-defined shape index —

                     user-defined shape index specifies the index of the user-defined shape that
                    determines the degrees of membership for the linguistic variable. This parameter is
                     applicable only if you set shape to User-Defined. Define the user-defined shapes in the
                     user-defined membership function shapes array in both the FL New Fuzzy System VI
                 and the User-Defined instance of the FL Create Membership Function VI.


               •      output variables —

           output variables specifies the output linguistic variables for the fuzzy system.

                     •     name —

            name specifies the name of the linguistic variable.

                     •      range —

               range specifies the minimum and maximum values of the linguistic variable.

                     •     membership functions —

              membership functions specifies the linguistic terms for the linguistic variable and the
               degree of membership of the linguistic variable within those linguistic terms. Each element
                  of the membership functions array corresponds to a linguistic term.

                           •     name —

               name specifies the name of the membership function, or linguistic term, you want to
                     modify.

                           •      shape —


5830   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5830 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5831 ordinal=5831 -->
## Functions

Functions


         shape specifies the shape of the function that determines the degrees of membership
            for the linguistic variable.

             •      points —

           points specifies the values of the linguistic variable corresponding to the base and top
            points, in order from left to right and base to top, of the membership function. The
          degree of membership of the linguistic variable within the linguistic term name is 0 at
          the base points and 1 at the top points. Specify one point for a singleton function, three
           points for a triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-
           defined functions.

             •       color —

           color specifies the color of the membership function when you view the membership
           function in the Fuzzy System Designer. You can wire a color box constant to this input.

             •      user-defined shape index —

           user-defined shape index specifies the index of the user-defined shape that
          determines the degrees of membership for the linguistic variable. This parameter is
           applicable only if you set shape to User-Defined. Define the user-defined shapes in the
           user-defined membership function shapes array in both the FL New Fuzzy System VI
         and the User-Defined instance of the FL Create Membership Function VI.


•       rules —

  rules specifies the rules for the fuzzy system. Use the input variables and output variables to
  form the antecedents and consequents, respectively, of the rules.

      •      antecedents —

      antecedents specifies the antecedents, or IF portions, of the rule. Each antecedent consists
       of three parts: the index of an input linguistic variable, an operator that specifies whether to
       calculate the degree of membership or the degree of non-membership of the input
        linguistic variable within a linguistic term, and the index of the linguistic term. The indexes
      correspond to the order in which the variables or linguistic terms were created.


                                                   © National Instruments 5831

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5831 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5832 ordinal=5832 -->
## Functions

Functions


                           •      Var Index —

                  The index of an input linguistic variable.

                           •     MF Index —

                  The index of the linguistic term.

                           •     Cond —

                 An operator that specifies whether to calculate the degree of membership or the
                   degree of non-membership of the linguistic variable within a linguistic term.


                     •      antecedent connective —

               antecedent connective specifies how this VI calculates the truth value of the aggregated
                  rule antecedent.

                     •      consequents —

               consequents specifies the consequents, or THEN portions, of the rule. Each consequent
                  consists of three parts: the index of an output linguistic variable, an operator that specifies
               whether to calculate the degree of membership or the degree of non-membership of the
               output linguistic variable within a linguistic term, and the index of the linguistic term. The
                indexes correspond to the order in which the variables or linguistic terms were created.

                           •      Var Index —

                  The index of an output linguistic variable.

                           •     MF Index —

                  The index of the linguistic term.

                           •     Cond —

                 An operator that specifies whether to calculate the degree of membership or the
                   degree of non-membership of the linguistic variable within a linguistic term.


                     •      consequent implication —


5832   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5832 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5833 ordinal=5833 -->
## Functions

Functions


      consequent implication specifies the implication method this VI uses to scale the
     membership functions of the output linguistic variable based on the rule weight.

      •      degree of support —

      degree of support specifies the weight, between 0 and 1, that you want to apply to the rule.
     The default is 1. Multiply the degree of support by the truth value of the aggregated rule
      antecedent to calculate the rule weight.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      user-defined membership function shapes —

  user-defined membership function shapes specifies the x-y values of points that define custom
  shapes for membership functions. The shape of a membership function determines the degrees
  of membership for a linguistic variable within the corresponding linguistic term. When you use
  the FL Create Membership Function VI to create a new membership function, you can use
  predefined membership function shapes, or you can use a custom membership function shape
  that you specify with this parameter.

  For each custom membership function shape you define, you can use any range of x-values.
  However, the range of the y-values must be between 0 and 1 such that the first point you specify
  has a degree of membership of 0 and the last point you specify has a degree of membership of 1.
  LabVIEW scales the custom shape linearly between the left base and left top points and scales
  the mirror image of this shape linearly between the right top and right base points. Any points
  between left top and right top have a degree of membership of 1.

      •      Y —

      •     X —


•      description —

  description specifies a description for the fuzzy system.

•      fuzzy system out —


                                                   © National Instruments 5833

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5833 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5834 ordinal=5834 -->
## Functions

Functions


            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

      VariablesVariables

      Use the Variables VIs to modify the linguistic variables in a fuzzy system. Linguistic
       variables represent, in words, the input variables and output variables of the system
      you want to control.

      The VIs on this palette can return general LabVIEW error codes and specific PID and
       Fuzzy Logic error codes.


         Palette                       Description        Object

        FL Create      Creates a linguistic variable for a fuzzy system. You also can use the Variables page
         Variable        of the Fuzzy System Designer to create linguistic variables interactively.


        FL Get         Returns the name, range, and membership functions for a linguistic variable in a
         Variable VI     fuzzy system.


        FL Set         Modifies the name, range, or membership functions of a linguistic variable in a
         Variable VI     fuzzy system.

        FL Get
       Number of     Returns the number of input and output variables in the fuzzy system you specify.
         Variables


5834   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5834 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5835 ordinal=5835 -->
## Functions

Functions


 Palette               Description
 Object

 FL Get               Returns the names of the input and output variables in the fuzzy system you Variable                  specify. Names


 FL Plot         Plots a specific input or output variable that is in a fuzzy system with the
 Variable VI    membership functions of that variable.


FLFL CreateCreate VariableVariable

Creates a linguistic variable for a fuzzy system. You also can use the Variables page of
the Fuzzy System Designer to create linguistic variables interactively.


Inputs/Outputs

   •     name —

   name specifies the name of the linguistic variable.

   •     minimum —

   minimum specifies the minimum value of the linguistic variable.

   •     maximum —

   maximum specifies the maximum value of the linguistic variable.

   •     membership functions —

    membership functions specifies the membership functions for the linguistic variable.


                                                    © National Instruments 5835

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5835 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5836 ordinal=5836 -->
## Functions

Functions


                     •     name —

            name specifies the name of the membership function, or linguistic term, you want to
                modify.

                     •      shape —

              shape specifies the shape of the function that determines the degrees of membership for
                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       variable —

             variable returns the linguistic variable with the name, range, and membership functions you
              specify.


5836   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5836 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5837 ordinal=5837 -->
## Functions

Functions


•     name —

  name specifies the name of the linguistic variable.

•      range —

  range specifies the minimum and maximum values of the linguistic variable.

•     membership functions —

  membership functions specifies the linguistic terms for the linguistic variable and the
  degree of membership of the linguistic variable within those linguistic terms. Each element
  of the membership functions array corresponds to a linguistic term.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to
      modify.

      •      shape —

      shape specifies the shape of the function that determines the degrees of membership
       for the linguistic variable.

      •      points —

      points specifies the values of the linguistic variable corresponding to the base and top
       points, in order from left to right and base to top, of the membership function. The
      degree of membership of the linguistic variable within the linguistic term name is 0 at
      the base points and 1 at the top points. Specify one point for a singleton function, three
       points for a triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-
      defined functions.

      •       color —

       color specifies the color of the membership function when you view the membership
       function in the Fuzzy System Designer. You can wire a color box constant to this input.

      •      user-defined shape index —

      user-defined shape index specifies the index of the user-defined shape that


                                                © National Instruments 5837

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5837 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5838 ordinal=5838 -->
## Functions

Functions


                    determines the degrees of membership for the linguistic variable. This parameter is
                     applicable only if you set shape to User-Defined. Define the user-defined shapes in the
                     user-defined membership function shapes array in both the FL New Fuzzy System VI
                 and the User-Defined instance of the FL Create Membership Function VI.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL GetGet VariableVariable VIVI

       Returns the name, range, and membership functions for a linguistic variable in a fuzzy
       system.


      Inputs/Outputs

               •       variable index —

             variable index specifies the index of the linguistic variable whose information you want to
             return. variable index corresponds to the order in which the linguistic variable was created.

               •      input/output —

            input/output specifies whether the linguistic variable corresponding to variable index is an
            input or output variable.

           0 Input—Specifies that the linguistic variable corresponding to variable index is an input


5838   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5838 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5839 ordinal=5839 -->
## Functions

Functions


    variable.
   Output—Specifies that the linguistic variable corresponding to variable index is an output  1    variable.

•      fuzzy system in —

  fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
  output from another VI to the fuzzy system in input of this VI.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      fuzzy system out —

  fuzzy system out returns the complete information for a fuzzy system. Wire the fuzzy system out
  output of this VI to the fuzzy system in input of another VI.

•     name —

  name returns the name of the linguistic variable.

•     minimum —

  minimum returns the minimum value of the linguistic variable.

•     maximum —

  maximum returns the maximum value of the linguistic variable.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•     membership functions —

  membership functions returns the membership functions for the linguistic variable.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to


                                                   © National Instruments 5839

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5839 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5840 ordinal=5840 -->
## Functions

Functions


                modify.

                     •      shape —

              shape specifies the shape of the function that determines the degrees of membership for
                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


      FLFL SetSet VariableVariable VIVI

       Modifies the name, range, or membership functions of a linguistic variable in a fuzzy
       system.


5840   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5840 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5841 ordinal=5841 -->
## Functions

Functions


Inputs/Outputs

   •       variable index —

    variable index specifies the index of the linguistic variable whose information you want to
    modify. variable index corresponds to the order in which the linguistic variable was created.

   •      input/output —

    input/output specifies whether the linguistic variable corresponding to variable index is an
    input or output variable.

     Input—Specifies that the linguistic variable corresponding to variable index is an input
    0      variable.
     Output—Specifies that the linguistic variable corresponding to variable index is an output
    1      variable.

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
    output from another VI to the fuzzy system in input of this VI.

   •     name —

   •     minimum —

   minimum specifies the minimum value of the linguistic variable.

   •     maximum —

   maximum specifies the maximum value of the linguistic variable.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.


                                                    © National Instruments 5841

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5841 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5842 ordinal=5842 -->
## Functions

Functions

               •     membership functions —

          membership functions specifies the membership functions for the linguistic variable.

                     •     name —

            name specifies the name of the membership function, or linguistic term, you want to
                modify.

                     •      shape —

              shape specifies the shape of the function that determines the degrees of membership for
                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire the fuzzy system out
           output of this VI to the fuzzy system in input of another VI.

               •       error out —


5842   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5842 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5843 ordinal=5843 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.


FLFL GetGet NumberNumber ofof VariablesVariables

Returns the number of input and output variables in the fuzzy system you specify.


Inputs/Outputs

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
    output from another VI to the fuzzy system in input of this VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      fuzzy system out —

    fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
    fuzzy system in input of another VI.

   •     number of input variables —

   number of input variables returns the number of input variables in the fuzzy system.

   •     number of output variables —

   number of output variables returns the number of output variables in the fuzzy system.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5843

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5843 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5844 ordinal=5844 -->
## Functions

Functions

      FLFL GetGet VariableVariable NamesNames

       Returns the names of the input and output variables in the fuzzy system you specify.


      Inputs/Outputs

               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •      input variable names —

            input variable names returns the names of the input variables in the fuzzy system.

               •      output variable names —

           output variable names returns the names of the output variables in the fuzzy system.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL PlotPlot VariableVariable VIVI

       Plots a specific input or output variable that is in a fuzzy system with the membership
       functions of that variable.

5844   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5844 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5845 ordinal=5845 -->
## Functions

Functions


Inputs/Outputs

   •       variable index —

   •      input/output —

    input/output specifies whether the linguistic variable corresponding to variable index is an
    input or output variable.

     Input—Specifies that the linguistic variable corresponding to variable index is an input    0      variable.
     Output—Specifies that the linguistic variable corresponding to variable index is an output    1      variable.

   •      fuzzy system in —

    The Fuzzy Set datatype contains all information related to the Fuzzy controller here specified.

   •      graph refnum —

   •       error in (no error) —

    error in can accept error information wired from VIs previously called. Use this information to
    decide if any functionality should be bypassed in the event of errors from other VIs. Right-click
    the error in control on the front panel and select Explain Error or Explain Warning from the
    shortcut menu for more information about the error.

   •      fuzzy system out —

    The Fuzzy Set datatype contains all information related to the Fuzzy controller here specified.

   •     membership functions plot —

   •       error out —

    error out passes error or warning information out of a VI to be used by other VIs. Right-click the
    error out indicator on the front panel and select Explain Error or Explain Warning from the


                                                    © National Instruments 5845

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5845 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5846 ordinal=5846 -->
## Functions

Functions


            shortcut menu for more information about the error.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\control\fuzzy\Dynamic greenhouse
        controller\FuzzyEx Dynamic Fuzzy Controller for a
        greenhouse.vi

     MembershipMembership

      Use the Membership VIs to modify the membership functions for linguistic variables in
      a fuzzy system. Membership functions represent the degree of membership of
        linguistic variables within their linguistic terms. The degree of membership is
       continuous between 0 and 1.

      The VIs on this palette can return general LabVIEW error codes and specific PID and
       Fuzzy Logic error codes.


         Palette                      Description
        Object

        FL Create
                      Creates a membership function for a linguistic variable. You also can use the Define
        Membership
                       Variable dialog box to create membership functions interactively.
         Function


                     Returns the shape, color, and points of a membership function for a linguistic
        FL Get
                         variable. You can return a membership function from a fuzzy system or from an array
        Membership
                        of membership functions. The data type you wire to the fuzzy system in input
         Function VI
                     determines the polymorphic instance to use.


5846   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5846 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5847 ordinal=5847 -->
## Functions

Functions


 Palette              Description
 Object

              Modifies the shape, color, or points of a membership function for a linguistic variable. FL Set            You can modify a membership function from a fuzzy system or from an array of Membership            membership functions. The data type you wire to the fuzzy system in input Function VI
             determines the polymorphic instance to use.

 FL Get
 Number of   Returns the number of membership functions for all input and output variables in
 Membership the fuzzy system you specify.
 Functions

             Returns the names of the linguistic terms for a linguistic variable. Membership
 FL Get              functions represent the degree of membership of linguistic variables within their Membership                 linguistic terms. You can return the names of the membership functions from a fuzzy
 Function             system or from an array of membership functions. The data type you wire to the Names VI              fuzzy system in input determines the polymorphic instance to use.


FLFL CreateCreate MembershipMembership FunctionFunction

Creates a membership function for a linguistic variable. You also can use the Define
Variable dialog box to create membership functions interactively.

By default, this VI uses a triangle function to determine the degrees of membership for
the linguistic variable. You must manually select the polymorphic instance you want to
use.


  • FL Create Membership Function (Triangle) VI
  • FL Create Membership Function (Trapezoid) VI
  • FL Create Membership Function (Singleton) VI
  • FL Create Membership Function (Sigmoid) VI
  • FL Create Membership Function (Gaussian) VI
  • FL Create Membership Function (User-Defined) VI


                                                    © National Instruments 5847

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5847 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5848 ordinal=5848 -->
## Functions

Functions

   FLFL CreateCreate MembershipMembership FunctionFunction (Triangle)(Triangle) VIVI

       Creates a membership function for a linguistic variable. You also can use the Define
       Variable dialog box to create membership functions interactively.

      By default, this VI uses a triangle function to determine the degrees of membership for
       the linguistic variable. You must manually select the polymorphic instance you want to
       use.


      Inputs/Outputs

               •     name —

         name specifies the name of the membership function, or linguistic term, you want to create.

               •        left base —

               left base specifies the numerical value of the linguistic variable corresponding to the left base
            point of the membership function. The degree of membership of the linguistic variable within
            the linguistic term name is 0 at the left base value.

               •      top —

           top specifies the numerical value of the linguistic variable corresponding to the top of the
              triangle membership function. The degree of membership of the linguistic variable within the
              linguistic term name is 1 at the top value.

               •       right base —

             right base specifies the numerical value of the linguistic variable corresponding to the right base
            point of the membership function. The degree of membership of the linguistic variable within
            the linguistic term name is 0 at the right base value.

               •       error in (no error) —


5848   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5848 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5849 ordinal=5849 -->
## Functions

Functions


  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       color —

  color specifies the color of the membership function when you view the membership function in
  the Fuzzy System Designer. You can wire a color box constant to this input.

•     membership function —

  membership function returns the membership function with the shape, points, and color you
  specify.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to
      modify.

      •      shape —

      shape specifies the shape of the function that determines the degrees of membership for
      the linguistic variable.

      •      points —

      points specifies the values of the linguistic variable corresponding to the base and top
       points, in order from left to right and base to top, of the membership function. The degree
       of membership of the linguistic variable within the linguistic term name is 0 at the base
       points and 1 at the top points. Specify one point for a singleton function, three points for a
       triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
       functions.

      •       color —

       color specifies the color of the membership function when you view the membership
       function in the Fuzzy System Designer. You can wire a color box constant to this input.

      •      user-defined shape index —

      user-defined shape index specifies the index of the user-defined shape that determines the
      degrees of membership for the linguistic variable. This parameter is applicable only if you
       set shape to User-Defined. Define the user-defined shapes in the user-defined membership


                                                   © National Instruments 5849

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5849 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5850 ordinal=5850 -->
## Functions

Functions


                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FLFL CreateCreate MembershipMembership FunctionFunction (Trapezoid)(Trapezoid)
    VIVI

       Creates a membership function for a linguistic variable. You also can use the Define
       Variable dialog box to create membership functions interactively.

      By default, this VI uses a triangle function to determine the degrees of membership for
       the linguistic variable. You must manually select the polymorphic instance you want to
       use.


      Inputs/Outputs

               •     name —

         name specifies the name of the membership function, or linguistic term, you want to create.

               •        left base —

               left base specifies the numerical value of the linguistic variable corresponding to the left base
            point of the membership function. The degree of membership of the linguistic variable within


5850   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5850 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5851 ordinal=5851 -->
## Functions

Functions


  the linguistic term name is 0 at the left base value.

•        left top —

   left top specifies the numerical value of the linguistic variable corresponding to the left top point
  of the membership function. The degree of membership of the linguistic variable within the
   linguistic term name is 1 at the left top value.

•       right top —

  right top specifies the numerical value of the linguistic variable corresponding to the right top
  point of the membership function. The degree of membership of the linguistic variable within
  the linguistic term name is 1 at the right top value.

•       right base —

  right base specifies the numerical value of the linguistic variable corresponding to the right base
  point of the membership function. The degree of membership of the linguistic variable within
  the linguistic term name is 0 at the right base value.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       color —

  color specifies the color of the membership function when you view the membership function in
  the Fuzzy System Designer. You can wire a color box constant to this input.

•     membership function —

  membership function returns the membership function with the shape, points, and color you
  specify.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to
      modify.

      •      shape —


                                                   © National Instruments 5851

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5851 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5852 ordinal=5852 -->
## Functions

Functions


              shape specifies the shape of the function that determines the degrees of membership for
                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FLFL CreateCreate MembershipMembership FunctionFunction (Singleton)(Singleton)
    VIVI

       Creates a membership function for a linguistic variable. You also can use the Define
       Variable dialog box to create membership functions interactively.

      By default, this VI uses a triangle function to determine the degrees of membership for
       the linguistic variable. You must manually select the polymorphic instance you want to

5852   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5852 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5853 ordinal=5853 -->
## Functions

Functions

use.


Inputs/Outputs

   •     name —

   name specifies the name of the membership function, or linguistic term, you want to create.

   •      value —

    value specifies the numerical value of the linguistic variable corresponding to the unique point
     of the singleton membership function. The degree of membership of the linguistic variable
    within the linguistic term name is 1 at this value.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       color —

    color specifies the color of the membership function when you view the membership function in
    the Fuzzy System Designer. You can wire a color box constant to this input.

   •     membership function —

    membership function returns the membership function with the shape, points, and color you
     specify.

         •     name —

      name specifies the name of the membership function, or linguistic term, you want to
        modify.

         •      shape —

       shape specifies the shape of the function that determines the degrees of membership for


                                                    © National Instruments 5853

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5853 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5854 ordinal=5854 -->
## Functions

Functions


                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FLFL CreateCreate MembershipMembership FunctionFunction (Sigmoid)(Sigmoid) VIVI

       Creates a membership function for a linguistic variable. You also can use the Define
       Variable dialog box to create membership functions interactively.

      By default, this VI uses a triangle function to determine the degrees of membership for
       the linguistic variable. You must manually select the polymorphic instance you want to
       use.


5854   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5854 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5855 ordinal=5855 -->
## Functions

Functions


Inputs/Outputs

   •     name —

   name specifies the name of the membership function, or linguistic term, you want to create.

   •        left base —

     left base specifies the numerical value of the linguistic variable corresponding to the left base
    point of the membership function. The degree of membership of the linguistic variable within
    the linguistic term name is 0 at the left base value.

   •        left top —

     left top specifies the numerical value of the linguistic variable corresponding to the left top point
     of the membership function. The degree of membership of the linguistic variable within the
     linguistic term name is 1 at the left top value.

   •       right top —

     right top specifies the numerical value of the linguistic variable corresponding to the right top
    point of the membership function. The degree of membership of the linguistic variable within
    the linguistic term name is 1 at the right top value.

   •       right base —

     right base specifies the numerical value of the linguistic variable corresponding to the right base
    point of the membership function. The degree of membership of the linguistic variable within
    the linguistic term name is 0 at the right base value.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •       color —


                                                    © National Instruments 5855

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5855 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5856 ordinal=5856 -->
## Functions

Functions


             color specifies the color of the membership function when you view the membership function in
            the Fuzzy System Designer. You can wire a color box constant to this input.

               •     membership function —

          membership function returns the membership function with the shape, points, and color you
              specify.

                     •     name —

            name specifies the name of the membership function, or linguistic term, you want to
                modify.

                     •      shape —

              shape specifies the shape of the function that determines the degrees of membership for
                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error out —


5856   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5856 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5857 ordinal=5857 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

FLFL CreateCreate MembershipMembership FunctionFunction (Gaussian)(Gaussian)
VIVI

Creates a membership function for a linguistic variable. You also can use the Define
Variable dialog box to create membership functions interactively.

By default, this VI uses a triangle function to determine the degrees of membership for
the linguistic variable. You must manually select the polymorphic instance you want to
use.


Inputs/Outputs

   •     name —

   name specifies the name of the membership function, or linguistic term, you want to create.

   •        left base —

     left base specifies the numerical value of the linguistic variable corresponding to the left base
    point of the membership function. The degree of membership of the linguistic variable within
    the linguistic term name is 0 at the left base value.

   •        left top —

     left top specifies the numerical value of the linguistic variable corresponding to the left top point
     of the membership function. The degree of membership of the linguistic variable within the
     linguistic term name is 1 at the left top value.


                                                    © National Instruments 5857

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5857 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5858 ordinal=5858 -->
## Functions

Functions

               •       right top —

             right top specifies the numerical value of the linguistic variable corresponding to the right top
            point of the membership function. The degree of membership of the linguistic variable within
            the linguistic term name is 1 at the right top value.

               •       right base —

             right base specifies the numerical value of the linguistic variable corresponding to the right base
            point of the membership function. The degree of membership of the linguistic variable within
            the linguistic term name is 0 at the right base value.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       color —

             color specifies the color of the membership function when you view the membership function in
            the Fuzzy System Designer. You can wire a color box constant to this input.

               •     membership function —

          membership function returns the membership function with the shape, points, and color you
              specify.

                     •     name —

            name specifies the name of the membership function, or linguistic term, you want to
                modify.

                     •      shape —

              shape specifies the shape of the function that determines the degrees of membership for
                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a


5858   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5858 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5859 ordinal=5859 -->
## Functions

Functions


         triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
         functions.

         •       color —

         color specifies the color of the membership function when you view the membership
         function in the Fuzzy System Designer. You can wire a color box constant to this input.

         •      user-defined shape index —

        user-defined shape index specifies the index of the user-defined shape that determines the
        degrees of membership for the linguistic variable. This parameter is applicable only if you
         set shape to User-Defined. Define the user-defined shapes in the user-defined membership
        function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
        the FL Create Membership Function VI.


   •       error out —

    error out contains error information. This output provides standard error out functionality.

FLFL CreateCreate MembershipMembership FunctionFunction (User-(User-
Defined)Defined) VIVI

Creates a membership function for a linguistic variable. You also can use the Define
Variable dialog box to create membership functions interactively.

      Note Uses a user-defined function to determine the degrees of membership
         for the linguistic variable.


                                                    © National Instruments 5859

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5859 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5860 ordinal=5860 -->
## Functions

Functions


      Inputs/Outputs

               •     name —

         name specifies the name of the membership function, or linguistic term, you want to create.

               •        left base —

               left base specifies the numerical value of the linguistic variable corresponding to the left base
            point of the membership function. The degree of membership of the linguistic variable within
            the linguistic term name is 0 at the left base value.

               •        left top —

               left top specifies the numerical value of the linguistic variable corresponding to the left top point
             of the membership function. The degree of membership of the linguistic variable within the
              linguistic term name is 1 at the left top value.

               •       right top —

             right top specifies the numerical value of the linguistic variable corresponding to the right top
            point of the membership function. The degree of membership of the linguistic variable within
            the linguistic term name is 1 at the right top value.

               •       right base —

             right base specifies the numerical value of the linguistic variable corresponding to the right base
            point of the membership function. The degree of membership of the linguistic variable within
            the linguistic term name is 0 at the right base value.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       color —


5860   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5860 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5861 ordinal=5861 -->
## Functions

Functions


  color specifies the color of the membership function when you view the membership function in
  the Fuzzy System Designer. You can wire a color box constant to this input.

•      user-defined membership function shapes —

  user-defined membership function shapes specifies the x-y values of points that define custom
  shapes for membership functions. The shape of a membership function determines the degrees
  of membership for a linguistic variable within the corresponding linguistic term. Use the user-
  defined shape index to specify which user-defined membership function shape in this array you
  want to use for the membership function.

  For each custom membership function shape you define, you can use any range of x-values.
  However, the range of the y-values must be between 0 and 1 such that the first point you specify
  has a degree of membership of 0 and the last point you specify has a degree of membership of 1.
  LabVIEW scales the custom shape linearly between the left base and left top points and scales
  the mirror image of this shape linearly between the right top and right base points. Any points
  between left top and right top have a degree of membership of 1.

      •      Y —

      •     X —


•      user-defined shape index —

  user-defined shape index specifies the index of the shape in the user-defined membership
  function shapes array that you want to use for the membership function.

•     membership function —

  membership function returns the membership function with the shape, points, and color you
  specify.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to
      modify.

      •      shape —

      shape specifies the shape of the function that determines the degrees of membership for


                                                   © National Instruments 5861

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5861 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5862 ordinal=5862 -->
## Functions

Functions


                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL GetGet MembershipMembership FunctionFunction VIVI

       Returns the shape, color, and points of a membership function for a linguistic variable.
      You can return a membership function from a fuzzy system or from an array of
      membership functions. The data type you wire to the fuzzy system in input
      determines the polymorphic instance to use.


5862   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5862 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5863 ordinal=5863 -->
## Functions

Functions

  • FL Get Membership Function (Fuzzy System) VI
  • FL Get Membership Function (MF Array) VI
FLFL GetGet MembershipMembership FunctionFunction (Fuzzy(Fuzzy System)System)
VIVI

Returns the shape, color, and points of a membership function for a linguistic variable.
You can return a membership function from a fuzzy system or from an array of
membership functions. The data type you wire to the fuzzy system in input
determines the polymorphic instance to use.


Inputs/Outputs

   •     membership function index —

    membership function index specifies the index of the membership function whose information
    you want to return. membership function index corresponds to the order in which the
    membership function was created.

   •       variable index —

    variable index specifies the index of the linguistic variable whose information you want to
     return. variable index corresponds to the order in which the linguistic variable was created.

   •      input/output —

    input/output specifies whether the linguistic variable corresponding to variable index is an
    input or output variable.


                                                    © National Instruments 5863

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5863 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5864 ordinal=5864 -->
## Functions

Functions


             Input—Specifies that the linguistic variable corresponding to variable index is an input           0
               variable.
             Output—Specifies that the linguistic variable corresponding to variable index is an output           1               variable.

               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire the fuzzy system out
           output of this VI to the fuzzy system in input of another VI.

               •     name —

         name returns the name of the membership function, or linguistic term.

               •      shape —

           shape returns the shape of the function that determines the degrees of membership for the
              linguistic variable.

             Triangle—Indicates that a triangle function determines the degrees of membership for the           0
                linguistic variable.
             Trapezoid—Indicates that a trapezoid function determines the degrees of membership for the
           1
                linguistic variable.
             Singleton—Indicates that a singleton function determines the degrees of membership for the
           2 linguistic variable. A singleton function has only one point. Therefore, no value of the linguistic
              variable has partial membership within the corresponding linguistic term.
             Sigmoid—Indicates that a sigmoid function determines the degrees of membership for the
           3
                linguistic variable.
             Gaussian—Indicates that a Gaussian function determines the degrees of membership for the
           4
                linguistic variable.
           5 User-Defined—Indicates that the user-defined shape corresponding to the user-defined shape


5864   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5864 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5865 ordinal=5865 -->
## Functions

Functions


     index determines the degrees of membership for the linguistic variable.

   •      points —

    points returns the values of the linguistic variable corresponding to the base and top points, in
    order from left to right and base to top, of the membership function. The degree of membership
     of the linguistic variable within the linguistic term name is 0 at the base points and 1 at the top
     points. points returns one point for a singleton function, three points for a triangle function, and
    four points for trapezoid, sigmoid, Gaussian, or user-defined functions.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       color —

    color returns the color of the membership function when you view the membership function in
    the Fuzzy System Designer.

   •      user-defined shape index —

    user-defined shape index returns the index of the user-defined shape that determines the
    degrees of membership for the linguistic variable. This parameter is applicable only if shape
    returns User-Defined. Define the user-defined shapes in the user-defined membership function
    shapes array in both the FL New Fuzzy System VI and the User-Defined instance of the FL Create
    Membership Function VI.

FLFL GetGet MembershipMembership FunctionFunction (MF(MF Array)Array) VIVI

Returns the shape, color, and points of a membership function for a linguistic variable.
You can return a membership function from a fuzzy system or from an array of
membership functions. The data type you wire to the fuzzy system in input
determines the polymorphic instance to use.

      Note

       Returns a membership function from an array of membership functions.


                                                    © National Instruments 5865

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5865 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5866 ordinal=5866 -->
## Functions

Functions


      Inputs/Outputs

               •     membership function index —

          membership function index specifies the index of the membership function whose information
           you want to return. membership function index corresponds to the order in which the
          membership function was created.

               •     membership functions in —

          membership functions in specifies an array of membership functions. Wire the membership
            functions out output from another VI to the membership functions in input of this VI.

                     •     name —

            name specifies the name of the membership function, or linguistic term, you want to
                modify.

                     •      shape —

              shape specifies the shape of the function that determines the degrees of membership for
                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —


5866   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5866 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5867 ordinal=5867 -->
## Functions

Functions


       color specifies the color of the membership function when you view the membership
       function in the Fuzzy System Designer. You can wire a color box constant to this input.

      •      user-defined shape index —

      user-defined shape index specifies the index of the user-defined shape that determines the
      degrees of membership for the linguistic variable. This parameter is applicable only if you
       set shape to User-Defined. Define the user-defined shapes in the user-defined membership
      function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
      the FL Create Membership Function VI.


•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•     membership functions out —

  membership functions out returns an array of membership functions. Wire the membership
  functions out output of this VI to the membership functions in input of another VI.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to
      modify.

      •      shape —

      shape specifies the shape of the function that determines the degrees of membership for
      the linguistic variable.

      •      points —

      points specifies the values of the linguistic variable corresponding to the base and top
       points, in order from left to right and base to top, of the membership function. The degree
       of membership of the linguistic variable within the linguistic term name is 0 at the base
       points and 1 at the top points. Specify one point for a singleton function, three points for a
       triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
       functions.

      •       color —


                                                   © National Instruments 5867

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5867 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5868 ordinal=5868 -->
## Functions

Functions


                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •     name —

         name returns the name of the membership function, or linguistic term.

               •      shape —

           shape returns the shape of the function that determines the degrees of membership for the
              linguistic variable.

             Triangle—Indicates that a triangle function determines the degrees of membership for the           0                linguistic variable.
             Trapezoid—Indicates that a trapezoid function determines the degrees of membership for the           1                linguistic variable.
             Singleton—Indicates that a singleton function determines the degrees of membership for the
           2 linguistic variable. A singleton function has only one point. Therefore, no value of the linguistic
              variable has partial membership within the corresponding linguistic term.
             Sigmoid—Indicates that a sigmoid function determines the degrees of membership for the           3
                linguistic variable.
             Gaussian—Indicates that a Gaussian function determines the degrees of membership for the
           4
                linguistic variable.
             User-Defined—Indicates that the user-defined shape corresponding to the user-defined shape
           5
             index determines the degrees of membership for the linguistic variable.

               •      points —

            points returns the values of the linguistic variable corresponding to the base and top points, in
            order from left to right and base to top, of the membership function. The degree of membership
             of the linguistic variable within the linguistic term name is 0 at the base points and 1 at the top
             points. points returns one point for a singleton function, three points for a triangle function, and


5868   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5868 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5869 ordinal=5869 -->
## Functions

Functions


    four points for trapezoid, sigmoid, Gaussian, or user-defined functions.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

   •       color —

    color returns the color of the membership function when you view the membership function in
    the Fuzzy System Designer.

   •      user-defined shape index —

    user-defined shape index returns the index of the user-defined shape that determines the
    degrees of membership for the linguistic variable. This parameter is applicable only if shape
    returns User-Defined. Define the user-defined shapes in the user-defined membership function
    shapes array in both the FL New Fuzzy System VI and the User-Defined instance of the FL Create
    Membership Function VI.


FLFL SetSet MembershipMembership FunctionFunction VIVI

Modifies the shape, color, or points of a membership function for a linguistic variable.
You can modify a membership function from a fuzzy system or from an array of
membership functions. The data type you wire to the fuzzy system in input
determines the polymorphic instance to use.


  • FL Set Membership Function (Fuzzy System) VI
  • FL Set Membership Function (MF array) VI
FLFL SetSet MembershipMembership FunctionFunction (Fuzzy(Fuzzy System)System)
VIVI

Modifies the shape, color, or points of a membership function for a linguistic variable.
You can modify a membership function from a fuzzy system or from an array of

                                                    © National Instruments 5869

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5869 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5870 ordinal=5870 -->
## Functions

Functions

      membership functions. The data type you wire to the fuzzy system in input
      determines the polymorphic instance to use.


      Inputs/Outputs

               •     membership function index —

          membership function index specifies the index of the membership function you want to modify.
          membership function index corresponds to the order in which the membership function was
             created.

               •       variable index —

             variable index specifies the index of the linguistic variable you want to modify. variable index
            corresponds to the order in which the linguistic variable was created.

               •      input/output —

            input/output specifies whether the linguistic variable corresponding to variable index is an
            input or output variable.

             Input—Specifies that the linguistic variable corresponding to variable index is an input
           0
               variable.
             Output—Specifies that the linguistic variable corresponding to variable index is an output
           1
               variable.

               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •     name —


5870   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5870 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5871 ordinal=5871 -->
## Functions

Functions


  name specifies the name of the membership function, or linguistic term, you want to modify.

•      shape —

  shape specifies the shape of the function that determines the degrees of membership for the
   linguistic variable.

   Triangle—Specifies that a triangle function determines the degrees of membership for the  0    linguistic variable.
   Trapezoid—Specifies that a trapezoid function determines the degrees of membership for the  1    linguistic variable.
   Singleton—Specifies that a singleton function determines the degrees of membership for the
  2 linguistic variable. A singleton function has only one point. Therefore, no value of the linguistic
    variable has partial membership within the corresponding linguistic term.
   Sigmoid—Specifies that a sigmoid function determines the degrees of membership for the  3    linguistic variable.
   Gaussian—Specifies that a Gaussian function determines the degrees of membership for the  4    linguistic variable.
   User-Defined—Specifies that the user-defined shape corresponding to the user-defined shape  5   index determines the degrees of membership for the linguistic variable.

•      points —

  points specifies the values of the linguistic variable corresponding to the base and top points, in
  order from left to right and base to top, of the membership function. The degree of membership
  of the linguistic variable within the linguistic term name is 0 at the base points and 1 at the top
  points. Specify one point for a singleton function, three points for a triangle function, and four
  points for trapezoid, sigmoid, Gaussian, or user-defined functions.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•       color —

  color specifies the color of the membership function when you view the membership function in
  the Fuzzy System Designer. You can wire a color box constant to this input.

•      user-defined shape index —

  user-defined shape index specifies the index of the user-defined shape that determines the


                                                   © National Instruments 5871

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5871 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5872 ordinal=5872 -->
## Functions

Functions


            degrees of membership for the linguistic variable. This parameter is applicable only if you set
           shape to User-Defined. Define the user-defined shapes in the user-defined membership
            function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of the
           FL Create Membership Function VI.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire the fuzzy system out
           output of this VI to the fuzzy system in input of another VI.

               •       error out —

             error out contains error information. This output provides standard error out functionality.

   FLFL SetSet MembershipMembership FunctionFunction (MF(MF array)array) VIVI

       Modifies the shape, color, or points of a membership function for a linguistic variable.
      You can modify a membership function from a fuzzy system or from an array of
      membership functions. The data type you wire to the fuzzy system in input
      determines the polymorphic instance to use.

           Note Modifies a membership function from an array of membership
               functions.


      Inputs/Outputs

               •     membership function index —


5872   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5872 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5873 ordinal=5873 -->
## Functions

Functions


  membership function index specifies the index of the membership function you want to modify.
  membership function index corresponds to the order in which the membership function was
  created.

•     membership functions in —

  membership functions in specifies an array of membership functions. Wire the membership
  functions out output from another VI to the membership functions in input of this VI.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to
      modify.

      •      shape —

      shape specifies the shape of the function that determines the degrees of membership for
      the linguistic variable.

      •      points —

      points specifies the values of the linguistic variable corresponding to the base and top
       points, in order from left to right and base to top, of the membership function. The degree
       of membership of the linguistic variable within the linguistic term name is 0 at the base
       points and 1 at the top points. Specify one point for a singleton function, three points for a
       triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
       functions.

      •       color —

       color specifies the color of the membership function when you view the membership
       function in the Fuzzy System Designer. You can wire a color box constant to this input.

      •      user-defined shape index —

      user-defined shape index specifies the index of the user-defined shape that determines the
      degrees of membership for the linguistic variable. This parameter is applicable only if you
       set shape to User-Defined. Define the user-defined shapes in the user-defined membership
      function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
      the FL Create Membership Function VI.


•     name —


                                                   © National Instruments 5873

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5873 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5874 ordinal=5874 -->
## Functions

Functions


         name specifies the name of the membership function, or linguistic term, you want to modify.

               •      shape —

           shape specifies the shape of the function that determines the degrees of membership for the
              linguistic variable.

              Triangle—Specifies that a triangle function determines the degrees of membership for the           0                linguistic variable.
             Trapezoid—Specifies that a trapezoid function determines the degrees of membership for the           1                linguistic variable.
             Singleton—Specifies that a singleton function determines the degrees of membership for the
           2 linguistic variable. A singleton function has only one point. Therefore, no value of the linguistic
              variable has partial membership within the corresponding linguistic term.
             Sigmoid—Specifies that a sigmoid function determines the degrees of membership for the           3                linguistic variable.
             Gaussian—Specifies that a Gaussian function determines the degrees of membership for the           4                linguistic variable.
             User-Defined—Specifies that the user-defined shape corresponding to the user-defined shape           5             index determines the degrees of membership for the linguistic variable.

               •      points —

            points specifies the values of the linguistic variable corresponding to the base and top points, in
            order from left to right and base to top, of the membership function. The degree of membership
             of the linguistic variable within the linguistic term name is 0 at the base points and 1 at the top
             points. Specify one point for a singleton function, three points for a triangle function, and four
            points for trapezoid, sigmoid, Gaussian, or user-defined functions.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •       color —

             color specifies the color of the membership function when you view the membership function in
            the Fuzzy System Designer. You can wire a color box constant to this input.

               •      user-defined membership function shapes —


5874   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5874 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5875 ordinal=5875 -->
## Functions

Functions


      •      Y —

      •     X —


•      user-defined shape index —

  user-defined shape index specifies the index of the user-defined shape that determines the
  degrees of membership for the linguistic variable. This parameter is applicable only if you set
  shape to User-Defined. Define the user-defined shapes in the user-defined membership
  function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of the
  FL Create Membership Function VI.

•     membership functions out —

  membership functions out returns an array of membership functions. Wire the membership
  functions out output of this VI to the membership functions in input of another VI.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want to
      modify.

      •      shape —

      shape specifies the shape of the function that determines the degrees of membership for
      the linguistic variable.

      •      points —

      points specifies the values of the linguistic variable corresponding to the base and top
       points, in order from left to right and base to top, of the membership function. The degree
       of membership of the linguistic variable within the linguistic term name is 0 at the base
       points and 1 at the top points. Specify one point for a singleton function, three points for a
       triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
       functions.

      •       color —

       color specifies the color of the membership function when you view the membership
       function in the Fuzzy System Designer. You can wire a color box constant to this input.

      •      user-defined shape index —


                                                   © National Instruments 5875

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5875 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5876 ordinal=5876 -->
## Functions

Functions


                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL GetGet NumberNumber ofof MembershipMembership FunctionsFunctions

       Returns the number of membership functions for all input and output variables in the
       fuzzy system you specify.


      Inputs/Outputs

               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •     number of input membership functions —


5876   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5876 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5877 ordinal=5877 -->
## Functions

Functions


   number of input membership functions returns the number of membership functions, or
     linguistic terms, for each input variable in the fuzzy system. Each element in the number of
    input membership functions array represents the number of membership functions for the
    input variable that corresponds, in order of creation, to the index of the array element.

   •     number of output membership functions —

   number of output membership functions returns the number of membership functions, or
     linguistic terms, for each output variable in the fuzzy system. Each element in the number of
    output membership functions array represents the number of membership functions for the
    output variable that corresponds, in order of creation, to the index of the array element.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FLFL GetGet MembershipMembership FunctionFunction NamesNames VIVI

Returns the names of the linguistic terms for a linguistic variable. Membership
functions represent the degree of membership of linguistic variables within their
linguistic terms. You can return the names of the membership functions from a fuzzy
system or from an array of membership functions. The data type you wire to the fuzzy
system in input determines the polymorphic instance to use.


  • FL Get Membership Function Names (Fuzzy System) VI
  • FL Get Membership Function Names (MF Array) VI
FLFL GetGet MembershipMembership FunctionFunction NamesNames (Fuzzy(Fuzzy
System)System) VIVI

Returns the names of the linguistic terms for a linguistic variable. Membership
functions represent the degree of membership of linguistic variables within their
linguistic terms. You can return the names of the membership functions from a fuzzy

                                                    © National Instruments 5877

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5877 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5878 ordinal=5878 -->
## Functions

Functions

      system or from an array of membership functions. The data type you wire to the fuzzy
      system in input determines the polymorphic instance to use.


      Inputs/Outputs

               •       variable index —

             variable index specifies the index of the linguistic variable whose information you want to
             return. variable index corresponds to the order in which the linguistic variable was created.

               •      input/output —

            input/output specifies whether the linguistic variable corresponding to variable index is an
            input or output variable.

             Input—Specifies that the linguistic variable corresponding to variable index is an input
           0               variable.
             Output—Specifies that the linguistic variable corresponding to variable index is an output
           1               variable.

               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire the fuzzy system out
           output of this VI to the fuzzy system in input of another VI.

               •     membership function names —


5878   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5878 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5879 ordinal=5879 -->
## Functions

Functions


    membership function names returns the names of the membership functions, or linguistic
    terms, for the linguistic variable.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

FLFL GetGet MembershipMembership FunctionFunction NamesNames (MF(MF
Array)Array) VIVI

Returns the names of the linguistic terms for a linguistic variable. Membership
functions represent the degree of membership of linguistic variables within their
linguistic terms. You can return the names of the membership functions from a fuzzy
system or from an array of membership functions. The data type you wire to the fuzzy
system in input determines the polymorphic instance to use.


Inputs/Outputs

   •     membership functions in —

    membership functions in specifies an array of membership functions. Wire the membership
    functions out output from another VI to the membership functions in input of this VI.

         •     name —

      name specifies the name of the membership function, or linguistic term, you want to
        modify.

         •      shape —

       shape specifies the shape of the function that determines the degrees of membership for


                                                    © National Instruments 5879

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5879 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5880 ordinal=5880 -->
## Functions

Functions


                the linguistic variable.

                     •      points —

                points specifies the values of the linguistic variable corresponding to the base and top
                  points, in order from left to right and base to top, of the membership function. The degree
                  of membership of the linguistic variable within the linguistic term name is 0 at the base
                 points and 1 at the top points. Specify one point for a singleton function, three points for a
                  triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
                  functions.

                     •       color —

                 color specifies the color of the membership function when you view the membership
                 function in the Fuzzy System Designer. You can wire a color box constant to this input.

                     •      user-defined shape index —

                user-defined shape index specifies the index of the user-defined shape that determines the
                degrees of membership for the linguistic variable. This parameter is applicable only if you
                  set shape to User-Defined. Define the user-defined shapes in the user-defined membership
                function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
                the FL Create Membership Function VI.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •     membership functions out —

          membership functions out returns an array of membership functions. Wire the membership
            functions out output of this VI to the membership functions in input of another VI.

                     •     name —

            name specifies the name of the membership function, or linguistic term, you want to
                modify.

                     •      shape —


5880   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5880 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5881 ordinal=5881 -->
## Functions

Functions


       shape specifies the shape of the function that determines the degrees of membership for
        the linguistic variable.

         •      points —

        points specifies the values of the linguistic variable corresponding to the base and top
         points, in order from left to right and base to top, of the membership function. The degree
         of membership of the linguistic variable within the linguistic term name is 0 at the base
         points and 1 at the top points. Specify one point for a singleton function, three points for a
         triangle function, and four points for trapezoid, sigmoid, Gaussian, or user-defined
         functions.

         •       color —

         color specifies the color of the membership function when you view the membership
         function in the Fuzzy System Designer. You can wire a color box constant to this input.

         •      user-defined shape index —

        user-defined shape index specifies the index of the user-defined shape that determines the
        degrees of membership for the linguistic variable. This parameter is applicable only if you
         set shape to User-Defined. Define the user-defined shapes in the user-defined membership
        function shapes array in both the FL New Fuzzy System VI and the User-Defined instance of
        the FL Create Membership Function VI.


   •     membership function names —

    membership function names returns the names of the membership functions, or linguistic
    terms, for the linguistic variable.

   •       error out —

    error out contains error information. This output provides standard error out functionality.

RulesRules

Use the Rules VIs to modify the rules for a fuzzy system. Rules describe, in words, the
relationships between input and output linguistic variables based on their linguistic
terms.


                                                    © National Instruments 5881

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5881 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5882 ordinal=5882 -->
## Functions

Functions

      The VIs on this palette can return general LabVIEW error codes and specific PID and
       Fuzzy Logic error codes.


         Palette                      Description
        Object

        FL Create    Creates a rule for a fuzzy system. You also can use the Rule Editor page of the Fuzzy
        Rule        System Designer to create rules interactively.


        FL Get Rule  Returns the antecedents, consequents, and relationships for a rule in a fuzzy system.


        FL Set Rule   Modifies the antecedents, consequents, or relationships of a rule in a fuzzy system.

        FL Get
       Number of   Returns the number of rules in the fuzzy system you specify.
         Rules

        FL Get
         Rules as     Returns the rules of a fuzzy system in words.
         Text

                      Creates an antecedent, or IF portion, of a rule for a fuzzy system. An antecedent
                       consists of three parts: an input linguistic variable, an operator that specifies whether
                      to calculate the degree of membership or the degree of non-membership of the input
        FL Create     linguistic variable within a linguistic term, and a linguistic term.
        Antecedent
                   You can use the Build Array function or a loop to build an array of rule antecedents
                       that you create with this VI. You then can wire the array to the antecedents input of
                     the FL Create Rule VI.


                      Creates a consequent, or THEN portion, of a rule for a fuzzy system. A consequent
        FL Create
                       consists of three parts: an output linguistic variable, an operator that specifies to
        Consequent
                       calculate the degree of membership of the output linguistic variable within a


5882   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5882 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5883 ordinal=5883 -->
## Functions

Functions


 Palette              Description
 Object

                linguistic term, and a linguistic term.

            You can use the Build Array function or a loop to build an array of rule consequents
              that you create with this VI. You then can wire the array to the consequents input of
             the FL Create Rule VI.

 FL Integrate  Checks a new rule for conflicts with existing rules in the fuzzy system and, optionally,
 Rule         integrates the new rule into the system.

FLFL CreateCreate RuleRule

Creates a rule for a fuzzy system. You also can use the Rule Editor page of the Fuzzy
System Designer to create rules interactively.


Inputs/Outputs

   •      antecedent connective —

    antecedent connective specifies how this VI calculates the truth value of the aggregated rule
    antecedent.

    AND (Minimum)—Specifies that this VI uses the smallest degree of membership of the
    0
      antecedents.
    AND (Product)—Specifies that this VI uses the product of the degrees of membership of the
    1
      antecedents.
    OR (Maximum)—Specifies that this VI uses the largest degree of membership of the
    2
      antecedents.
    OR (Probabilistic)—Specifies that this VI uses the probabilistic sum of the degrees of
    3
     membership of the antecedents. The fuzzy logic controller uses the following equation to


                                                    © National Instruments 5883

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5883 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5884 ordinal=5884 -->
## Functions

Functions


              calculate the probabilistic sum: (A+ B) – (A* B), where Aand Bare the antecedents.

               •      antecedents —

           antecedents specifies the antecedents, or IF portions, of the rule. Each antecedent consists of
            three parts: the index of an input linguistic variable, an operator that specifies whether to
             calculate the degree of membership or the degree of non-membership of the input linguistic
             variable within a linguistic term, and the index of the linguistic term. The indexes correspond to
            the order in which the variables or linguistic terms were created.

           You can use the Build Array function or a loop to build an array of rule antecedents that you
             create with the FL Create Antecedent VI. You then can wire the array to this input.

                     •      Var Index —

              The index of an input linguistic variable.

                     •     MF Index —

              The index of the linguistic term.

                     •     Cond —

              An operator that specifies whether to calculate the degree of membership or the degree of
              non-membership of the linguistic variable within a linguistic term.


               •      degree of support (1) —

           degree of support specifies the weight, between 0 and 1, that you want to apply to the rule. The
             default is 1. Multiply the degree of support by the truth value of the aggregated rule antecedent
             to calculate the rule weight.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      consequents —

           consequents specifies the consequents, or THEN portions, of the rule. Each consequent consists
             of three parts: the index of an output linguistic variable, an operator that specifies whether to
             calculate the degree of membership or the degree of non-membership of the output linguistic


5884   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5884 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5885 ordinal=5885 -->
## Functions

Functions


  variable within a linguistic term, and the index of the linguistic term. The indexes correspond to
  the order in which the variables or linguistic terms were created.

  You can use the Build Array function or a loop to build an array of rule consequents that you
  create with the FL Create Consequent VI. You then can wire the array to this input.

      •      Var Index —

     The index of an output linguistic variable.

      •     MF Index —

     The index of the linguistic term.

      •     Cond —

     An operator that specifies whether to calculate the degree of membership or the degree of
      non-membership of the linguistic variable within a linguistic term.


•      consequent implication —

  consequent implication specifies the implication method this VI uses to scale the membership
  functions of the output linguistic variable based on the rule weight.

  0 Minimum—Specifies to use the Minimum implication method.
  1 Product—Specifies to use the Product implication method.

•       rule —

  rule returns the rule with the antecedents, consequents, and relationships you specify.

      •      antecedents —

      antecedents specifies the antecedents, or IF portions, of the rule. Each antecedent consists
       of three parts: the index of an input linguistic variable, an operator that specifies whether to
       calculate the degree of membership or the degree of non-membership of the input
        linguistic variable within a linguistic term, and the index of the linguistic term. The indexes
      correspond to the order in which the variables or linguistic terms were created.


                                                   © National Instruments 5885

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5885 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5886 ordinal=5886 -->
## Functions

Functions


                           •      Var Index —

                  The index of an input linguistic variable.

                           •     MF Index —

                  The index of the linguistic term.

                           •     Cond —

                 An operator that specifies whether to calculate the degree of membership or the
                   degree of non-membership of the linguistic variable within a linguistic term.


                     •      antecedent connective —

               antecedent connective specifies how this VI calculates the truth value of the aggregated
                  rule antecedent.

                     •      consequents —

               consequents specifies the consequents, or THEN portions, of the rule. Each consequent
                  consists of three parts: the index of an output linguistic variable, an operator that specifies
               whether to calculate the degree of membership or the degree of non-membership of the
               output linguistic variable within a linguistic term, and the index of the linguistic term. The
                indexes correspond to the order in which the variables or linguistic terms were created.

                           •      Var Index —

                  The index of an output linguistic variable.

                           •     MF Index —

                  The index of the linguistic term.

                           •     Cond —

                 An operator that specifies whether to calculate the degree of membership or the
                   degree of non-membership of the linguistic variable within a linguistic term.


                     •      consequent implication —


5886   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5886 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5887 ordinal=5887 -->
## Functions

Functions


        consequent implication specifies the implication method this VI uses to scale the
       membership functions of the output linguistic variable based on the rule weight.

         •      degree of support —

        degree of support specifies the weight, between 0 and 1, that you want to apply to the rule.
       The default is 1. Multiply the degree of support by the truth value of the aggregated rule
        antecedent to calculate the rule weight.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


FLFL GetGet RuleRule

Returns the antecedents, consequents, and relationships for a rule in a fuzzy system.


Inputs/Outputs

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
    output from another VI to the fuzzy system in input of this VI.

   •       rule index —

    rule index specifies the index of the rule whose information you want to return. rule index
    corresponds to the order in which the rule was created.

   •       error in (no error) —


                                                    © National Instruments 5887

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5887 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5888 ordinal=5888 -->
## Functions

Functions


             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      antecedent connective —

           antecedent connective indicates how this VI calculates the truth value of the aggregated rule
            antecedent.

          AND (Minimum)—Indicates that this VI uses the smallest degree of membership of the
           0              antecedents.
          AND (Product)—Indicates that this VI uses the product of the degrees of membership of the           1              antecedents.
          OR (Maximum)—Indicates that this VI uses the largest degree of membership of the
           2              antecedents.
          OR (Probabilistic)—Indicates that this VI uses the probabilistic sum of the degrees of
           3 membership of the antecedents. The fuzzy logic controller uses the following equation to
              calculate the probabilistic sum: (A+ B) – (A* B), where A and B are the antecedents.

               •      antecedents —

           antecedents returns the antecedents, or IF portions, of the rule. Each antecedent consists of
            three parts: the index of an input linguistic variable, an operator that specifies whether to
             calculate the degree of membership or the degree of non-membership of the input linguistic
             variable within a linguistic term, and the index of the linguistic term. The indexes correspond to
            the order in which the variables or linguistic terms were created.

                     •      Var Index —

              The index of an input linguistic variable.

                     •     MF Index —

              The index of the linguistic term.

                     •     Cond —

              An operator that specifies whether to calculate the degree of membership or the degree of
              non-membership of the linguistic variable within a linguistic term.


               •      fuzzy system out —


5888   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5888 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5889 ordinal=5889 -->
## Functions

Functions


  fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
  fuzzy system in input of another VI.

•      degree of support —

  degree of support returns the weight, between 0 and 1, that you want to apply to the rule.
  Multiply the degree of support by the truth value of the aggregated rule antecedent to calculate
  the rule weight.

•       error out —

  error out contains error information. This output provides standard error out functionality.

•      consequents —

  consequents returns the consequents, or THEN portions, of the rule. Each consequent consists
  of three parts: the index of an output linguistic variable, an operator that specifies whether to
  calculate the degree of membership or the degree of non-membership of the output linguistic
  variable within a linguistic term, and the index of the linguistic term. The indexes correspond to
  the order in which the variables or linguistic terms were created.

      •      Var Index —

     The index of an output linguistic variable.

      •     MF Index —

     The index of the linguistic term.

      •     Cond —

     An operator that specifies whether to calculate the degree of membership or the degree of
      non-membership of the linguistic variable within a linguistic term.


•      consequent implication —

  consequent implication returns the implication method this VI uses to scale the membership
  functions of the output linguistic variable based on the rule weight.

  0 Minimum—Indicates that this VI uses the Minimum implication method.
  1 Product—Indicates that this VI uses the Product implication method.


                                                   © National Instruments 5889

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5889 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5890 ordinal=5890 -->
## Functions

Functions

      FLFL SetSet RuleRule

       Modifies the antecedents, consequents, or relationships of a rule in a fuzzy system.


      Inputs/Outputs

               •      antecedent connective —

           antecedent connective specifies how this VI calculates the truth value of the aggregated rule
            antecedent.

          AND (Minimum)—Specifies that this VI uses the smallest degree of membership of the           0              antecedents.
          AND (Product)—Specifies that this VI uses the product of the degrees of membership of the           1              antecedents.
          OR (Maximum)—Specifies that this VI uses the largest degree of membership of the           2              antecedents.
          OR (Probabilistic)—Specifies that this VI uses the probabilistic sum of the degrees of
           3 membership of the antecedents. The fuzzy logic controller uses the following equation to
              calculate the probabilistic sum: (A+ B) – (A* B), where Aand Bare the antecedents.

               •      antecedents —

           antecedents specifies the antecedents, or IF portions, of the rule. Each antecedent consists of
            three parts: the index of an input linguistic variable, an operator that specifies whether to
             calculate the degree of membership or the degree of non-membership of the input linguistic
             variable within a linguistic term, and the index of the linguistic term. The indexes correspond to
            the order in which the variables or linguistic terms were created.

           You can use the Build Array function or a loop to build an array of rule antecedents that you
             create with the FL Create Antecedent VI. You then can wire the array to this input.


5890   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5890 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5891 ordinal=5891 -->
## Functions

Functions


      •      Var Index —

     The index of an input linguistic variable.

      •     MF Index —

     The index of the linguistic term.

      •     Cond —

     An operator that specifies whether to calculate the degree of membership or the degree of
      non-membership of the linguistic variable within a linguistic term.


•      fuzzy system in —

  fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
  output from another VI to the fuzzy system in input of this VI.

•       rule index —

  rule index specifies the index of the rule whose information you want to return. rule index
  corresponds to the order in which the rule was created.

•      degree of support (1) —

  degree of support specifies the weight, between 0 and 1, that you want to apply to the rule. The
  default is 1. Multiply the degree of support by the truth value of the aggregated rule antecedent
  to calculate the rule weight.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      consequents —

  consequents specifies the consequents, or THEN portions, of the rule. Each consequent consists
  of three parts: the index of an output linguistic variable, an operator that specifies whether to
  calculate the degree of membership or the degree of non-membership of the output linguistic
  variable within a linguistic term, and the index of the linguistic term. The indexes correspond to
  the order in which the variables or linguistic terms were created.


                                                   © National Instruments 5891

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5891 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5892 ordinal=5892 -->
## Functions

Functions


           You can use the Build Array function or a loop to build an array of rule consequents that you
             create with the FL Create Consequent VI. You then can wire the array to this input.

                     •      Var Index —

              The index of an output linguistic variable.

                     •     MF Index —

              The index of the linguistic term.

                     •     Cond —

              An operator that specifies whether to calculate the degree of membership or the degree of
              non-membership of the linguistic variable within a linguistic term.


               •      consequent implication —

           consequent implication specifies the implication method this VI uses to scale the membership
             functions of the output linguistic variable based on the rule weight.

           0 Minimum—Specifies to use the Minimum implication method.
           1 Product—Specifies to use the Product implication method.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL GetGet NumberNumber ofof RulesRules

       Returns the number of rules in the fuzzy system you specify.


5892   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5892 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5893 ordinal=5893 -->
## Functions

Functions


Inputs/Outputs

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
    output from another VI to the fuzzy system in input of this VI.

   •       error in (no error) —

    error in describes error conditions that occur before this node runs. This input provides
    standard error in functionality.

   •      fuzzy system out —

    fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
    fuzzy system in input of another VI.

   •     number of rules —

   number of rules returns the number of rules in the fuzzy system.

   •       error out —

    error out contains error information. This output provides standard error out functionality.


FLFL GetGet RulesRules asas TextText

Returns the rules of a fuzzy system in words.


Inputs/Outputs

   •      fuzzy system in —

    fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out


                                                    © National Instruments 5893

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5893 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5894 ordinal=5894 -->
## Functions

Functions


           output from another VI to the fuzzy system in input of this VI.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •       rules as text —

             rules as text returns the rules of the fuzzy system in words. Each element in the rules as text
             array represents the rule that corresponds, in order of creation, to the index of the element.

               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL CreateCreate AntecedentAntecedent

       Creates an antecedent, or IF portion, of a rule for a fuzzy system. An antecedent
       consists of three parts: an input linguistic variable, an operator that specifies whether
       to calculate the degree of membership or the degree of non-membership of the input
        linguistic variable within a linguistic term, and a linguistic term.

      You can use the Build Array function or a loop to build an array of rule antecedents that
      you create with this VI. You then can wire the array to the antecedents input of the FL
       Create Rule VI.


      Inputs/Outputs

               •       variable index —

5894   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5894 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5895 ordinal=5895 -->
## Functions

Functions


  variable index specifies the index of the linguistic variable you want to use for the antecedent.
  variable index corresponds to the order in which the linguistic variable was created.

•     membership function index —

  membership function index specifies the index of the membership function you want to relate
  to the corresponding linguistic variable. membership function index corresponds to the order in
  which the membership function was created.

•      condition —

  condition specifies whether to calculate the degree of membership or the degree of non-
  membership of the linguistic variable in the membership function.

    =  0    —Tells the VI to calculate the degree of membership, or μ.
    !=  1    —Tells the VI to calculate the degree of non-membership, or 1 – μ.

•       error in (no error) —

  error in describes error conditions that occur before this node runs. This input provides
  standard error in functionality.

•      antecedent —

  antecedent returns the antecedent, or IF portion, of a rule. The antecedent consists of three
  parts corresponding to the variable index, condition, and membership function index,
  respectively.

      •      Var Index —

     The index of an input linguistic variable.

      •     MF Index —

     The index of the linguistic term.

      •     Cond —

     An operator that specifies whether to calculate the degree of membership or the degree of


                                                   © National Instruments 5895

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5895 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5896 ordinal=5896 -->
## Functions

Functions


              non-membership of the linguistic variable within a linguistic term.


               •       error out —

             error out contains error information. This output provides standard error out functionality.


      FLFL CreateCreate ConsequentConsequent

       Creates a consequent, or THEN portion, of a rule for a fuzzy system. A consequent
       consists of three parts: an output linguistic variable, an operator that specifies to
       calculate the degree of membership of the output linguistic variable within a linguistic
       term, and a linguistic term.

      You can use the Build Array function or a loop to build an array of rule consequents
       that you create with this VI. You then can wire the array to the consequents input of
       the FL Create Rule VI.


      Inputs/Outputs

               •       variable index —

             variable index specifies the index of the linguistic variable you want to use for the consequent.
             variable index corresponds to the order in which the linguistic variable was created.

               •     membership function index —

          membership function index specifies the index of the membership function you want to relate
             to the corresponding linguistic variable. membership function index corresponds to the order in
           which the membership function was created.

               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides


5896   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5896 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5897 ordinal=5897 -->
## Functions

Functions


    standard error in functionality.

   •      consequent —

    consequent returns the consequent, or THEN portion, of a rule. The first and last parts of the
    consequent correspond to the variable index and membership function index, respectively.
    The middle part of the consequent is an operator specifying to calculate mu, the degree of
    membership of the linguistic variable within the membership function.

         •      Var Index —

       The index of an output linguistic variable.

         •     MF Index —

       The index of the linguistic term.

         •     Cond —

       An operator that specifies whether to calculate the degree of membership or the degree of
       non-membership of the linguistic variable within a linguistic term.


   •       error out —

    error out contains error information. This output provides standard error out functionality.


FLFL IntegrateIntegrate RuleRule

Checks a new rule for conflicts with existing rules in the fuzzy system and, optionally,
integrates the new rule into the system.


Inputs/Outputs

   •       integration option —

                                                    © National Instruments 5897

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5897 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5898 ordinal=5898 -->
## Functions

Functions

             integration option specifies the method to use for determining whether LabVIEW integrates the
         new rule. You can select from the following options:
                     • Check rule only—Checks the new rule for conflicts with existing rules but does not integrate
                the new rule.
                     • Add if no conflicts—Integrates the new rule only if it has no conflicts with existing rules.
                     • Add if partial conflicts—Integrates the new rule if it has partial, but not full, conflicts with
                  existing rules. A partial conflict occurs when an antecedent conflicts with one or more, but
                not all, antecedents declared in another rule.
                     • Replace if full conflict—Integrates the new rule as a replacement for an existing rule with
               which the new rule has a full conflict. A full conflict occurs when all the antecedents in the
            new rule conflict with all the antecedents declared in another rule.
               •      fuzzy system in —

            fuzzy system in specifies the complete information for a fuzzy system. Wire the fuzzy system out
           output from another VI to the fuzzy system in input of this VI.

               •     new rule —

         new rule specifies the new rule to integrate into the fuzzy system.

                     •      antecedents —

               antecedents specifies the antecedents, or IF portions, of the rule. Each antecedent consists
                  of three parts: the index of an input linguistic variable, an operator that specifies whether to
                  calculate the degree of membership or the degree of non-membership of the input
                    linguistic variable within a linguistic term, and the index of the linguistic term. The indexes
               correspond to the order in which the variables or linguistic terms were created.

               You can use the Build Array function or a loop to build an array of rule antecedents that you
                 create with the FL Create Antecedent VI. You then can wire the array to this input.

                           •      Var Index —

                  The index of an input linguistic variable.

                           •     MF Index —

                  The index of the linguistic term.

                           •     Cond —


5898   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5898 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5899 ordinal=5899 -->
## Functions

Functions


     An operator that specifies whether to calculate the degree of membership or the
      degree of non-membership of the linguistic variable within a linguistic term.


•      antecedent connective —

  antecedent connective specifies how this VI calculates the truth value of the aggregated
  rule antecedent.

   AND (Minimum)—Specifies that this VI uses the smallest degree of membership of the
  0   antecedents.
   AND (Product)—Specifies that this VI uses the product of the degrees of membership of  1   the antecedents.
  OR (Maximum)—Specifies that this VI uses the largest degree of membership of the  2   antecedents.
  OR (Probabilistic)—Specifies that this VI uses the probabilistic sum of the degrees of
  3 membership of the antecedents. The fuzzy logic controller uses the following equation to
    calculate the probabilistic sum: (A+ B) – (A* B), where Aand Bare the antecedents.

•      consequents —

  consequents specifies the consequents, or THEN portions, of the rule. Each consequent
  consists of three parts: the index of an output linguistic variable, an operator that specifies
  whether to calculate the degree of membership or the degree of non-membership of the
  output linguistic variable within a linguistic term, and the index of the linguistic term. The
  indexes correspond to the order in which the variables or linguistic terms were created.

  You can use the Build Array function or a loop to build an array of rule consequents that you
  create with the FL Create Consequent VI. You then can wire the array to this input.

      •      Var Index —

     The index of an output linguistic variable.

      •     MF Index —

     The index of the linguistic term.


                                                © National Instruments 5899

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5899 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5900 ordinal=5900 -->
## Functions

Functions


                           •     Cond —

                 An operator that specifies whether to calculate the degree of membership or the
                   degree of non-membership of the linguistic variable within a linguistic term.


                     •      consequent implication —

               consequent implication specifies the implication method this VI uses to scale the
              membership functions of the output linguistic variable based on the rule weight.

               0 Minimum—Specifies to use the Minimum implication method.
               1 Product—Specifies to use the Product implication method.

                     •      degree of support —

               degree of support specifies the weight, between 0 and 1, that you want to apply to the rule.
              The default is 1. Multiply the degree of support by the truth value of the aggregated rule
                antecedent to calculate the rule weight.


               •       error in (no error) —

             error in describes error conditions that occur before this node runs. This input provides
            standard error in functionality.

               •      fuzzy system out —

            fuzzy system out returns the complete information for a fuzzy system. Wire this output to the
            fuzzy system in input of another VI.

               •        all rule conflicts —

                all rule conflicts returns the indexes of all existing rules that have either partial or full conflicts
            with the new rule.

               •        full rule conflicts —

               full rule conflicts returns the indexes of existing rules that have full conflicts with the new rule.

               •       error out —


5900   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5900 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5901 ordinal=5901 -->
## Functions

Functions


    error out contains error information. This output provides standard error out functionality.

FLFL SystemSystem VIVI

Many Fuzzy Logic VIs contain a fuzzy system in or fuzzy system out parameter that
contains the complete information for a fuzzy system. Wire the fuzzy system out
output from one VI to the fuzzy system in input of another VI.


Data type

   •      fuzzy system —

     Specifies the complete information for a fuzzy system. Wire the fuzzy system out output from
    one VI to the fuzzy system in input of another VI.

         •      input variables —

        input variables specifies the input linguistic variables for the fuzzy system.

                •     name —

         name specifies the name of the linguistic variable.

                •      range —

            range specifies the minimum and maximum values of the linguistic variable.

                •     membership functions —

           membership functions specifies the linguistic terms for the linguistic variable and the
            degree of membership of the linguistic variable within those linguistic terms. Each
            element of the membership functions array corresponds to a linguistic term.

                      •     name —


                                                    © National Instruments 5901

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5901 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5902 ordinal=5902 -->
## Functions

Functions


                  name specifies the name of the membership function, or linguistic term, you want
                          to modify.

                                  •      shape —

                      shape specifies the shape of the function that determines the degrees of
                     membership for the linguistic variable.

                                  •      points —

                         points specifies the values of the linguistic variable corresponding to the base and
                        top points, in order from left to right and base to top, of the membership function.
                     The degree of membership of the linguistic variable within the linguistic term
                  name is 0 at the base points and 1 at the top points. Specify one point for a
                          singleton function, three points for a triangle function, and four points for
                           trapezoid, sigmoid, Gaussian, or user-defined functions.

                                  •       color —

                          color specifies the color of the membership function when you view the
                     membership function in the Fuzzy System Designer. You can wire a color box
                         constant to this input.

                                  •      user-defined shape index —

                         user-defined shape index specifies the index of the user-defined shape that
                        determines the degrees of membership for the linguistic variable. This parameter
                                  is applicable only if you set shape to User-Defined. Define the user-defined shapes
                            in the user-defined membership function shapes array in both the FL New Fuzzy
                      System VI and the User-Defined instance of the FL Create Membership Function VI.


                     •      output variables —

               output variables specifies the output linguistic variables for the fuzzy system.

                           •     name —


5902   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5902 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5903 ordinal=5903 -->
## Functions

Functions


  name specifies the name of the linguistic variable.

•      range —

  range specifies the minimum and maximum values of the linguistic variable.

•     membership functions —

  membership functions specifies the linguistic terms for the linguistic variable and the
  degree of membership of the linguistic variable within those linguistic terms. Each
  element of the membership functions array corresponds to a linguistic term.

      •     name —

     name specifies the name of the membership function, or linguistic term, you want
       to modify.

      •      shape —

      shape specifies the shape of the function that determines the degrees of
     membership for the linguistic variable.

      •      points —

      points specifies the values of the linguistic variable corresponding to the base and
      top points, in order from left to right and base to top, of the membership function.
     The degree of membership of the linguistic variable within the linguistic term
     name is 0 at the base points and 1 at the top points. Specify one point for a
       singleton function, three points for a triangle function, and four points for
       trapezoid, sigmoid, Gaussian, or user-defined functions.

      •       color —

       color specifies the color of the membership function when you view the
     membership function in the Fuzzy System Designer. You can wire a color box
      constant to this input.

      •      user-defined shape index —


                                             © National Instruments 5903

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5903 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5904 ordinal=5904 -->
## Functions

Functions


                         user-defined shape index specifies the index of the user-defined shape that
                        determines the degrees of membership for the linguistic variable. This parameter
                                  is applicable only if you set shape to User-Defined. Define the user-defined shapes
                            in the user-defined membership function shapes array in both the FL New Fuzzy
                      System VI and the User-Defined instance of the FL Create Membership Function VI.


                     •       rules —

                 rules specifies the rules for the fuzzy system. Use the input variables and output variables
                 to form the antecedents and consequents, respectively, of the rules.

                           •      antecedents —

                   antecedents specifies the antecedents, or IF portions, of the rule. Each antecedent
                      consists of three parts: the index of an input linguistic variable, an operator that
                       specifies whether to calculate the degree of membership or the degree of non-
                  membership of the input linguistic variable within a linguistic term, and the index of
                    the linguistic term. The indexes correspond to the order in which the variables or
                         linguistic terms were created.

                                  •      Var Index —

                     The index of an input linguistic variable.

                                  •     MF Index —

                     The index of the linguistic term.

                                  •     Cond —

                     An operator that specifies whether to calculate the degree of membership or the
                       degree of non-membership of the linguistic variable within a linguistic term.


                           •      antecedent connective —


5904   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5904 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5905 ordinal=5905 -->
## Functions

Functions


      antecedent connective specifies how this VI calculates the truth value of the
      aggregated rule antecedent.

      •      consequents —

      consequents specifies the consequents, or THEN portions, of the rule. Each
      consequent consists of three parts: the index of an output linguistic variable, an
      operator that specifies whether to calculate the degree of membership or the degree of
      non-membership of the output linguistic variable within a linguistic term, and the
      index of the linguistic term. The indexes correspond to the order in which the variables
      or linguistic terms were created.

             •      Var Index —

         The index of an output linguistic variable.

             •     MF Index —

         The index of the linguistic term.

             •     Cond —

         An operator that specifies whether to calculate the degree of membership or the
          degree of non-membership of the linguistic variable within a linguistic term.


      •      consequent implication —

      consequent implication specifies the implication method this VI uses to scale the
     membership functions of the output linguistic variable based on the rule weight.

      •      degree of support —

      degree of support specifies the weight, between 0 and 1, that you want to apply to the
        rule. The default is 1. Multiply the degree of support by the truth value of the
      aggregated rule antecedent to calculate the rule weight.


•       defuzzification method —


                                                © National Instruments 5905

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5905 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5906 ordinal=5906 -->
## Functions

Functions


                 defuzzification method specifies the defuzzification method this VI uses to convert the
                degrees of membership of output linguistic variables into numerical values.

                     •      description —

                 description specifies a description for the fuzzy system.

                     •      user MF interpolating polynomials —

                           •     X —

                           •      Y —

                           •       Y(x) coeff —

                           •       X(y) coeff —

                           •       Area(y) coeff —

                           •      coa_x(y) coeff —


    ExpressExpress

      Use the Express VIs and functions to build common measurement tasks.


         Palette
                       Description
        Object

         Input        Use the Input Express VIs to gather data or to acquire or simulate signals.


         Signal
                    Use the Signal Analysis Express VIs to perform waveform measurements, waveform
         Analysis


5906   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5906 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5907 ordinal=5907 -->
## Functions

Functions


 Palette               Description
 Object

               generation, and signal processing.


             Use the Output Express VIs to save data to files, to generate reports, to output real Output              world signals, to communicate with instruments, and to display messages to users.


 Signal       Use the Signal Manipulation Express VIs to manipulate signals and to perform data
 Manipulation type conversions.


 Execution    Use the Execution Control Express VIs and structures to add control and timing to
 Control         VIs.


 Arithmetic &  Use the Arithmetic & Comparison Express VIs and functions to perform arithmetic
 Comparison   functions and to compare Boolean values, strings, and numeric values.

InputInput

Use the Input Express VIs to gather data or to acquire or simulate signals.

      Note

      The DAQ Assistant Express VI does not appear on the Input palette unless you
       have NI-DAQmx installed. Refer to the DAQGettingStartedGuidefor
      more information about installing NI-DAQmx.

      The Instrument I/O Assistant Express VI does not appear on the Input palette
        unless you have the Instrument I/O Assistant installed. You install the
       Instrument I/O Assistant from the National Instruments Device Drivers DVD.


                                                    © National Instruments 5907

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5907 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5908 ordinal=5908 -->
## Functions

Functions


         Palette                       Description        Object

                    Use Instrument Drivers VIs to configure, control, and retrieve data from GPIB, serial,
                      modular, PXI, and other types of instruments. Use the NI Instrument Driver Finder to        Instrument                       search for and install instrument drivers. If an instrument driver is not available, you         Drivers                     can use the Create New Instrument Driver Project wizard to create a new instrument
                           driver.


        Simulate                      Simulates a sine wave, square wave, triangle wave, sawtooth wave, or noise signal.         Signal

        Simulate
          Arbitrary      Simulates a signal that you define.
         Signal

         Acquire       Acquires data from a sound device. This Express VI automatically configures an
       Sound        input task, acquires the data, and clears the task after the acquisition completes.


       Read From                    Reads data from a text-based measurement file (.lvm) or binary measurement file
        Measurement
                   (.tdm or .tdms).           File


       Prompt User   Displays a standard dialog box that prompts users to enter information, such as a
          for Input      user name and password.


           File Dialog     Displays a dialog box with which you can specify the path to a file or directory.


     InstrumentInstrument DriversDrivers

      Use Instrument Drivers VIs to configure, control, and retrieve data from GPIB, serial,
       modular, PXI, and other types of instruments. Use the NI Instrument Driver Finder to


5908   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5908 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5909 ordinal=5909 -->
## Functions

Functions

search for and install instrument drivers. If an instrument driver is not available, you
can use the Create New Instrument Driver Project wizard to create a new instrument
driver.

The VIs and controls that appear on this palette change depending on the instrument
drivers you install. You can add new VIs and controls to this palette. Before you begin
using the Instrument Driver VIs, make sure you choose the appropriate method of
instrument control.


SimulateSimulate SignalSignal

Simulates a sine wave, square wave, triangle wave, sawtooth wave, or noise signal.


Dialog Box Options

 Option   Description

          Contains the following options:

                  • Signal type—

             Type of waveform to simulate. You can simulate a sine wave, square wave, sawtooth
             wave, triangle wave, or noise (DC).

                  • Frequency (Hz)—
 Signal
             Frequency in hertz of the waveform. The default is 10.1.

                  • Phase (deg)—

                   Initial phase in degrees of the waveform. The default is 0.

                  • Amplitude—


                                                    © National Instruments 5909

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5909 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5910 ordinal=5910 -->
## Functions

Functions


        Option   Description

                     Amplitude of the waveform. The default is 1.

                              • Offset—

                 DC offset of the signal. The default is 0.

                              • Duty cycle (%)—

                     Percentage of time a square wave remains high versus low over one period. The
                       default is 50.

                              • Add noise—

                   Adds noise to the simulated waveform.

                              • Noise type—

                        Specifies the type of noise to add to the waveform. This option is available only when
                   you place a checkmark in the Add Noise checkbox.

                    You can add the following noise types:
          ◦ Uniform White Noise generates a signal that contains a uniformly distributed,
                      pseudorandom pattern whose values are in the range [-a:a], where ais the
                          absolute value of Amplitude.
          ◦ Gaussian White Noise generates a signal that contains a Gaussian-distributed,
                      pseudorandom pattern whose statistical profile is (µ,sigma) = (0,s), where sis
                          the absolute value of the specified Standard deviation.
          ◦  Periodic Random Noise generates a signal that contains periodic random noise
                           (PRN).
          ◦ Gamma Noise generates a signal that contains a pseudorandom pattern of
                           values that are the waiting times to the Order number event of a unit mean
                         Poisson process.
          ◦ Poisson Noise generates a signal that contains a pseudorandom sequence of
                           values that are the number of discrete events occurring in a given interval,
                            specified by Mean, of a unit rate Poisson process.
          ◦ Binomial Noise generates a signal that contains a binomially distributed,
                      pseudorandom pattern whose values are the number of occurrences of an
                           event, given the probability of that event occurring and the number of trials.
          ◦  Bernoulli Noise generates a signal that contains a pseudorandom pattern of
                        ones and zeros.


5910   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5910 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5911 ordinal=5911 -->
## Functions

Functions


Option   Description

      ◦ MLS Sequence generates a signal that contains a maximum length sequence of
                ones and zeros using a modulo-2 primitive polynomial of order Polynomial
                  order.
      ◦ Inverse F Noise generates a signal that contains a continuous noise waveform
                 with a power spectral density that is inversely proportional to frequency over a
                   specified frequency range.
                 • Noise amplitude—

          Maximum absolute value the signal can have. The default is 0.6. This option is
              available only when you select Uniform White Noise or Inverse F Noise from the
             Noise type pull-down menu.

                 • Standard deviation—

             Standard deviation of the noise you generate. The default is 0.6. This option is
              available only when you select Gaussian White Noise from the Noise type pull-down
           menu.

                 • Spectral amplitude—

            Magnitude of the frequency domain components of the simulated signal. The default
                  is 0.6. This option is available only when you select Periodic Random Noise from the
             Noise type pull-down menu.

                 • Order—

               Specifies the event number of the unit mean Poisson process. The default is 0.6. This
             option is available only when you select Gamma Noise from the Noise type pull-
          down menu.

                 • Mean—

               Specifies the interval of a unit rate Poisson process. The default is 0.6. This option is
              available only when you select Poisson Noise from the Noise type pull-down menu.

                 •  Trial probability—

              Probability that a given trial is TRUE. The default is 0.6. This option is available only
          when you select Binomial Noise from the Noise type pull-down menu.

                 • One probability—


                                                    © National Instruments 5911

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5911 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5912 ordinal=5912 -->
## Functions

Functions


        Option   Description

                        Specifies the probability that a given element of the signal is TRUE. The default is 0.6.
                       This option is available only when you select Bernoulli Noise from the Noise type
                     pull-down menu.

                              • Polynomial order—

                        Specifies the order of the modulo-2 primitive polynomial to use to generate the
                          signal. The default is 0.6. This option is available only when you select MLS Sequence
                    from the Noise type pull-down menu.

                              • Seed number—

                 When greater than 0, causes reseeding of the noise sample generator. The default is
                        –1. LabVIEW maintains the internal seed state independently for each instance of this
                       reentrant VI. For a specific instance of this VI, if Seed number is less than or equal to
                           0, LabVIEW does not reseed the noise generator, and the noise generator resumes
                     producing noise samples as a continuation of the previous noise sequence.

                              • Exponent—

                        Specifies the exponent of the inverse-f spectral shape you want. The default is 1. This
                      option is available only when you select Inverse F Noise from the Noise type pull-
                 down menu.

                 Contains the following options:

                              • Samples per second (Hz)—

                    Sampling rate in samples per second. The default is 1000.

                              • Number of samples—

                 Number of samples in the signal. The default is 100.        Timing
                              • Automatic—

                       Sets the Number of samples to be one-tenth of Samples per second (Hz).

                              •  Integer number of cycles—

                       Sets the nearest frequency and Number of samples such that the waveform contains


5912   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5912 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5913 ordinal=5913 -->
## Functions

Functions


Option   Description

           an integer number of cycles.

                 • Actual number of samples—

              Indicates the actual number of samples in the waveform when you select Integer
           number of cycles.

                 • Actual frequency—

              Indicates the actual frequency of the waveform when you select Integer number of
               cycles.

                 • Simulate acquisition timing—

             Simulates an acquisition rate comparable to an actual acquisition rate.

                 • Run as fast as possible—

             Simulates the signal as quickly as the system allows.

         Contains the following options:

                 • Absolute (date and time)—

              Displays the timestamp in terms of time elapsed since 12:00 a.m., Friday, January 1,
Time         1904, Universal Time [01-01-1904 00:00:00].
Stamps
                 •  Relative to start of measurement—

              Displays the timestamp in terms of seconds starting from zero. For example, 100 in
               relative time equals 1 minute and 40 seconds.

         Contains the following options:

                 • Reset phase, seed, and time stamps—
Reset
             Resets the phase to the phase value and the time stamp to zero. Resets the seed
Signal
           number to –1.

                 • Use continuous generation—


                                                    © National Instruments 5913

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5913 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5914 ordinal=5914 -->
## Functions

Functions


        Option   Description

                     Continuously simulates the signal. Does not reset the phase, time stamp, or seed
                    number.

                 Contains the following options:

                              • Use signal type name—

         Signal       Uses the default signal name.
      Name
                              • Signal name—

                      Contains the following options:

         Result                   Displays a preview of the signal to be simulated.
        Preview

      Inputs/Outputs

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       Offset —

             Specifies the DC offset of the signal. The default is 0. The value you wire to this input overrides
            the value you set in the configuration dialog box.

               •      Phase —

             Specifies the initial phase in degrees of the signal. The default is 0. The value you wire to this
            input overrides the value you set in the configuration dialog box.

               •      Amplitude —

             Specifies the amplitude of the signal. The default is 1. The value you wire to this input overrides
            the value you set in the configuration dialog box.

               •      Duty Cycle (%) —

             Specifies the percentage of time a square wave remains high versus low over one period. The


5914   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5914 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5915 ordinal=5915 -->
## Functions

Functions


  default is 50. The value you wire to this input overrides the value you set in the configuration
  dialog box.

•      Noise Amplitude —

  Specifies the maximum absolute value the signal can have. The default is 0.6. The value you wire
  to this input overrides the value you set in the configuration dialog box.

•      Standard deviation —

  Specifies the standard deviation of the noise you generate. The default is 0.6. The value you wire
  to this input overrides the value you set in the configuration dialog box.

•      Spectral amplitude —

  Specifies the magnitude of the frequency domain components of the simulated signal. The
  default is 0.6. The value you wire to this input overrides the value you set in the configuration
  dialog box.

•      Order —

  Specifies the event number of the unit mean Poisson process. The default is 0.6. The value you
  wire to this input overrides the value you set in the configuration dialog box.

•     Mean —

  Specifies the interval of a unit rate Poisson process. The default is 0.6. The value you wire to this
  input overrides the value you set in the configuration dialog box.

•       Trial probability —

  Specifies the probability that a given trial is TRUE. The default is 0.6. The value you wire to this
  input overrides the value you set in the configuration dialog box.

•     One probability —

  Specifies the probability that a given element of the signal is TRUE. The default is 0.6. The value
  you wire to this input overrides the value you set in the configuration dialog box.

•      Polynomial Order —

  Specifies the order of the modulo-2 primitive polynomial to use to generate the signal. The
  default is 0.6. The value you wire to this input overrides the value you set in the configuration


                                                   © National Instruments 5915

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5915 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5916 ordinal=5916 -->
## Functions

Functions


             dialog box.

               •      Exponent —

             Specifies the exponent of the inverse-f spectral shape you want. The default is 1. The value you
            wire to this input overrides the value you set in the configuration dialog box.

               •       Trials —

             Specifies the number of trials performed for each element of the simulated signal. The default is
               1. The value you wire to this input overrides the value you set in the configuration dialog box.

               •      Reset Signal —

             Specifies when to reset the signal. The value you wire to this input overrides the value you set in
            the configuration dialog box.

               •     Seed Number —

           Reseeds the noise sample generator when this value is > 0. The default is –1. If seed is 0, the
            noise generator does not reseed and resumes producing noise samples as a continuation of the
            previous noise sequence. The value you wire to this input overrides the value you set in the
             configuration dialog box.

               •      Frequency —

             Specifies the frequency in hertz of the waveform. The default is 10.1. The value you wire to this
            input overrides the value you set in the configuration dialog box.

               •      Signal —

            Returns the output signal formatted as dynamic data.

               •       error out —

            Contains error information. This output provides standard error out functionality.


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Amplitude and

5916   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5916 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5917 ordinal=5917 -->
## Functions

Functions

   Level Measurements.vi

SimulateSimulate ArbitraryArbitrary SignalSignal

Simulates a signal that you define.


Dialog Box Options

 Option          Description

                 Contains the following options:

                             • Define Signal—

                      Displays the Define Signal dialog box, which you use to generate an arbitrary
                         signal.

                             •  Start over when end of signal is reached—

                     Continuously simulates the signal you defined.
 Signal
 Specifications    ◦ X values repeat (0, 1, 2, 0, 1, 2)—

                        Repeats the xvalues when you select Start over when end of signal is
                         reached.

          ◦ X values continue (0, 1, 2, 3, 4, 5)—

                           Sequentially increments the xvalues when you select Start over when
                     end of signal is reached.

                 Contains the following options:

 Signal                   • One point per iteration—
 Generation
                     Simulates one point per iteration.


                                                    © National Instruments 5917

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5917 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5918 ordinal=5918 -->
## Functions

Functions


        Option          Description

                                         •  Entire signal each iteration—

                             Simulates the entire signal each iteration.

                                         • One defined Y point per iteration (no interpolation)—

                             Simulates one defined Y point per iteration without using interpolation.


         Signal Name     Specifies the name of the signal to display on the block diagram.


                          Displays a preview of the signal to be simulated.

                                         • Number of points—
         Result Preview
                               Displays the number of data points in the signal you defined in the Define
                               Signal dialog box.


      Inputs/Outputs

               •      Reset —

            Controls the initialization of the internal state of the VI. The default is FALSE.

               •      Next Value —

             Specifies the next value of the signal. The default is TRUE. If FALSE, the Express VI outputs the
          same value for each iteration.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Signal —

            Returns the output signal formatted as dynamic data.

               •       error out —


5918   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5918 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5919 ordinal=5919 -->
## Functions

Functions


    Contains error information. This output provides standard error out functionality.

   •      Data Valid —

     Indicates whether the data is valid.

AcquireAcquire SoundSound

Acquires data from a sound device. This Express VI automatically configures an input
task, acquires the data, and clears the task after the acquisition completes.

(Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
Open Sound System (OSS) driver to use this VI.


Dialog Box Options

 Option              Description

 Device                 Lists the sound devices you have connected.


 #Channels           Specifies the number of channels. 1 is Mono, and 2 is Stereo.


 Resolution (bits)     Specifies the quality of each sample in bits. The default is 16 bits.


 Duration (s)         Sets the number of seconds for which you want to acquire sound.


                                                    © National Instruments 5919

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5919 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5920 ordinal=5920 -->
## Functions

Functions


        Option              Description

       Sample rate (Hz)     Specifies the sample rate in hertz.


        Preview             Displays a preview of the sound operation in the graph.


       Graph Preview       Displays a preview of the sound operation.


      Inputs/Outputs

               •      Device —

               Lists the sound devices you have connected.

               •     Sample rate (Hz) —

             Specifies the sample rate in hertz.

               •      Resolution (bits) —

             Specifies the quality of each sample in bits. The default is 16 bits.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Duration (s) —

            Sets the number of seconds for which you want to acquire sound.

               •      #Channels —

             Specifies the number of channels. 1 is Mono, and 2 is Stereo.

               •      Data —

            Returns the data this Express VI acquires from the selected device using the settings you specify
              in the configuration dialog box.


5920   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5920 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5921 ordinal=5921 -->
## Functions

Functions


    You can convert this output to a waveform or one-dimensional array of waveforms (one per
    channel) by using the Convert from Dynamic Data function.

   •       error out —

    Contains error information. This output provides standard error out functionality.

ReadRead FromFrom MeasurementMeasurement FileFile

Reads data from a text-based measurement file (.lvm) or binary measurement file
(.tdm or .tdms).


Dialog Box Options

 Option    Description

            Displays the full path to the file from which you want to read data. The Express VI reads
           data from the file that this parameter specifies only if the Filename input is unwired. If Filename          you wire the Filename input, the VI reads data from the file that this input specifies
            instead.

           Contains the following options:

                    • Text (LVM)—

 File           Sets the file format to text-based measurement file (.lvm) and the file extension in
 Format         File Name to .lvm.

              To enable this VI to read data from generic text files, place a checkmark in the Read
               generic text files checkbox.


                                                    © National Instruments 5921

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5921 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5922 ordinal=5922 -->
## Functions

Functions


        Option    Description

                               • Binary (TDMS)—

                        Sets the file format to binary measurement file (.tdms) and the file extension in
                           File Name to .tdms.

                                      If you select this option, the Time Stamps and Generic Text File sections are not
                          available.

                               • Binary with XML Header (TDM)—

                     (Windows) Sets the file format to binary measurement file (.tdm) and the file
                       extension in File Name to .tdm.

                                      If you select this option, the Time Stamps and Generic Text File sections are not
                          available.

                  When you select this file format, you enable the Lock file for faster access
                      checkbox. Selecting this checkbox makes reading and writing significantly faster (at
                       the expense of the ability to multitask certain activities). It is recommended that
                    you use this option in most cases.

                        Note When this option is enabled, no two Express VIs can access the
                          same file at the same time when one of them is writing a "series of files."


                   Contains the following option:

                               • Ask user to choose file—         Action
                        Displays a dialog box that prompts users to select a file.

                   Contains the following options:

                               • Retrieve segments of original size—

       Segment      Retrieves segments of the signal from the file in the original size.
         Size
                               • Retrieve segments of specified size—

                        Retrieves segments of the signal using the size you specify in Samples.


5922   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5922 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5923 ordinal=5923 -->
## Functions

Functions


Option    Description

       ◦ Samples—

                    Specifies the number of samples you want to include in the segment size read
                 from the file. The default is 100. This option is available only when you select
                  the Retrieve segments of specified size option.

          Contains the following options:

                  •  Relative to start of measurement—

               Displays the timestamp in terms of seconds starting from zero. For example, 100 in
                 relative time equals 1 minute and 40 seconds.

Time           • Absolute (date and time)—
Stamps
               Displays the timestamp in terms of time elapsed since 12:00 a.m., Friday, January 1,
               1904, Universal Time [01-01-1904 00:00:00].

              Note These options are available only when you select the Text (LVM) option
                 from the File Format section.


          Contains the following options:

                  •  Start row of numeric data—

                Indicates the first row of numeric data. The Express VI begins reading data from this
               row. The default is 1.

                  •  First row is channel names—
Generic
                Specifies that the channel names are in the first row of the data file.Text File
                  •  First column is time channel—

                Specifies that the time data for each channel are in the first column of the data file.

                  • Read File Now—

              Imports the data from the file you specify in File Name into the Sample data table.


                                                    © National Instruments 5923

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5923 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5924 ordinal=5924 -->
## Functions

Functions


        Option    Description

                               • Sample data—

                        Displays the data from the file you specify in File Name when you click the Read
                           File Now button.

                     Note These options are available only when you select the Text (LVM) option
                         from the File Format section.


                   Contains the following options:

                               • Tab—

                     Uses tabs to delimit fields in the text file.

                               • Comma—         Delimiter
                     Uses a comma as the decimal separator.

                     Note These options are available only when you select the Text (LVM) option
                         from the File Format section.


                   Contains the following options:

                               •  . (dot)—

                     Uses a period as the decimal separator.

        Decimal       •  , (comma)—
         Point
                     Uses a comma as the decimal separator.

                     Note These options are available only when you select the Text (LVM) option
                         from the File Format section.


      Inputs/Outputs

               •      Enable —


5924   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5924 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5925 ordinal=5925 -->
## Functions

Functions


    Enables or disables the Express VI. The default is ON or TRUE.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Filename —

     Specifies the name of the file from which you want to read data.

   •      Reset —

    Resets the file position such that the next read starts at the beginning of the file.

   •      Signals —

    Contains the output signal or signals.

   •      Filename Out —

    Returns the name of the file.

   •     Comment —

    Returns the appended comment of each data set in the .lvm or .tdm file.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Description —

    Returns the description in the header of the .lvm or .tdm file.

   •     EOF? —

    Returns TRUE when the Express VI reaches the end of the file.


You also can use this VI to read Multisim data if you have Multisim 9.0 or later installed.
Use the Write To Measurement File Express VI to write data to a measurement file. You
also can use the Storage/DataPlugin VIs to read from and write to .tdm files.


                                                    © National Instruments 5925

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5925 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5926 ordinal=5926 -->
## Functions

Functions

           Note The behavior of this VI changes depending upon the target. If the
               current target does not or might not have a host computer connected, the
               configuration dialog box displays warnings next to options that are invalid
              without a host. If you configure this VI to prompt for input and run the VI on a
                target with no user interface, such as the Real-Time Module with no host
             computer connected, this VI returns an error.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\File IO\TDMS\Express Read and Write\TDMS
        Express Read Data (Time Domain).vi

     PromptPrompt UserUser forfor InputInput

       Displays a standard dialog box that prompts users to enter information, such as a user
     name and password.


      Dialog Box Options

        Option   Description

        Message
         to       Contains the text to display in the dialog box.
         Display

                  Contains the following options:

        Buttons      •  First button name—
         to
         Display       Specifies the text that appears on the first button. By default, the text on the first
                     button is OK.


5926   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5926 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5927 ordinal=5927 -->
## Functions

Functions


 Option   Description

                  • Second button name—

                Specifies the text that appears on the second button. By default, the text on the
             second button is Cancel. This option is available only when you place a checkmark
                 in the Display second button checkbox.

                  • Display second button—

                Specifies whether a second button is displayed in the dialog box.


           Specifies the name and data type of the controls that appear in the dialog box. The
           Inputs you list here are returned as outputs on the block diagram.
 Inputs          Input Name is the name of the control and instructs users what to enter into the control.
          Input Data Type is the type of control you want to use in the dialog box. You can choose
         from the following options: Number, Checkbox, or Text Entry Box.

          Contains the following options:

                  • Delete—

 Edit          Deletes the selected input.
 Inputs
                  • Insert—

                Inserts a new row in the Inputs list above the selected row.


 Window
          Contains the text to display in the title bar of the dialog box.
 Title

Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Enable —


                                                    © National Instruments 5927

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5927 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5928 ordinal=5928 -->
## Functions

Functions


            Enables or disables the Express VI. The default is ON or TRUE.

               •     OK —

            Returns TRUE when you click the first button in the dialog box and FALSE when you click the
           second button.

               •       error out —

            Contains error information. This output provides standard error out functionality.


           Note The behavior of this VI changes depending upon the target. If the
               current target does not or might not have a host computer connected, the
               configuration dialog box displays warnings next to options that are invalid
              without a host. If you configure this VI to prompt for input and run the VI on a
                target with no user interface, such as the Real-Time Module with no host
             computer connected, this VI returns an error.

       FileFile DialogDialog

       Displays a dialog box with which you can specify the path to a file or directory.

      You can use this dialog box to select existing files or directories or to select a location
      and name for a new file or directory.

      (macOS) This VI does not recognize macOS-specific means of specifying the default
       application for a file. However, you can use the pattern input to specify a file type for
         files that include an extension to the filename.


5928   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5928 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5929 ordinal=5929 -->
## Functions

Functions

Dialog Box Options

 Option    Description

         The user can select one or more files. When you de-select this option, the options for the
           types of files or folders the user can select appear dimmed.

                   •  files or folders—
               Contains the following options:
 Limit    ◦ File—The user can select only a file.
 selection   ◦ Folder—The user can select only a folder.
 to single   ◦  File or folder—The user can select either a file or a folder.
 item            • new or existing—
               Contains the following options:
       ◦ Existing—The user can select only an existing file or folder.
       ◦ New—The user only can enter the name of a new file or folder.
       ◦ New or existing—The user can select an existing file or folder or create a new
                           file or folder.


            Specifies that you can select a file from an LLB or a packed library. If this checkbox does
          not contain a checkmark, you can select an LLB or a packed library but you cannot
            select a file in an LLB or a packed library.
 Allow
 selection
               Note To select an LLB or packed library using the File Dialog Express VI, you of files in
                  can remove the checkmark from the Allow selection of files in LLBs and LLBs and
                 packed project libraries checkbox and select the LLB or packed library from packed
                   the file dialog box. You also can place a checkmark in the Allow selection of project
                         files in LLBs and packed project libraries checkbox, select the Files or libraries
                    Folders option button, choose an LLB or packed library from the file dialog
                    box, and select the second folder icon from the file list in the second file
                    dialog box that appears.


Inputs/Outputs

   •      button label —

    Label to display on the OK or Current Directory button in the file dialog box. If you configure the
    Express VI to allow the user to select directories, use this input to specify a label for the Current


                                                    © National Instruments 5929

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5929 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5930 ordinal=5930 -->
## Functions

Functions


            Directory button. If the configuration does not allow the user to select directories, use this input
             to specify a label for the OK button.

            For example, if you select Files only in the configure dialog box, the user must select an existing
                 file to which to append data, so you might want to wire Append to button label.

                    If button label is longer than the width of the button, the file dialog box does not display the
             entire label. For example, in an English version of Windows, the button is approximately 11
             characters wide.

               •      pattern (all files) —

              Restricts the files displayed in the dialog box to those whose name matches pattern (all files).
            pattern (all files) does not restrict the directories displayed.

          The pattern matching in this VI is similar to the matching used in matching wildcards in Windows
          and Linux filenames. If you specify characters other than the question mark character (?) or the
              asterisk character (*), the VI displays only files or directories that contain those characters. You
           can use the question mark character (?) to match any single character. You can use the asterisk
             character (*) to match any sequence of zero or more characters.

            For example, a pattern (all files) of *.vi;test*.llb returns matches for any file with a .vi
            extension and any file whose filename begins with test and has a .llb extension.

           To match multiple patterns, use a semicolon ( ; ) to separate the patterns. White space, such as
             blanks, tabs, and carriage returns, are taken literally. Avoid using white spaces unless they are
             part of the extension pattern. For example, if you use *.html;*.doc, the dialog box displays
                all files that end with .html and .doc. If you use *.html; *.doc, the dialog box displays
            only files that end with .html.

               •       start path —

            Path of the directory whose contents LabVIEW initially displays in the dialog box.

                    If start path is valid, but does not refer to an existing directory, LabVIEW strips names from the
          end of the path until the path is a valid directory path or an empty path. If start path is invalid or
            unwired, the last directory viewed in a file dialog box initially appears in the dialog box.

               •       default name —

         Name you want to appear as the initial file or directory name in the dialog box.

          The default is an empty string.


5930   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5930 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5931 ordinal=5931 -->
## Functions

Functions

•       error in —

  Describes error conditions that occur before this node runs.

•     prompt —

  Custom message that appears as the title of the file dialog box. (Windows and Linux) The default
  dialog box title is Choose or Enter Path of File. (macOS) The default dialog box title is Select File
  or Create New File.

•      pattern label —

  Label to display in the file dialog box next to the custom pattern.

   If you do not wire this input or it contains an empty string, the default label next to any custom
  pattern is Custom Pattern. If you do not wire a string to pattern, LabVIEW ignores this input.

•       error out —

  Contains error information. This output provides standard error out functionality.

•      selected path —

   Full path to the file or directory selected using this dialog box.

   If you cancel the dialog box, this VI sets selected path to <Not A Path>. This output is
  available if you place a checkmark in the Limit selection to single item checkbox in the
  Configure File Dialog dialog box.

•       exists —

   Is TRUE if selected path specifies an existing file or directory.

•      cancelled —

   Is TRUE if you cancel the dialog box.

•      selected paths —

  Contains the full path names to the files or directories selected using this dialog box. This output
   is available if you do not place a checkmark in the Limit selection to single item in the
  Configure File Dialog dialog box.


                                                   © National Instruments 5931

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5931 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5932 ordinal=5932 -->
## Functions

Functions

     SignalSignal AnalysisAnalysis

      Use the Signal Analysis Express VIs to perform waveform measurements, waveform
       generation, and signal processing.

           Note The VIs on this palette return an error if an input signal is a waveform
              with a dt less than or equal to zero.


         Palette Object  Description

         Spectral       Performs FFT-based spectral measurements, such as the averaged magnitude
        Measurements spectrum, power spectrum, and phase spectrum on a signal.


         Distortion      Performs distortion measurements on a signal, such as tone analysis, total
        Measurements harmonic distortion (THD), and signal in noise and distortion (SINAD).


                        Finds the single tone with the highest amplitude or searches a specified frequency        Tone
                       range to find the single tone with the highest amplitude. You also can find the        Measurements                       frequency and phase for a single tone.


        Dual Channel   Measures the frequency response of the input signals and the coherence based on
         Spectral       the current and previous input signals. This Express VI returns results such as
        Measurement  Magnitude, Phase, Coherence, Real, and Imaginary.

        Amplitude
       and Level      Performs voltage measurements on a signal.
        Measurements

        Timing and
                       Performs timing and transition measurements, such as frequency, period, or duty
         Transition
                           cycle, on a signal, usually a pulse.
        Measurements


5932   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5932 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5933 ordinal=5933 -->
## Functions

Functions


 Palette Object  Description

             Computes the coefficients that best represent the input data based on the chosen
 Curve Fitting             model type.


 Filter          Processes signals through filters and windows.


 Statistics       Returns the selected parameter of the first signal in a waveform.

 Convolution
 and           Performs convolution, deconvolution, or correlation on the input signals.
 Correlation

 Simulate                Simulates a sine wave, square wave, triangle wave, sawtooth wave, or noise signal. Signal

 Mask and               Performs limit testing on Signals.
 Limit Testing

 Create             Computes a histogram for Signal. Histogram

SpectralSpectral MeasurementsMeasurements

Performs FFT-based spectral measurements, such as the averaged magnitude
spectrum, power spectrum, and phase spectrum on a signal.


                                                    © National Instruments 5933

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5933 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5934 ordinal=5934 -->
## Functions

Functions

      Dialog Box Options

        Option        Description

                       Contains the following options:

                                     • Magnitude (peak)—

                         Measures the spectrum and displays the results in terms of peak amplitude.

                        You typically use this measurement with more advanced measurements that
                             require magnitude and phase information. The magnitude of the spectrum is
                        measured in peak values. For example, a sine tone of amplitude A yields a
                        magnitude spectral value of A at the sine tone frequency. You can unwrap the
                         phase spectrum or convert it from radians to degrees by setting Phase to
                      Unwrap phase or Convert to degree, respectively. If you place a checkmark in
                           the Averaging checkbox, the phase of the spectrum is zero for averaging.

                                     • Magnitude (RMS)—

                         Measures the spectrum and displays the results in terms of root-mean-square
                            (RMS).

        Selected         You typically use this measurement with more advanced measurements that
       Measurement      require magnitude and phase information. The magnitude of the spectrum is
                        measured in RMS values. For example, a sine tone of amplitude A yields a
                        magnitude spectral value of 0.707*A at the sine tone frequency. You can
                       unwrap the phase spectrum or convert it from radians to degrees by setting
                        Phase to Unwrap phase or Convert to degree, respectively. If you place a
                        checkmark in the Averaging checkbox, the phase of the spectrum is zero for
                            averaging.

                                     • Power spectrum—

                         Measures the spectrum and displays the results in terms of power. All phase
                           information is lost in the computation.

                        You typically use this measurement to examine the various frequency
                        components of a signal. While averaging to compute a power spectrum does
                          not reduce the unwanted noise in a system, averaging is useful because it
                           provides a reliable statistical estimate of the level of random signals measured.

                                     • Power spectral density—


5934   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5934 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5935 ordinal=5935 -->
## Functions

Functions


Option        Description

                 Measures the spectrum and displays the results in terms of power spectral
                   density (PSD).

               Power spectral density is a scaled version of Power spectrum, where the
                power present within each spectral bin is normalized by the frequency bin
                   width. You typically use this measurement to examine the noise floor of a
                    signal or the power in a specific frequency range. Normalizing the power
                 spectrum by the bin width makes this measurement independent of the signal
                    duration, or number of samples.

              Contains the following options:

                         • Linear—

                  Returns the results in terms of the original units.Result
                         • dB—

                  Returns the results in terms of decibels (dB).


                Specifies the window to apply to the signal.

                         • None does not apply a window to Signals.
                         • Hanning applies a Hanning window to Signals.
                         • Hamming applies a Hamming window to Signals.
                         • Blackman-Harris applies a Blackman-Harris window to Signals.
                         • Exact Blackman applies an exact Blackman window to Signals.
Window                         • Blackman applies a Blackman window to Signals.
                         •  Flat Top applies a Flat Top window to Signals.
                         • 4 Term B-Harris applies a Four Term Blackman-Harris window to Signals.
                         • 7 Term B-Harris applies a Seven Term Blackman-Harris window to Signals.
                         • Low Sidelobe applies a Low Sidelobe window to Signals.

               Refer to the Scaled Time Domain Window VI for information about coefficients and
            window parameters for each window type.

Averaging      Specifies whether the Express VI performs averaging.

Mode         Contains the following options:

                                                    © National Instruments 5935

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5935 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5936 ordinal=5936 -->
## Functions

Functions


        Option        Description

                                     • Peak hold—

                          Performs averaging at each frequency line separately, retaining peak levels
                         from one FFT record to the next.

                                     • Vector—

                       Computes the average of complex FFT spectrum quantities directly. Vector
                           averaging eliminates noise from synchronous signals.

                                     • RMS—

                           Averages the energy, or power, of the FFT spectrum of the signal.

                       Contains the following options:

                                     • Linear—

                           Returns the results in terms of the original units.

        Weighting          • Exponential—

                              Specifies exponential averaging, which averages over the number of packets
                        you specify in Number of Averages in a weighted manner. Exponential
                           averaging gives the most recent packets more weighting in the average than
                            older packets.


       Number of
                         Specifies the number of packets to average. The default is 10.
        Averages

                       Contains the following options:

                                     • Every iteration—

                           Returns the spectrum after every iteration of the Express VI.        Produce
       Spectrum                                     • Only when averaging complete—

                           Returns the spectrum only after the Express VI gathers the number of packets
                        you specify in Number of Averages.


5936   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5936 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5937 ordinal=5937 -->
## Functions

Functions


 Option        Description

               Contains the following options:

                          • Unwrap phase—

                   Enables phase unwrapping on the output phase. Phase
                          • Convert to degree—

                   Returns the phase in degrees.


                Displays the first channel of Signals. This graph displays the incoming signal with
             windowing applied.
 Windowed
 Input Signal     If you wire data to the Express VI and run it, Windowed Input Signal displays real
                data. If you close and reopen the Express VI, Windowed Input Signal displays
              sample data until you run the VI again.


                Displays a preview of the magnitude measurement of the signal.
 Magnitude
 Result              If you wire data to the Express VI and run it, Magnitude Result Preview displays real
 Preview       data. If you close and reopen the Express VI, Magnitude Result Preview displays
              sample data until you run the VI again.


               Contains the following options:
 Phase Result                         If you wire data to the Express VI and run it, Phase Result Preview displays real
 Preview                data. If you close and reopen the Express VI, Phase Result Preview displays sample
               data until you run the VI again.


Inputs/Outputs

   •      Restart Averaging — Specifies whether to restart the selected averaging process. The
     default is FALSE. When you call this Express VI for the first time, the averaging process starts
    automatically.

    This input appears only if you place a checkmark in the Averaging checkbox.


                                                    © National Instruments 5937

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5937 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5938 ordinal=5938 -->
## Functions

Functions

               •       error in (no error) —
            Describes error conditions that occur before this node runs.
               •      Signals —
            Contains the input signal or signals.
               •       error out —
            Contains error information. This output provides standard error out functionality.
               •     FFT - (RMS) — Returns the FFT magnitude spectrum and displays the results in RMS units.
               •     Power Spectrum — Returns the FFT power spectrum and displays the results in RMS-
           squared units.

           To compute the FFT power spectrum, LabVIEW converts the two-sided power spectrum to the
             single-sided power spectrum.

               •     PSD — Returns the FFT power spectral density and displays the results in RMS-squared per
          Hz units.
               •     FFT - (Peak) — Returns the FFT magnitude spectrum and displays the results in peak units.
               •      averaging done — Returns TRUE when the number of averages completed equals or
            exceeds Number of Averages.
               •      Phase —
            Returns the FFT phase spectrum and displays the results in degrees or radians.

                     •       f0 —

                     •       df —

                     •      phase —


      FFT-based spectral computations assume that the finite block of signal data represents
      one period of a periodic signal. The computed spectrum of this effective periodically
      extended signal shows energy spreading into frequencies that were not present in the
        original signal. To reduce this spectral leakage, use smoothing windows to taper the
      sharp transitions in the effective signal. You do not typically use windows if you can
       acquire an integer number of cycles of each frequency component measured or if you
       are analyzing noise spectra.

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Spectral

5938   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5938 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5939 ordinal=5939 -->
## Functions

Functions

   Measurements.vi
  • labview\examples\Express VIs\Express VI - Filter.vi

DistortionDistortion MeasurementsMeasurements

Performs distortion measurements on a signal, such as tone analysis, total harmonic
distortion (THD), and signal in noise and distortion (SINAD).


Dialog Box Options

 Option     Description

            Contains the following options:

                     • SINAD (dB)—

                 Calculates the measured signal in noise and distortion (SINAD). SINAD is defined
                as the dB of the ratio of the RMS energy of Signals to the RMS energy of Signals
                   less the energy in the fundamental. To compute the THD Plus Noise in dB, negate
                the SINAD.

                     •  Total harmonic distortion—

              Computes the measured total harmonic distortion up to and including the highest
                harmonic. THD is defined as the ratio of the RMS sum of the harmonics to the
 Distortion      amplitude of the fundamental tone. To compute THD as a percentage, multiply it
               by 100.

                     •  Specific harmonic level—

                Returns the harmonic you specify.

                     • Harmonic number (fundamental = 1)—

                  Specifies the harmonic to measure. This option is available only when you select
                  Specific harmonic level.

                     • Stop search at Nyquist—


                                                    © National Instruments 5939

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5939 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5940 ordinal=5940 -->
## Functions

Functions


        Option     Description

                          Specifies to include only frequencies less than the Nyquist frequency, or half the
                       sampling rate, in the harmonic search. This option is available only when you
                           select Total harmonic distortion or Specific harmonic level.

                   When you remove the checkmark from the Stop search at Nyquist checkbox, this
                            VI continues searching the frequency domain beyond the Nyquist frequency by
                      assuming that the higher frequency components have aliased according to the
                         following equation: aliased f = Fs – (f modulo Fs) where Fs = 1/dt = sampling rate

                                 • Highest harmonic—

                         Controls the highest harmonic, including the fundamental tone, to use for the
                      harmonic analysis. For example, for third harmonic analysis, set Highest
                     harmonic to 3 to measure the fundamental, second, and third harmonic. This
                        option is available only when you select Total harmonic distortion or Specific
                     harmonic level.

                    Contains the following options:

                                 • Search for fundamental frequency—

                         Controls the frequency domain search area, which is the center frequency and
                         width, to use for finding the fundamental tone frequency of the signal.

           ◦ Approximate frequency—

                            Center frequency to use in the frequency domain search for the fundamental
        Search             tone frequency. The default is 0. If you set Approximate frequency to –1, this
        Frequency          Express VI uses the tone with the highest amplitude as the fundamental tone.
                             This option is available only when you place a checkmark in the Search for
                         fundamental frequency checkbox.

           ◦ Search (+/- % of approx. freq.)—

                          Frequency width, as a percentage of the sampling rate, to use for the
                            frequency domain search for the fundamental tone frequency. The default is
                                  5. This option is available only when you place a checkmark in the Search for
                         fundamental frequency checkbox.


5940   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5940 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5941 ordinal=5941 -->
## Functions

Functions


 Option     Description

             Displays the measurements you configured this Express VI to perform and the
             calculated values of those measurements. You can click any measurement listed in the Results          Measurement column, and the corresponding value or plot appears in the Result
           Preview graph.


             Displays the input signal.
 Input                    If you wire data to the Express VI and run it, Input Signal displays real data. If you close
 Signal          and reopen the Express VI, Input Signal displays sample data until you run the Express
              VI again.


             Displays a preview of the measurement. The Result Preview plot indicates the value of
            the selected measurement with a dotted line.
 Result                    If you wire data to the Express VI and run the VI, Result Preview displays real data. If
 Preview           you close and reopen the Express VI, Result Preview displays sample data until you run
            the VI again. If the cutoff frequency values are invalid, Result Preview does not display
              valid data.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •     SINAD (dB) —

    Returns the measured signal in noise and distortion (SINAD). SINAD is defined as the dB of the
     ratio of the RMS energy of Signals to the RMS energy of Signals less the energy in the


                                                    © National Instruments 5941

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5941 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5942 ordinal=5942 -->
## Functions

Functions


            fundamental. To compute the THD Plus Noise in dB, negate the SINAD.

               •       Specific Harmonic —

            Returns the harmonic you specify in Specific harmonic level.

               •     THD —

            Returns the measured total harmonic distortion up to and including the highest harmonic. To
          compute THD as a percentage, you must multiply it by 100.

     ToneTone MeasurementsMeasurements

       Finds the single tone with the highest amplitude or searches a specified frequency
      range to find the single tone with the highest amplitude. You also can find the
       frequency and phase for a single tone.


      Dialog Box Options

        Option         Description

                        Contains the following options:

                                       • Amplitude—

                              Calculates the amplitude of the detected single tone in volts peak (Vp).

         Single Tone          • Frequency—
       Measurements
                              Calculates the frequency of the detected single tone in Hertz.

                                       • Phase—

                              Calculates the phase of the detected single tone in degrees.


5942   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5942 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5943 ordinal=5943 -->
## Functions

Functions


Option         Description

               Contains the following options:

                          • Approximate frequency (Hz)—

                   Center frequency to use in the frequency domain search for the single tone.
                 The default is 10. This option is available only when you place a checkmark in
Search for          the Search for Specific Frequency checkbox.
Specific
Frequency           • Search (+/- % of approx. freq.)—

                  Frequency width, as a percentage of the sampling rate, for the frequency
                 domain search for the single tone frequency. The default is 5. This option is
                     available only when you place a checkmark in the Search for Specific
                  Frequency checkbox.


                Displays the measurements you configured this Express VI to perform and the
                calculated values of those measurements. You can click any measurement listed inResults
               the Measurement column, and the corresponding value or plot appears in the
               Result Preview graph.


                Displays the input signal.

Input Signal      If you wire data to the Express VI and run it, Input Signal displays real data. If you
                close and reopen the Express VI, Input Signal displays sample data until you run
               the Express VI again.


                Displays a preview of the measurement. The Result Preview plot indicates the
                value of the selected measurement with a dotted line.
Result                         If you wire data to the Express VI and run the VI, Result Preview displays real data.
Preview                         If you close and reopen the Express VI, Result Preview displays sample data until
              you run the VI again. If the cutoff frequency values are invalid, Result Preview does
               not display valid data.


Approximate   Center frequency to use in the frequency domain search for the single tone. The
frequency (Hz)  default is 10. This option is available only when you place a checkmark in the


                                                    © National Instruments 5943

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5943 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5944 ordinal=5944 -->
## Functions

Functions


        Option         Description

                      Search for Specific Frequency checkbox.


      Inputs/Outputs

               •      Signals —

            Contains the input signal or signals.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Phase —

            Returns the phase of the detected single tone in degrees.

               •      Frequency —

            Returns the frequency of the detected single tone in Hertz.

               •      Amplitude —

            Returns the amplitude of the detected single tone in volts peak (Vp).


     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Filter.vi

     DualDual ChannelChannel SpectralSpectral MeasurementMeasurement

      Measures the frequency response of the input signals and the coherence based on the
       current and previous input signals. This Express VI returns results such as Magnitude,

5944   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5944 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5945 ordinal=5945 -->
## Functions

Functions

Phase, Coherence, Real, and Imaginary.


Dialog Box Options

 Option       Description

               Specifies how to handle multiple signals in each input.

                        • Ordered pairs—

                   Calculates the frequency response of the first channel in Input Signal A against
                  the first channel in Input Signal B, then the second channel in Input Signal A
                   against the second channel in Input Signal B, and so on.

        ◦  If there is one channel on Input Signal A and one channel on Input Signal B,
                      the result is one output.
        ◦  If there are multiple channels on Input Signal A and one channel on Input
                      Signal B, the analysis result is the first channel in Input Signal A against the
                        single channel in Input Signal B. The rest of the channels in Input Signal A
                      are ignored and the VI returns a warning.
        ◦  If there is one channel on Input Signal A and multiple channels on Input
                      Signal B, the analysis result is the single channel in Input Signal A against Input                      the first channel in Input Signal B. The rest of the channels in Input Signal B
 Comparison                      are ignored and the VI returns a warning.
        ◦  If there are multiple channels on both Input Signal A and Input Signal B, the
                        analysis result is the first channel in Input Signal A against the first channel
                         in Input Signal B, the second channel in Input Signal A against the second
                     channel in Input Signal B, and so on. If there is a mismatched number of
                      channels, the VI ignores unmatched channels and returns a warning.
        ◦  If either Input Signal is empty, the result is empty and the VI returns an error.
                        •  All cross pairs—

                   Calculates the frequency response of the first channel in Input Signal A against
                each channel in Input Signal B, then the second channel in Input Signal A
                   against each channel in Input Signal B, and so on.

        ◦  If there is one channel on Input Signal A and one channel on Input Signal B,
                      the result is one output.


                                                    © National Instruments 5945

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5945 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5946 ordinal=5946 -->
## Functions

Functions


        Option       Description

            ◦  If there are multiple channels on Input Signal A and one channel on Input
                              Signal B, the analysis result is the first channel in Input Signal A against the
                                 single channel in Input Signal B, then the second channel in Input Signal A
                               against the single channel in Input Signal B, and so on. The output contains
                              the same number of signals as Input Signal A.
            ◦  If there is one channel on Input Signal A and multiple channels on Input
                              Signal B, the analysis result is the single channel in Input Signal A against
                              the first channel in Input Signal B, then the single channel in Input Signal A
                               against the second channel in Input Signal B, and so on. The output
                               contains the same number of signals as Input Signal B.
            ◦  If there are Mchannels on Input Signal A and Nchannels on Input Signal B,
                              the analysis result is the matrix set of Input Signal A versus Input Signal B.
                          The signals are returned in the order 1-1, ... 1-N, 2-1, ... M-N.
            ◦  If either Input Signal is empty, the result is empty and the VI returns an error.

                     Contains the following options:

                                   • Magnitude—

                           Select to include magnitude results in the output.

            ◦ dB—

                                Select to return the magnitude results in decibels. Remove the checkmark
                           from this checkbox to return the magnitude results in the original units.

        Frequency        • Phase—
        Response
        Function         Select to include phase results in the output. Select Unwrap phase to return the
                       phase results in radians. Select Convert to degree to return the phase results in
                          degrees.

            ◦ Unwrap phase—

                                Select to return the phase results in radians.

            ◦ Convert to degree—

                                Select to return the phase results in degrees.


5946   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5946 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5947 ordinal=5947 -->
## Functions

Functions


Option       Description

                      • Real—

                  Select to include real results in the output.

                      • Imaginary—

                  Select to include imaginary results in the output.

                      • Coherence—

                  Select to include coherence results in the output.


              Specifies the window to apply to the signal.

                      • None does not apply a window to Signals.
                      • Hanning applies a Hanning window to Signals.
                      • Hamming applies a Hamming window to Signals.
                      • Blackman-Harris applies a Blackman-Harris window to Signals.
                      • Exact Blackman applies an exact Blackman window to Signals.
Window                      • Blackman applies a Blackman window to Signals.
                      •  Flat Top applies a Flat Top window to Signals.
                      • 4 Term B-Harris applies a Four Term Blackman-Harris window to Signals.
                      • 7 Term B-Harris applies a Seven Term Blackman-Harris window to Signals.
                      • Low Sidelobe applies a Low Sidelobe window to Signals.

              Refer to the Scaled Time Domain Window VI for information about coefficients and
           window parameters for each window type.

Averaging    Specifies whether the Express VI performs averaging.

             Contains the following options:

                      • Vector—

               Computes the average of complex quantities directly.Mode
                      • RMS—

                 Averages the energy, or power, of the signal.


                                                    © National Instruments 5947

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5947 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5948 ordinal=5948 -->
## Functions

Functions


        Option       Description

                     Contains the following options:

                                   • Linear—

                            Specifies linear averaging, which averages over the number of packets you
                            specify in Number of Averages in a non-weighted manner.
        Weighting
                                   • Exponential—

                            Specifies exponential averaging, which averages over the number of packets you
                            specify in Number of Averages in a weighted manner. Exponential averaging
                           gives the most recent packets more weighting in the average than older packets.


       Number of
                        Specifies the number of packets to average. The default is 10.        Averages

                     Contains the following options:

                                   • Every iteration—

                         Returns the spectrum after every iteration of the Express VI.        Produce
       Spectrum                                   • Only when averaging complete—

                         Returns the spectrum only after the Express VI gathers the number of packets
                       you specify in Number of Averages.


                       Displays the first channel of Input Signal A. This graph displays the first incoming
                        signal with windowing applied.       Windowed
        Input Signal                                   If you wire data to the Express VI and run it, Windowed Input Signal A displays real
       A                       data. If you close and reopen the Express VI, Windowed Input Signal A displays
                   sample data until you run the VI again.


                       Displays the first channel of Input Signal B. This graph displays the second incoming       Windowed
                        signal with windowing applied.        Input Signal
       B                                   If you wire data to the Express VI and run it, Windowed Input Signal B displays real


5948   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5948 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5949 ordinal=5949 -->
## Functions

Functions


Option       Description

              data. If you close and reopen the Express VI, Windowed Input Signal B displays
            sample data until you run the VI again.


                     If you wire data to the Express VI and run it, Results displays real data. If you close
           and reopen the Express VI, Results displays sample data until you run the VI again.

                      • Magnitude—

                  Select to include magnitude results in the output.

                  This page appears only if you place a checkmark in the Magnitude checkbox.

                      • Phase—

                  Select to include phase results in the output. Select Unwrap phase to return the
               phase results in radians. Select Convert to degree to return the phase results in
                  degrees.

                  This page appears only if you place a checkmark in the Phase checkbox.
Results
                      • Real—

                  Select to include real results in the output.

                  This page appears only if you place a checkmark in the Real checkbox.

                      • Imaginary—

                  Select to include imaginary results in the output.

                  This page appears only if you place a checkmark in the Imaginary checkbox.

                      • Coherence—

                  Select to include coherence results in the output.

                  This page appears only if you place a checkmark in the Coherence checkbox.


                                                    © National Instruments 5949

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5949 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5950 ordinal=5950 -->
## Functions

Functions

      Inputs/Outputs

               •      Input Signal A —

            Contains the first input signal or signals. This is assumed to be the excitation. The input signals
          must have the same number of data points, t0, and dt. If they do not, an error is returned.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Restart Averaging (F) —

             Specifies whether to restart the selected averaging process. The default is FALSE. When you call
              this Express VI for the first time, the averaging process starts automatically.

             This input appears only if you place a checkmark in the Averaging checkbox.

               •      Input Signal B —

            Contains the second input signal or signals. This is assumed to be the response. The input
             signals must have the same number of data points, t0, and dt. If they do not, an error is returned.

               •      Magnitude —

          The magnitude from the frequency response calculations.

             This output appears only if you place a checkmark in the Magnitude checkbox.

               •      Imaginary —

          The imaginary part from the frequency response calculations.

             This output appears only if you place a checkmark in the Imaginary checkbox.

               •      Real —

          The real part from the frequency response calculations.

             This output appears only if you place a checkmark in the Real checkbox.

               •      Averaging Done —

            Returns TRUE when the number of averages completed equals or exceeds Number of Averages.


5950   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5950 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5951 ordinal=5951 -->
## Functions

Functions


    This output appears only if you place a checkmark in the Averaging checkbox.

   •      Coherence —

    The coherence from the frequency response calculations.

    This output appears only if you place a checkmark in the Coherence checkbox.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Phase —

    The phase from the frequency response calculations.

    This output appears only if you place a checkmark in the Phase checkbox.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Dual Channel
   Spectral Measurement.vi

AmplitudeAmplitude andand LevelLevel MeasurementsMeasurements

Performs voltage measurements on a signal.


Dialog Box Options

 Option         Description

 Amplitude
                Contains the following options:
 Measurements


                                                    © National Instruments 5951

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5951 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5952 ordinal=5952 -->
## Functions

Functions


        Option         Description

                                       • Mean (DC)—

                             Acquires a DC measurement of Signals.

                                       • RMS—

                              Calculates the root mean square value of Signals.

                                       • Apply window—

                             Applies a low side lobe window to Signals. This option is available only when
                         you place a checkmark in the DC or RMS checkbox.

                         Use smoothing windows to taper the sharp transitions in the effective signal.
                         You do not typically use windows if you can acquire an integer number of
                              cycles of the signal or if you are analyzing noise spectra.

                                       •  Positive peak—

                          Measures the most positive peak in Signals.

                                       • Negative peak—

                          Measures the most negative peak in Signals.

                                       • Peak to peak—

                          Measures the most positive peak to the most negative peak in Signals.

                                       • Cycle average—

                          Measures the mean level of one complete period of a periodic input signal.

                                       • Cycle RMS—

                              Calculates the root mean square value of one complete period of a periodic
                             input signal.


                         Displays the measurements you configured this Express VI to perform and the
         Results
                         calculated values of those measurements. You can click any measurement listed in


5952   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5952 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5953 ordinal=5953 -->
## Functions

Functions


 Option         Description

                the Measurement column, and the corresponding value or plot appears in the
                Result Preview graph.


                 Displays the input signal.

 Input Signal      If you wire data to the Express VI and run it, Input Signal displays real data. If you
                 close and reopen the Express VI, Input Signal displays sample data until you run
                the Express VI again.


                 Displays a preview of the measurement. The Result Preview plot indicates the
                value of the selected measurement with a dotted line.
 Result                          If you wire data to the Express VI and run the VI, Result Preview displays real data.
 Preview                          If you close and reopen the Express VI, Result Preview displays sample data until
              you run the VI again. If the cutoff frequency values are invalid, Result Preview does
                not display valid data.


Inputs/Outputs

   •      Restart Averaging —

     Specifies whether to restart the selected averaging process. The default is FALSE. When you call
     this Express VI for the first time, the averaging process starts automatically.

    This input appears only if you place a checkmark in the Averaging checkbox.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Signals —

    Contains the input signal or signals.

   •     Mean (DC) —

    Returns the measured DC value of Signals.


                                                    © National Instruments 5953

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5953 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5954 ordinal=5954 -->
## Functions

Functions

               •      Negative Peak —

            Returns a measurement of the most negative peak in Signals.

               •      Cycle Average —

            Returns the mean level of one complete period of a periodic input signal.

          The cycle average of a perfect sine wave is zero, but the average level of the entire signal can be
           nonzero as a result of partial periods at the boundaries of the signal.

               •       Positive Peak —

            Returns a measurement of the most positive peak in Signals.

               •     RMS —

            Returns the calculated RMS of the values in Signals.

               •      Cycle RMS —

            Returns the root mean square value of one complete period of a periodic input signal.

               •      Cycle Average —

            Returns the mean level of one complete period of a periodic input signal. The cycle average of a
             perfect sine wave is zero, but the average level of the entire signal can be nonzero as a result of
              partial periods at the boundaries of the signal.

               •      Cycle RMS —

            Returns the root mean square value of one complete period of a periodic input signal.

               •     Mean (DC) —

            Returns the measured DC value of Signals.

               •      Negative Peak —

            Returns a measurement of the most negative peak in Signals.

               •     Peak to Peak —

            Returns a measurement from the most positive peak to the most negative peak in Signals.

               •       Positive Peak —

5954   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5954 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5955 ordinal=5955 -->
## Functions

Functions


    Returns a measurement of the most positive peak in Signals.

   •     RMS —

    Returns the calculated RMS of the values in Signals.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •     Peak to Peak —

    Returns a measurement from the most positive peak to the most negative peak in Signals.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Amplitude and
   Level Measurements.vi

TimingTiming andand TransitionTransition MeasurementsMeasurements

Performs timing and transition measurements, such as frequency, period, or duty
cycle, on a signal, usually a pulse.


Dialog Box Options

 Option         Description

                Contains the following options:
 Timing and
                           • Frequency— Transition
 Measurements                     Calculates the frequency of Signals in Hertz.


                                                    © National Instruments 5955

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5955 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5956 ordinal=5956 -->
## Functions

Functions


        Option         Description

                                       • Period—

                              Calculates the time in seconds between adjacent middle reference level
                              crossings in the same direction. The reciprocal of this value is the signal
                             frequency.

                                       • Pulse duration—

                              Calculates the time difference in seconds between the first two middle
                             reference level crossings. Pulse duration also is known as pulse width.

                                       • Duty cycle—

                              Calculates the Pulse duration as a fraction of the Period.


                                       • Preshoot (%)—

                              Calculates the height of the local minimum that precedes a rising transition or
                            the local maximum that precedes a falling transition as a percentage of the
                           histogram-based amplitude of the signal.

                                       • Overshoot (%)—

                              Calculates the height of the local maximum that follows a rising transition or
                            the local minimum that follows a falling transition as a percentage of the
                           histogram-based amplitude of the signal.

                                       • Slew rate—

                              Calculates the ratio between (90% amplitude – 10% amplitude) and the rise
                              time.


                         Displays the measurement you configured this Express VI to perform and the
                         calculated value of that measurement. You can click any measurement listed in the
         Results
                    Measurement column, and the corresponding value or plot appears in the Result
                      Preview graph.


5956   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5956 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5957 ordinal=5957 -->
## Functions

Functions


 Option         Description

                 Displays the input signal.

 Input Signal      If you wire data to the Express VI and run it, Input Signal displays real data. If you
                 close and reopen the Express VI, Input Signal displays sample data until you run
                the Express VI again.


                 Displays the measurement you configured this Express VI to perform and the
                 calculated value of that measurement. You can click any measurement listed in the
              Measurement column, and the corresponding value or plot appears in the Result
               Preview graph. Result
 Preview                          If you wire data to the Express VI and run the VI, Result Preview displays real data.
                          If you close and reopen the Express VI, Result Preview displays sample data until
              you run the VI again. If the cutoff frequency values are invalid, Result Preview does
                not display valid data.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •      Duration —

    Returns the time difference in seconds between the first two middle reference level crossings.

   •      Preshoot —

    Returns the height of the local minimum that precedes a rising transition or the local maximum
    that precedes a falling transition as a percentage of the histogram-based amplitude of the signal.


                                                    © National Instruments 5957

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5957 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5958 ordinal=5958 -->
## Functions

Functions

               •      Slew Rate —

            Returns the ratio between (90% amplitude – 10% amplitude) and the rise time.

               •      Frequency —

            Returns the frequency of Signals in Hertz.

               •      Overshoot —

            Returns the height of the local maximum that follows a rising transition or the local minimum
             that follows a falling transition as a percentage of the histogram-based amplitude of the signal.

               •      Period —

            Returns the time in seconds between adjacent middle reference level crossings in the same
              direction. The reciprocal of this value is the signal frequency.

               •      Duty Cycle —

             Calculates the Pulse duration as a fraction of the Period.


     CurveCurve FittingFitting

      Computes the coefficients that best represent the input data based on the chosen
      model type.


      Dialog Box Options

        Option   Description

       Model
                  Displays the data and results according to a mathematical model type you specify.
        Type


5958   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5958 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5959 ordinal=5959 -->
## Functions

Functions


Option   Description

        The model type can be any of the following options:

                • Linear—

             Finds the slope and intercept of the line that best represents the input data set in the
              least-squares sense.

                • Quadratic—

             Finds the polynomial curve of order 2 that best represents the input data set in the
              least-squares sense.

                • Spline—

             Returns the spline interpolant of length n.

      ncontains the second derivatives of the spline interpolating function g(x) at the
             tabulated points ξ, where i= 0, 1, …, n– 1.

                • Polynomial—

             Finds the set of polynomial fit coefficients that best represents the input data set in
             the least-squares sense.

      ◦ Polynomial order—

                Must be greater than or equal to zero. If Polynomial order is less than zero, the
                 Express VI returns an error. The default is 5. This option is available only when
               you select the Polynomial option.

               The value of polynomial order must observe the following relationship: 0 ≤ m<
        n– 1, where nis the number of sample points, and mis Polynomial order.

                • General least squares linear—

             Finds the k-dimension linear curve values and the set of k-dimension linear fit
               coefficients that best represents the input data set using the least-squares solution.

      ◦ Models—

                   Individual functions of the independent variable. This option is available only


                                                    © National Instruments 5959

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5959 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5960 ordinal=5960 -->
## Functions

Functions


        Option   Description

                    when you select the General least squares linear option.

                             In the following equation, the models are the functions of x, namely f0(x), f1(x),
                    …, fn – 1(x).                                           where a= {a0,

                              a1, a2, …, an – 1}

                             • Current Model—

                       Displays the formula for the currently selected Model Type. This display is available
                      only when you set Model Type to Linear, Quadratic, Spline, Polynomial, or General
                        least squares linear.

                             • Non-linear—

                    Uses the Levenberg-Marquardt algorithm to determine the set of coefficients of the
                      nonlinear model that best represents the input data set in the least-squares sense.
                   The nonlinear model is expressed by a nonlinear function y = f(x,a), where ais the set
                        of coefficients.

          ◦ Independent variable—

                            Specifies the independent variable in Non-linear model. This option is available
                          only when you select the Non-linear option.

          ◦ Maximum iterations—

                    Maximum number of executing iterations. If the Express VI reaches Maximum
                             iterations without finding a solution, the VI returns an error. You must increase
                   Maximum iterations or adjust Initial guesses to find a solution. The default is
                           500. This option is available only when you select the Non-linear option.

          ◦  Initial guesses—

                                  Initial guesses of the solution coefficients. This option is available only when you
                             select the Non-linear option.

                             • Non-linear model—

                        String that describes the model equation. This option is available only when you


5960   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5960 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5961 ordinal=5961 -->
## Functions

Functions


 Option   Description

               select the Non-linear option.


          Displays values generated for the parameters based on the options you select and values results         you enter.


          Displays the original data and the best fit.
 Data
 Graph   The VI calculates best fit using the following equation. zi = f(xi)A where Ais the best fit
           coefficient.


 Residue          Displays the difference between the original data and the best fit. Graph

Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Signals —

     Specifies the observed values of the dependent variable.

   •      Locations —

     Specifies the values of the independent variables.

   •      best fit —

    Returns the fitted data.

    The VI calculates best fit using the following equation. zi = f(xi)A where Ais the best fit
     coefficient.

   •      slope —


                                                    © National Instruments 5961

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5961 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5962 ordinal=5962 -->
## Functions

Functions


            Returns the slope of the calculated best linear fit.

               •      a0 —

            Returns the constant term of the calculated best quadratic fit.

               •      a2 —

            Returns the coefficient of the second-order term.

               •       spline interpolant —

            Returns the second derivative of interpolating function g(x).

             spline interpolant is the second derivative of interpolating function g(x) at points ξ, i = 0, 1,…, n
           – 1.

               •      non-linear coefficients —

            Returns the set of coefficients of the nonlinear model that best represents the input data set in
            the least-squares sense.

               •     mean squared error —

            Returns the mean square error of the best fit.

               •       intercept —

            Returns the intercept of the calculated best linear fit.

               •      polynomial coefficients —

            Returns the coefficients that describe the best polynomial fit. The total number of elements in
           polynomial coefficients is m+ 1, where mis Polynomial order.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      a1 —

            Returns the coefficient of the first-order term.

               •      general LS coefficients —


5962   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5962 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5963 ordinal=5963 -->
## Functions

Functions


    Returns the set of coefficients that best represent the input data set in the least-squares sense.

   •       residual —

    Returns the difference between the original data and the best fit.

FilterFilter

Processes signals through filters and windows.


Dialog Box Options

 Option        Description

                 Specifies the following types of filters to use: lowpass, highpass, bandpass, Filtering Type
               bandstop, or smoothing. The default is Lowpass.

               Contains the following options:

                          •  Cutoff Frequency (Hz)—

                      Specifies the cutoff frequency of the filter. This option is available only when
                 you select Lowpass or Highpass from the Filtering Type pull-down menu. The
                     default is 100.
 Filter
                          • Low cutoff frequency (Hz)—
 Specifications
                      Specifies the low cutoff frequency of the filter. Low cutoff frequency (Hz) must
                 be less than High cutoff frequency (Hz) and observe the Nyquist criterion. The
                     default is 100. This option is available only when you select Bandpass or
                 Bandstop from the Filtering Type pull-down menu.

                          • High cutoff frequency (Hz)—


                                                    © National Instruments 5963

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5963 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5964 ordinal=5964 -->
## Functions

Functions


        Option        Description

                              Specifies the high cutoff frequency of the filter. High cutoff frequency (Hz)
                        must be greater than Low cutoff frequency (Hz) and observe the Nyquist
                                 criterion. The default is 400. This option is available only when you select
                        Bandpass or Bandstop from the Filtering Type pull-down menu.

                                      •  Finite impulse response (FIR) filter—

                            Creates an FIR filter, which depends only on the current and past inputs.

                         Because the filter does not depend on past outputs, the impulse response
                          decays to zero in a finite amount of time. Because FIR filters return a linear
                         phase response, use FIR filters for applications that require linear phase
                            responses.

                                      • Taps—

                              Specifies the total number of FIR coefficients, which must be greater than zero.
                        The default is 29. This option is available only when you select the Finite
                          impulse response (FIR) filter option.

                             Increasing the value of Taps causes the transition between the passband and
                           the stopband to become steeper. However, as the value of Taps increases, the
                            processing speed becomes slower.

                                      •  Infinite impulse response (IIR) filter—

                            Creates an IIR filter that is a digital filter with impulse responses that can
                               theoretically be infinite in length or duration.

                                      • Topology—

                          Determines the design type of the filter. You can create either a Butterworth,
                          Chebyshev, Inverse Chebyshev, Elliptic, or Bessel filter design. This option is
                              available only when you select the Infinite impulse response (IIR) filter
                             option. The default is Butterworth.

                                      • Order—

                          Order of the IIR filter, which must be greater than zero. This option is available
                            only when you select the Infinite impulse response (IIR) filter option. The
                              default is 3.


5964   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5964 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5965 ordinal=5965 -->
## Functions

Functions


Option        Description

                    Increasing the value of Order causes the transition between the passband and
                   the stopband to become steeper. However, as the value of Order increases, the
                   processing speed becomes slower, and the number of distorted points at the
                       start of the signal increases.

                         • Moving average—

                     Yields forward-only (FIR) coefficients. This option is available only when you
                     select Smoothing from the Filtering Type pull-down menu.

                         • Rectangular—

                     Specifies that all samples in the moving-average window are weighted equally
                      in computing each smoothed output sample. This option is available only
               when you select Smoothing from the Filtering Type pull-down menu and the
                 Moving average option.

                         • Triangular—

                     Specifies that the moving weighting window applied to the samples is
                     triangular with the peak centered in the middle of the window, ramping down
                   symmetrically on both sides of the center sample. This option is available only
               when you select Smoothing from the Filtering Type pull-down menu and the
                 Moving average option.

                         • Half-width of moving average—

                     Specifies the half-width of the moving-average window in samples. The
                    default is 1. For a half-width of moving average of M, the full width of the
                  moving-average window is N = 1 + 2M samples. Therefore, the full width N is
                  always an odd number of samples. This option is available only when you
                     select Smoothing from the Filtering Type pull-down menu and the Moving
                  average option.

                         • Exponential—

                     Yields first-order IIR coefficients. This option is available only when you select
                Smoothing from the Filtering Type pull-down menu.

                         • Time constant of exponential average—


                                                    © National Instruments 5965

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5965 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5966 ordinal=5966 -->
## Functions

Functions


        Option        Description

                              Specifies the time constant of the exponential-weighting filter in seconds. The
                              default is 0.001. This option is available only when you select Smoothing from
                           the Filtering Type pull-down menu and the Exponential option.


                        Displays the input signal.

        Input Signal     If you wire data to the Express VI and run it, Input Signal displays real data. If you
                         close and reopen the Express VI, Input Signal displays sample data until you run
                       the Express VI again.


                        Displays a preview of the measurement. The Result Preview plot indicates the
                        value of the selected measurement with a dotted line.
         Result                                      If you wire data to the Express VI and run the VI, Result Preview displays real data.
        Preview                                      If you close and reopen the Express VI, Result Preview displays sample data until
                     you run the VI again. If the cutoff frequency values are invalid, Result Preview does
                       not display valid data.

                       Contains the following options:

                        Note Changing the options in the View Mode section does not impact
                                the behavior of the Filter Express VI. Use the View Mode options to
                                     visualize what the filter does to the signal. LabVIEW does not save these
                                options when you close the configuration dialog box.

                                      • Signals—

        View Mode         Displays the filter response as real signals.

                                      •  Transfer function—

                             Displays the filter response as a transfer function.

                                      • Show as spectrum—

                              Specifies whether to display the real signals of the filter response as a
                           frequency spectrum or to leave the display as a time-based display. The


5966   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5966 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5967 ordinal=5967 -->
## Functions

Functions


 Option        Description

                   frequency display is useful for viewing how the filter affects the various
                   frequency components of the signal. The default is to display the filter
                   response as a time-based display. This option is available only when you select
                   the Signals option.

               Contains the following options:

                          • Magnitude in dB—

                    Presents the magnitude response of the filter in decibels. Scale Mode
                          • Frequency in log—

                    Presents the frequency response of the filter on a logarithmic scale.


 Magnitude     Displays the magnitude response of the filter. This display is available only when
 Response     you set View Mode to Transfer function.


 Phase         Displays the phase response of the filter. This display is available only when you set
 Response     View Mode to Transfer function.


Inputs/Outputs

   •      Signal —

     Specifies the input signal. The signal can be a waveform, a real array, or a complex array.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •     Upper Cut-Off —

     Specifies the high cutoff frequency of the filter. Upper Cut-Off must be greater than Lower Cut-
    Off and observe the Nyquist criterion. The default is 400.

   •     Lower Cut-Off —


                                                    © National Instruments 5967

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5967 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5968 ordinal=5968 -->
## Functions

Functions


             Specifies the low cutoff frequency of the filter. Lower Cut-Off must be less than Upper Cut-Off
          and observe the Nyquist criterion. The default is 100.

               •       Filtered Signal —

            Returns the filtered signal.

               •       error out —

            Contains error information. This output provides standard error out functionality.


           Note Use the Filters PtByPt VIs to implement continuous, point-by-point
                  filtering.

       StatisticsStatistics

       Returns the selected parameter of the first signal in a waveform.


      Dialog Box Options

        Option         Description

                        Contains the following options:

                                       • Arithmetic mean—

                              Calculates the mean, or average, of the values in Signals.
          Statistical
                                       • Median—
         Calculations
                            Finds the median value in Signals. The Express VI sorts the values in Signals
                        and selects the middle element of the sorted values.

                                       • Mode—


5968   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5968 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5969 ordinal=5969 -->
## Functions

Functions


Option         Description

                    Finds the value that occurs most often in the values in Signals.

                          • Sum of values—

                     Calculates the value of the sum of all the values in Signals.

                          • Root mean square (RMS)—

                     Calculates the RMS of the values in Signals.

                          • Standard deviation—

                     Calculates the standard deviation of the values in Signals.

                          • Variance—

                     Calculates the calculated variance of the values in Signals.

                          • Kurtosis—

                     Calculates the kurtosis of the values in Signals. Kurtosis is a measure of
                  peakedness and is a normalized form of the fourth-order moment about the
                 mean.

                     Kurtosis is indicated by the following formula:

                     Kurtosis = Fourth Moment/σ4

                          • Skewness—

                     Calculates the skewness of the values in Signals. Skewness is a measure of
                 symmetry and is a normalized form of the third-order moment about the
                 mean.

                 Skewness is indicated by the following formula:

                 Skewness = Third Moment/σ3

               Contains the following options:
Extreme
Values                 • Maximum—


                                                    © National Instruments 5969

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5969 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5970 ordinal=5970 -->
## Functions

Functions


        Option         Description

                            Finds the highest point in a set of values in Signals.

                                       • Time of maximum—

                            Finds the time of the highest point in a set of values in Signals.

                                       • Index of maximum—

                            Finds the index value of the highest point in a set of values in Signals.

                                       • Minimum—

                            Finds the lowest point in a set of values in Signals.

                                       • Time of minimum—

                            Finds the time of the lowest point in a set of values in Signals.

                                       • Index of minimum—

                            Finds the index value of the lowest point in a set of values in Signals.

                                       • Range (maximum - minimum)—

                            Finds the value of the range from the lowest point to the highest point in a set
                               of values in Signals.

                                       •  First time—

                            Finds the first time value in a set of values in Signals.

                                       • Last time—

                            Finds the last time value in a set of values in Signals.

                                       •  First value—

                            Finds the first value in a set of values in Signals.

                                       • Last value—

                            Finds the last value in a set of values in Signals.


5970   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5970 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5971 ordinal=5971 -->
## Functions

Functions


 Option         Description

                Contains the following options:

                           •  Total number of samples—

 Sampling          Bases the calculation on the total number of samples in Signals.
 Characteristics
                           • Time between samples (dt)—

                   Bases the calculation on the time between samples in Signals.


                 Displays the input signal.

 Input Signal       If you wire data to the Express VI and run it, Input Signal displays real data. If you
                 close and reopen the Express VI, Input Signal displays sample data until you run
                the Express VI again.


                 Displays the measurements you configured this Express VI to perform and the
                 calculated values of those measurements. You can click any measurement listed in
 Results                the Measurement column, and the corresponding value or plot appears in the
                Result Preview graph.


Inputs/Outputs

   •      Signals —

    Contains the input signal or signals.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       error out —

    Contains error information. This output provides standard error out functionality.

   •     Minimum —

    Returns the lowest point in a set of values in Signals.


                                                    © National Instruments 5971

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5971 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5972 ordinal=5972 -->
## Functions

Functions

               •     Range —

            Returns the value of the range from the lowest point to the highest point in a set of values in
             Signals.

               •        First Value —

            Returns the first value in Signals.

               •      Last Value —

            Returns the last value in Signals.

               •      Arithmetic Mean —

            Returns the mean, or average, of the values in Signals.

               •      Standard Dev —

            Returns the standard deviation of the values in Signals.

               •     Median —

            Returns the median value in Signals. The Express VI sorts the values in Signals and selecting the
           middle element of the sorted values.

               •      Index of Min —

            Returns the index value of the lowest point of the values in Signals.

               •     Summation —

            Returns the value of the sum of all the values in Signals.

               •       Kurtosis —

            Returns the kurtosis of the values in Signals. Kurtosis is a measure of peakedness and
            corresponds to the fourth-order moment about the mean.

               •     Time of Maximum —

            Returns the time of the highest point of the values in Signals.

               •     Time of Minimum —


5972   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5972 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5973 ordinal=5973 -->
## Functions

Functions


  Returns the time of the lowest point of the values in Signals.

•      Last Time —

  Returns the last time value in Signals.

•     RMS —

  Returns the calculated RMS of the values in Signals.

•     Mode —

  Returns the value that occurs most often in the set values in Signals.

•       Total Samples —

  Returns the total number of samples in Signals.

•     Maximum —

  Returns the highest point in a set of values in Signals.

•     Time Delta —

  Returns the time between samples in Signals.

•      Index of Max —

  Returns the index value of the highest point of the values in Signals.

•        First Time —

  Returns the first time value in Signals.

•      Variance —

  Returns the calculated variance of the values in Signals.

•     Skewness —

  Returns the skewness of the values in Signals. Skewness is a measure of symmetry and
  corresponds to the third-order moment about the mean.


                                                   © National Instruments 5973

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5973 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5974 ordinal=5974 -->
## Functions

Functions

     Examples

       Refer to the following example files included with LabVIEW.

            • labview\examples\Express VIs\Express VI - Statistics.vi

     ConvolutionConvolution andand CorrelationCorrelation

      Performs convolution, deconvolution, or correlation on the input signals.


      Dialog Box Options

        Option     Description

                    Contains the following options:

                                 • Convolution—

                     Computes the convolution of the input signals.

                                 • Deconvolution—

                     Computes the deconvolution of the input signals.

                                 • Autocorrelation—         Signal
        Processing                     Computes the autocorrelation of the input signal.

                                 • Cross correlation—

                     Computes the cross correlation of the input signals.

                                 • Ignore time stamp—

                           Specifies to ignore the time stamp of the input signals. This option is available
                         only when you place a checkmark in the Convolution or Deconvolution checkbox.


5974   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5974 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5975 ordinal=5975 -->
## Functions

Functions


 Option     Description

                           If you place a checkmark in the Ignore time stamp checkbox, the resulting signal
               has the delay you expect with classic convolution. If you do not place a checkmark
                   in the checkbox, LabVIEW shifts the resulting signal negatively in time to
               compensate for the filter length.


             Displays sample input signals you can use as a reference to determine how the
             configuration options you select affect the actual input signals.
 Sample
 Input Data   If you wire data to the Express VI and run it, Sample Input Data displays real data. If
           you close and reopen the Express VI, Sample Input Data displays sample data until
           you run the VI again.


             Displays a preview of the measurement. The Result Preview plot indicates the value of
            the selected measurement with a dotted line.
 Result                    If you wire data to the Express VI and run the VI, Result Preview displays real data. If
 Preview           you close and reopen the Express VI, Result Preview displays sample data until you
            run the VI again. If the cutoff frequency values are invalid, Result Preview does not
             display valid data.


Inputs/Outputs

   •      Input1 —

    Contains the input signal X.

   •      Y —

    Contains the input signal Y.

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      output signals —

    Returns the convolution of X and Y.


                                                    © National Instruments 5975

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5975 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5976 ordinal=5976 -->
## Functions

Functions

               •       error out —

            Contains error information. This output provides standard error out functionality.

     SimulateSimulate SignalSignal

       Simulates a sine wave, square wave, triangle wave, sawtooth wave, or noise signal.


      Dialog Box Options

        Option   Description

                 Contains the following options:

                              • Signal type—

                    Type of waveform to simulate. You can simulate a sine wave, square wave, sawtooth
                     wave, triangle wave, or noise (DC).

                              • Frequency (Hz)—

                    Frequency in hertz of the waveform. The default is 10.1.

                              • Phase (deg)—
         Signal
                             Initial phase in degrees of the waveform. The default is 0.

                              • Amplitude—

                     Amplitude of the waveform. The default is 1.

                              • Offset—

                 DC offset of the signal. The default is 0.

                              • Duty cycle (%)—


5976   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5976 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5977 ordinal=5977 -->
## Functions

Functions


Option   Description

             Percentage of time a square wave remains high versus low over one period. The
              default is 50.

                 • Add noise—

            Adds noise to the simulated waveform.

                 • Noise type—

               Specifies the type of noise to add to the waveform. This option is available only when
            you place a checkmark in the Add Noise checkbox.

            You can add the following noise types:
      ◦ Uniform White Noise generates a signal that contains a uniformly distributed,
               pseudorandom pattern whose values are in the range [-a:a], where ais the
                 absolute value of Amplitude.
      ◦ Gaussian White Noise generates a signal that contains a Gaussian-distributed,
               pseudorandom pattern whose statistical profile is (µ,sigma) = (0,s), where sis
                 the absolute value of the specified Standard deviation.
      ◦  Periodic Random Noise generates a signal that contains periodic random noise
                  (PRN).
      ◦ Gamma Noise generates a signal that contains a pseudorandom pattern of
                  values that are the waiting times to the Order number event of a unit mean
                 Poisson process.
      ◦ Poisson Noise generates a signal that contains a pseudorandom sequence of
                  values that are the number of discrete events occurring in a given interval,
                   specified by Mean, of a unit rate Poisson process.
      ◦ Binomial Noise generates a signal that contains a binomially distributed,
               pseudorandom pattern whose values are the number of occurrences of an
                  event, given the probability of that event occurring and the number of trials.
      ◦  Bernoulli Noise generates a signal that contains a pseudorandom pattern of
                ones and zeros.
      ◦ MLS Sequence generates a signal that contains a maximum length sequence of
                ones and zeros using a modulo-2 primitive polynomial of order Polynomial
                  order.
      ◦ Inverse F Noise generates a signal that contains a continuous noise waveform
                 with a power spectral density that is inversely proportional to frequency over a
                   specified frequency range.
                 • Noise amplitude—


                                                    © National Instruments 5977

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5977 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5978 ordinal=5978 -->
## Functions

Functions


        Option   Description

                 Maximum absolute value the signal can have. The default is 0.6. This option is
                        available only when you select Uniform White Noise or Inverse F Noise from the
                     Noise type pull-down menu.

                              • Standard deviation—

                     Standard deviation of the noise you generate. The default is 0.6. This option is
                        available only when you select Gaussian White Noise from the Noise type pull-down
                   menu.

                              • Spectral amplitude—

                    Magnitude of the frequency domain components of the simulated signal. The default
                              is 0.6. This option is available only when you select Periodic Random Noise from the
                     Noise type pull-down menu.

                              • Order—

                        Specifies the event number of the unit mean Poisson process. The default is 0.6. This
                      option is available only when you select Gamma Noise from the Noise type pull-
                 down menu.

                              • Mean—

                        Specifies the interval of a unit rate Poisson process. The default is 0.6. This option is
                        available only when you select Poisson Noise from the Noise type pull-down menu.

                              •  Trial probability—

                        Probability that a given trial is TRUE. The default is 0.6. This option is available only
                 when you select Binomial Noise from the Noise type pull-down menu.

                              • One probability—

                        Specifies the probability that a given element of the signal is TRUE. The default is 0.6.
                       This option is available only when you select Bernoulli Noise from the Noise type
                     pull-down menu.

                              • Polynomial order—

                        Specifies the order of the modulo-2 primitive polynomial to use to generate the


5978   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5978 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5979 ordinal=5979 -->
## Functions

Functions


Option   Description

               signal. The default is 0.6. This option is available only when you select MLS Sequence
            from the Noise type pull-down menu.

                 • Seed number—

          When greater than 0, causes reseeding of the noise sample generator. The default is
               –1. LabVIEW maintains the internal seed state independently for each instance of this
              reentrant VI. For a specific instance of this VI, if Seed number is less than or equal to
                0, LabVIEW does not reseed the noise generator, and the noise generator resumes
             producing noise samples as a continuation of the previous noise sequence.

                 • Exponent—

               Specifies the exponent of the inverse-f spectral shape you want. The default is 1. This
             option is available only when you select Inverse F Noise from the Noise type pull-
          down menu.

         Contains the following options:

                 • Samples per second (Hz)—

            Sampling rate in samples per second. The default is 1000.

                 • Number of samples—

           Number of samples in the signal. The default is 100.

                 • Automatic—
Timing              Sets the Number of samples to be one-tenth of Samples per second (Hz).

                 •  Integer number of cycles—

              Sets the nearest frequency and Number of samples such that the waveform contains
           an integer number of cycles.

                 • Actual number of samples—

              Indicates the actual number of samples in the waveform when you select Integer
           number of cycles.


                                                    © National Instruments 5979

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5979 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5980 ordinal=5980 -->
## Functions

Functions


        Option   Description

                              • Actual frequency—

                        Indicates the actual frequency of the waveform when you select Integer number of
                        cycles.

                              • Simulate acquisition timing—

                      Simulates an acquisition rate comparable to an actual acquisition rate.

                              • Run as fast as possible—

                      Simulates the signal as quickly as the system allows.

                 Contains the following options:

                              • Absolute (date and time)—

                       Displays the timestamp in terms of time elapsed since 12:00 a.m., Friday, January 1,
       Time         1904, Universal Time [01-01-1904 00:00:00].
       Stamps
                              •  Relative to start of measurement—

                       Displays the timestamp in terms of seconds starting from zero. For example, 100 in
                         relative time equals 1 minute and 40 seconds.

                 Contains the following options:

                              • Reset phase, seed, and time stamps—

                      Resets the phase to the phase value and the time stamp to zero. Resets the seed
        Reset       number to –1.
         Signal
                              • Use continuous generation—

                     Continuously simulates the signal. Does not reset the phase, time stamp, or seed
                    number.

                 Contains the following options:
         Signal
      Name        • Use signal type name—


5980   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5980 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5981 ordinal=5981 -->
## Functions

Functions


 Option   Description

             Uses the default signal name.

                  • Signal name—

              Contains the following options:

 Result          Displays a preview of the signal to be simulated. Preview

Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •       Offset —

     Specifies the DC offset of the signal. The default is 0. The value you wire to this input overrides
    the value you set in the configuration dialog box.

   •      Phase —

     Specifies the initial phase in degrees of the signal. The default is 0. The value you wire to this
    input overrides the value you set in the configuration dialog box.

   •      Amplitude —

     Specifies the amplitude of the signal. The default is 1. The value you wire to this input overrides
    the value you set in the configuration dialog box.

   •      Duty Cycle (%) —

     Specifies the percentage of time a square wave remains high versus low over one period. The
     default is 50. The value you wire to this input overrides the value you set in the configuration
    dialog box.

   •      Noise Amplitude —

     Specifies the maximum absolute value the signal can have. The default is 0.6. The value you wire
    to this input overrides the value you set in the configuration dialog box.


                                                    © National Instruments 5981

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5981 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5982 ordinal=5982 -->
## Functions

Functions

               •      Standard deviation —

             Specifies the standard deviation of the noise you generate. The default is 0.6. The value you wire
             to this input overrides the value you set in the configuration dialog box.

               •      Spectral amplitude —

             Specifies the magnitude of the frequency domain components of the simulated signal. The
             default is 0.6. The value you wire to this input overrides the value you set in the configuration
             dialog box.

               •      Order —

             Specifies the event number of the unit mean Poisson process. The default is 0.6. The value you
            wire to this input overrides the value you set in the configuration dialog box.

               •     Mean —

             Specifies the interval of a unit rate Poisson process. The default is 0.6. The value you wire to this
            input overrides the value you set in the configuration dialog box.

               •       Trial probability —

             Specifies the probability that a given trial is TRUE. The default is 0.6. The value you wire to this
            input overrides the value you set in the configuration dialog box.

               •     One probability —

             Specifies the probability that a given element of the signal is TRUE. The default is 0.6. The value
           you wire to this input overrides the value you set in the configuration dialog box.

               •      Polynomial Order —

             Specifies the order of the modulo-2 primitive polynomial to use to generate the signal. The
             default is 0.6. The value you wire to this input overrides the value you set in the configuration
             dialog box.

               •      Exponent —

             Specifies the exponent of the inverse-f spectral shape you want. The default is 1. The value you
            wire to this input overrides the value you set in the configuration dialog box.

               •       Trials —


5982   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5982 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5983 ordinal=5983 -->
## Functions

Functions


     Specifies the number of trials performed for each element of the simulated signal. The default is
     1. The value you wire to this input overrides the value you set in the configuration dialog box.

   •      Reset Signal —

     Specifies when to reset the signal. The value you wire to this input overrides the value you set in
    the configuration dialog box.

   •     Seed Number —

    Reseeds the noise sample generator when this value is > 0. The default is –1. If seed is 0, the
    noise generator does not reseed and resumes producing noise samples as a continuation of the
    previous noise sequence. The value you wire to this input overrides the value you set in the
    configuration dialog box.

   •      Frequency —

     Specifies the frequency in hertz of the waveform. The default is 10.1. The value you wire to this
    input overrides the value you set in the configuration dialog box.

   •      Signal —

    Returns the output signal formatted as dynamic data.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Amplitude and
   Level Measurements.vi

MaskMask andand LimitLimit TestingTesting

Performs limit testing on Signals.


                                                    © National Instruments 5983

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5983 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5984 ordinal=5984 -->
## Functions

Functions


      Dialog Box Options

        Option   Description

                 Contains the following options:

                              • Upper constant—

                   Compares Signals to the value in Upper limit constant. This option is available only
                 when you place a checkmark in the Upper Limit checkbox.

          ◦ Upper limit constant—

                            Specifies the value of the Upper constant. The default is 0. This option is
                            available only when you place a checkmark in the Upper Limit checkbox and
                             select the Upper constant option.

                              • Upper mask—
       Upper                   Compares Signals to the upper limit of a signal from a file or a signal you define. This
         Limit                      option is available only when you place a checkmark in the Upper Limit checkbox.

          ◦ Define—

                           Displays the Define Signal dialog box, which you use to set the values for the
                             signal you want to use for the limit test. This button is available only when you
                             select Upper Limit and Upper mask or Lower Limit and Lower mask.

                              • Upper inclusive—

                        Specifies if you want Pass to return TRUE when points in Signals fall on Upper Limit.
                      Place a checkmark in the Upper inclusive checkbox to include points falling on
                   Upper Limit in the points that pass the limit test. This option is available only when
                   you place a checkmark in the Upper Limit checkbox.

                 Contains the following options:
       Lower
         Limit         • Lower constant—


5984   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5984 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5985 ordinal=5985 -->
## Functions

Functions


 Option   Description

            Compares Signals to the value in Lower limit constant. This option is available only
           when you place a checkmark in the Lower Limit checkbox.

       ◦ Lower limit constant—

                    Specifies the value of the Lower constant. The default is 0. This option is
                    available only when you place a checkmark in the Lower Limit checkbox and
                    select the Lower constant option.

                  • Lower mask—

            Compares Signals to the lower limit of a signal from a file or a signal you define. This
              option is available only when you place a checkmark in the Lower Limit checkbox.

       ◦ Define—

                   Displays the Define Signal dialog box, which you use to set the values for the
                    signal you want to use for the limit test. This button is available only when you
                    select Upper Limit and Upper mask or Lower Limit and Lower mask.

                  • Lower inclusive—

               Specifies if you want Pass to return TRUE when points in Signals fall on Lower Limit.
              Place a checkmark in the Lower inclusive checkbox to include points falling on
            Lower Limit in the points that pass the limit test. This option is available only when
            you place a checkmark in the Lower Limit checkbox.

          Displays a preview of the measurement. The Result Preview plot indicates the value of
          the selected measurement with a dotted line.

 Result     If you wire data to the Express VI and run the VI, Result Preview displays real data. If you
 Preview  close and reopen the Express VI, Result Preview displays sample data until you run the VI
           again. If the cutoff frequency values are invalid, Result Preview does not display valid
           data.


Inputs/Outputs

   •       error in —


                                                    © National Instruments 5985

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5985 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5986 ordinal=5986 -->
## Functions

Functions


            Describes error conditions that occur before this node runs.

               •      Signals —

            Contains the input signal or signals.

               •     Lower Limit —

             Specifies the lower limit for mask and limit testing. The value you wire to this input overrides the
            value you set in the configuration dialog box.

               •     Upper Constant —

          Compares Signals to the value in Upper Constant. The value you wire to this input overrides the
            value you set in the configuration dialog box.

               •     Lower Constant —

          Compares Signals to the value in Lower Constant. The value you wire to this input overrides the
            value you set in the configuration dialog box.

               •     Upper Limit —

             Specifies the upper limit for mask and limit testing. The value you wire to this input overrides
            the value you set in the configuration dialog box.

               •      Point Evaluation —

            Returns the results of the limit testing at each data point. If Point Evaluation is TRUE, the data
            point is less than or equal to the upper limit and greater than or equal to the lower limit.

               •      Tested Signals —

            Returns the upper and lower limits, the input signal, and the failures.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Passed —

             Indicates the result of limit testing. If Passed is TRUE, the signal is less than or equal to the upper
              limit and greater than or equal to the lower limit.


5986   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5986 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5987 ordinal=5987 -->
## Functions

Functions

The Express VI compares Signals with the upper and lower limits you set and returns
the result of the comparison at each data point. The Express VI also returns an array of
waveforms that contains the upper limit and lower limit, the signal, and the failures.

CreateCreate HistogramHistogram

Computes a histogram for Signal.


Dialog Box Options

 Option          Description

                 Contains the following options:

                            • Number of bins—

                       Specifies the number of bins in the histogram. The default is 10.

                            • Maximum value—

                       Specifies the maximum value to include in the histogram. The default is 3.
                      This is best used with floating-point inputs. The maximum value is not
                      included, so values that match it exactly are not included in the histogram. Configuration
                            • Minimum value—

                       Specifies the minimum value to include in the histogram. The default is –3.

                            • Auto Configure—

                     Automatically configures the histogram settings based on the input data.

                  The Auto Configure button is enabled only after you wire valid data to Signal.

 Amplitude
                 Contains the following options:
 Representation


                                                    © National Instruments 5987

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5987 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5988 ordinal=5988 -->
## Functions

Functions


        Option          Description

                                        • Percent of total—

                            Represents the value of each bin as a percentage of the total.

                                        • Sample count—

                            Represents the value of each bin as the number of samples in that bin.


                          Displays the input signal.

        Input Signal        If you wire data to the Express VI and run it, Input Signal displays real data. If you
                          close and reopen the Express VI, Input Signal displays sample data until you run
                        the Express VI again.


                          Displays a preview of the measurement. The Result Preview plot indicates the
                         value of the selected measurement with a dotted line.

         Result Preview   If you wire data to the Express VI and run the VI, Result Preview displays real data.
                                        If you close and reopen the Express VI, Result Preview displays sample data until
                      you run the VI again. If the cutoff frequency values are invalid, Result Preview
                      does not display valid data.


      Inputs/Outputs

               •      Reset —

            Controls the initialization of the internal state of the VI. The default is FALSE.

               •      Signal —

             Specifies the input signal. The signal can be a waveform, a real array, or a complex array.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •      Enable —


5988   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5988 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5989 ordinal=5989 -->
## Functions

Functions


    Enables or disables the Express VI. The default is ON or TRUE.

   •      Histogram —

    Returns the resulting histogram.

   •       error out —

    Contains error information. This output provides standard error out functionality.


Examples

Refer to the following example files included with LabVIEW.

  • labview\examples\Express VIs\Express VI - Statistics.vi

OutputOutput

Use the Output Express VIs to save data to files, to generate reports, to output real
world signals, to communicate with instruments, and to display messages to users.

      Note

      The DAQ Assistant Express VI does not appear on the Output palette unless
       you have NI-DAQmx installed. Refer to the DAQGettingStartedGuidefor
      more information about installing NI-DAQmx.

      The Instrument I/O Assistant Express VI does not appear on the Output
        palette unless you have the Instrument I/O Assistant installed. You install the
       Instrument I/O Assistant from the National Instruments Device Drivers DVD.

       You must have DIAdem 9.1 Service Pack 2 or later installed to use the DIAdem
       Report Express VI. Visit ni.com to download an evaluation version of DIAdem
        or purchase DIAdem.


                                                    © National Instruments 5989

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5989 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5990 ordinal=5990 -->
## Functions

Functions


         Palette                       Description        Object

                    Use Instrument Drivers VIs to configure, control, and retrieve data from GPIB, serial,
                      modular, PXI, and other types of instruments. Use the NI Instrument Driver Finder to        Instrument                       search for and install instrument drivers. If an instrument driver is not available, you         Drivers                     can use the Create New Instrument Driver Project wizard to create a new instrument
                           driver.


                       Creates an output string from a combination of text and parameterized inputs. If the
         Build Text     input is not a string, this Express VI converts the input into a string based on the
                        configuration of the Express VI.

         Display
        Message to    Displays a standard dialog box that contains an alert or a message for users.
        User

                       Plays data from the sound output device using finite sampling. This Express VI         Play
                       automatically configures an output task and clears the task after the output       Waveform                      completes.


         Write To                        Writes data to text-based measurement files (.lvm), binary measurement files
        Measurement
                   (.tdm or .tdms), or Microsoft Excel files (.xlsx).           File


                      Generates a preformatted report that contains VI documentation, data the VI
        Report
                         returns, and report properties, such as the author, company, and number of pages.


     InstrumentInstrument DriversDrivers

      Use Instrument Drivers VIs to configure, control, and retrieve data from GPIB, serial,
       modular, PXI, and other types of instruments. Use the NI Instrument Driver Finder to
       search for and install instrument drivers. If an instrument driver is not available, you

5990   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5990 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5991 ordinal=5991 -->
## Functions

Functions

can use the Create New Instrument Driver Project wizard to create a new instrument
driver.

The VIs and controls that appear on this palette change depending on the instrument
drivers you install. You can add new VIs and controls to this palette. Before you begin
using the Instrument Driver VIs, make sure you choose the appropriate method of
instrument control.


BuildBuild TextText

Creates an output string from a combination of text and parameterized inputs. If the
input is not a string, this Express VI converts the input into a string based on the
configuration of the Express VI.


Dialog Box Options

 Option            Description

                     Specifies the text you want to build. Define parameters by placing text between Text with
                 a pair of percent signs. You can use each parameter only once in the text that Parameters in
                 you build. Percents
 (%parameter                 To include a percent sign in the output string, you must type the percent sign
 name%)                     twice.

                   Contains the following options:

                               • Parameter— Configure
 Parameters                            Lists all parameters defined in the Text with Parameters in Percents
                    (%parameter name%) section.


                                                    © National Instruments 5991

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5991 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5992 ordinal=5992 -->
## Functions

Functions


        Option            Description

                                           • Sample text—

                                Displays text configured according to the options set in Parameter
                                 Properties.

                                           • Sample boolean—

                                Displays a button configured according to the options set in Parameter
                                 Properties.

                                           • Sample number—

                                Displays a number configured according to the options set in Parameter
                                 Properties.

                                           • Sample result—

                                Displays the value you enter in Sample text, Sample number, or Sample
                            boolean based on the options you select in the Parameter Properties
                                  section.

                          Contains the following options:

                                           • Text—

                             Formats the parameter as a text string.

                                           • Number—

                             Formats the parameter as a numeric value.
        Parameter
         Properties               • Boolean—

                             Formats the parameter as a Boolean value.

                                           • Format—

                               Provides formatting options for the parameter depending on the data type.
                            Examples of each format appear in parentheses after the name of the
                                format.


5992   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5992 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5993 ordinal=5993 -->
## Functions

Functions


Option            Description

                              • Use minimum field width—

                    Pads any excess space to the left or right of the text, number, or Boolean
                      with zeros or spaces to reach the minimum width you enter in Minimum
                          field width.

                              • Minimum field width—

                        Specifies the width to which you want to pad the text, number, or Boolean.
                   The default is 0.

                              • Use specified precision—

                     Formats the numbers with the precision you specify in Precision. This
                      option is available only when you select Fractional/Scientific (12.345),
                       Fractional (12.345), or Scientific (1.234E1) from the Format the numbers
                     pull-down menu.

                              • Precision—

                    Changes the digits of precision of the numbers in the table. The default is
                           0.

                  Contains the following options:

                              • Left—

                          Justifies the parameter to the left.Justification
                              • Right—

                          Justifies the parameter to the right.

                  Contains the following options:

                              • Using spaces—
Padding
                    Pads numbers using spaces.

                              • Using zeros—


                                                    © National Instruments 5993

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5993 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5994 ordinal=5994 -->
## Functions

Functions


        Option            Description

                            Pads numbers using zeros.


      Inputs/Outputs

               •      Beginning Text —

           Prepends the text you wire to this input to the text the Express VI generates.

               •       error in (no error) —

            Describes error conditions that occur before this node runs.

               •       error out —

            Contains error information. This output provides standard error out functionality.

               •      Result —

            Returns the resulting data based on the configuration of the Express VI.

      DisplayDisplay MessageMessage toto UserUser

       Displays a standard dialog box that contains an alert or a message for users.


      Dialog Box Options

        Option   Description

        Message
         to       Contains the text to display in the dialog box.
         Display

        Buttons  Contains the following options:


5994   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5994 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5995 ordinal=5995 -->
## Functions

Functions


 Option   Description

                  •  First button name—

                Specifies the text that appears on the first button. By default, the text on the first
              button is OK.

                  • Second button name—
 to
 Display       Specifies the text that appears on the second button. By default, the text on the
             second button is Cancel. This option is available only when you place a checkmark
                 in the Display second button checkbox.

                  • Display second button—

                Specifies whether a second button is displayed in the dialog box.


Inputs/Outputs

   •       error in (no error) —

    Describes error conditions that occur before this node runs.

   •      Enable —

    Enables or disables the Express VI. The default is ON or TRUE.

   •      Message —

    Contains the text to display in the dialog box.

   •     OK? —

    Returns TRUE when you click the first button in the dialog box and FALSE when you click the
    second button.

   •       error out —

    Contains error information. This output provides standard error out functionality.


                                                    © National Instruments 5995

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5995 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5996 ordinal=5996 -->
## Functions

Functions

      PlayPlay WaveformWaveform

       Plays data from the sound output device using finite sampling. This Express VI
       automatically configures an output task and clears the task after the output
       completes.

      (Windows) You must have DirectX 8.0 or later to use this VI. (Linux) You must have the
     Open Sound System (OSS) driver to use this VI.


      Dialog Box Options

        Option           Description

        Device              Lists the sound devices you have connected.

                          Contains the following options:

                                          • Min sample rate (Hz)—

                              Returns the minimum output sample rate the selected device supports.

                                          • Max sample rate (Hz)—

        Device               Returns the maximum output sample rate the selected device supports.
         capabilities
                                          • Resolution (bits)—

                                 Specifies the quality of each sample in bits. The default is 16 bits.

                                          • #Channels—

                                 Specifies the number of channels. 1 is Mono, and 2 is Stereo.


         Test Device        Tests the selected sound device by playing a 500 Hz tone for approximately 1/4


5996   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5996 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5997 ordinal=5997 -->
## Functions

Functions


 Option           Description

                  second.


Inputs/Outputs

   •      Device —

     Lists the sound devices you have connected.

   •       error in —

    The error in cluster can accept error information wired from VIs previously called. Use this
    information to decide if any functionality should be bypassed in the event of errors from other
     VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the
     error displayed.

   •      Data —

     Specifies the data this Express VI plays.

    You can wire a waveform, an array of waveforms (one waveform per channel), or the Data output
     of the Acquire Sound Express VI to this input. The Play Waveform Express VI uses the timing
    information the waveform data type specifies to play back sound.

   •       error out —

    The error out cluster passes error or warning information out of a VI to be used by other VIs. The
    pop-up option Explain Error (or Explain Warning) gives more information about the error
    displayed.

WriteWrite ToTo MeasurementMeasurement FileFile

Writes data to text-based measurement files (.lvm), binary measurement files (.tdm
or .tdms), or Microsoft Excel files (.xlsx).

Use the Read From Measurement File Express VI to read data from the generated
measurement file.


                                                    © National Instruments 5997

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5997 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5998 ordinal=5998 -->
## Functions

Functions


      Dialog Box Options

        Option      Description

                      Displays the full path to the file to which you want to write data. The Express VI writes
                    data to the file that this parameter specifies only if the Filename input is unwired. If
        Filename                  you wire the Filename input, the VI writes data to the file that this input specifies
                       instead.

                     Contains the following options:

                                  • Binary with XML Header (TDM)—

                       (Windows) Sets the file format to binary measurement file (.tdm) and the file
                         extension in Filename to .tdm.

                                         If you select this option, the Delimiter section and the No headers option in the
                     Segment Headers section are not available.

                   When you select this file format, you enable the Lock file for faster access
                        checkbox. Selecting this checkbox makes reading and writing significantly faster
                              (at the expense of the ability to multitask certain activities). It is recommended
          File Format                           that you use this option in most cases.

                         Note When this option is enabled, no two Express VIs can access the
                           same file at the same time when one of them is writing a "series of
                                               files."

                                  • Binary (TDMS)—

                          Sets the file format to binary measurement file (.tdms) and the file extension in
                       Filename to .tdms.

                                         If you select this option, the Delimiter section and the No headers option in the


5998   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5998 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5999 ordinal=5999 -->
## Functions

Functions


Option      Description

              Segment Headers section are not available.

                     • Text (LVM)—

                 Sets the file format to text-based measurement file (.lvm) and the file extension
                   in Filename to .lvm.

                     •  Microsoft Excel (.xlsx)—

                 Sets the file format to Microsoft Excel (.xlsx) and the file extension in Filename
                 to .xlsx.

                           If you select this option, the Delimiter section and the Segment Headers section
                 are unavailable.

                   Note This option does not require Microsoft Excel installed on the
                             local computer.


            Contains the following options:

                     • Save to one file—

                Saves all the data to one file.

                     • Ask user to choose file—

                 Displays a dialog box that prompts users to select a file. This option is available
                 only when you select the Save to one file option.
Action                     • Ask only once—

               Prompts users to select a file only once. This option is available only when you
                 place a checkmark in the Ask user to choose file checkbox.

                     • Ask each iteration—

               Prompts users to select a file each time the Express VI runs. This option is
                  available only when you place a checkmark in the Ask user to choose file
                checkbox.


                                                    © National Instruments 5999

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:5999 -->

<!--KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6000 ordinal=6000 -->
## Functions

Functions


        Option      Description

                                  • Save to series of files (multiple files)—

                        Saves the data to multiple files. If Reset is TRUE, the VI starts at the first file in the
                              series. For example, if test_001.lvm has been saved to test_004.lvm,
                   test_001.lvm might be renamed, overwritten, or skipped based on the value
                           of the Existing Files option in the Configure Multi-file Settings dialog box.

                                  • Settings—

                          Displays the Configure Multi-file Settings dialog box. This option is available only
                    when you select the Save to series of files (multiple files) option.

                     Contains the following options:

                                  • Rename existing file—

                     Renames the existing file if Reset is TRUE.

                                  • Use next available filename—

                      Appends the next sequential number to the filename if Reset is TRUE.

                         For example, if test.lvm exists, LabVIEW saves the file as test1.lvm.

             If a file            • Append to file—
         already
                      Appends the data to the existing file.          exists

                      The VI ignores the value of Reset if you select the Append to file option.

                         Note When you append data to an existing Excel file, errors might
                                 occur if the Excel file was not created by this Express VI. This option
                               does not support appending data to an Excel file that was created by a
                                     third-party application.

                                  • Overwrite file—

                         Replaces data in an existing file if Reset is TRUE.

       Segment
                     Contains the following options:
        Headers

6000   ni.com

<!--END_KB_RECORD source=NI_LABVIEW_PROGRAMMING_REFERENCE locator=page:6000 -->

